import customtkinter as ctk
import threading
import os
from tkinter import filedialog, messagebox
from metrics import CPUMetric, RAMMetric, CTkCircularGauge # Imported our new Gauge!
from engine import SurgeonEngine

class PCSurgeonUI(ctk.CTk):
    def __init__(self, engine: SurgeonEngine, cpu_tracker: CPUMetric, ram_tracker: RAMMetric):
        super().__init__()
        
        self.engine = engine
        self.cpu_tracker = cpu_tracker
        self.ram_tracker = ram_tracker

        self.title("PC SURGEON PRO // ULTIMATE GRAPHICS")
        self.geometry("980x700")
        ctk.set_appearance_mode("dark")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._assemble_sidebar()
        self._assemble_main_viewport()
        
        self._switch_view("dashboard")
        self._run_live_hardware_daemon()

    def _assemble_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=180, corner_radius=0, fg_color="#111215")
        sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(sidebar, text="⚡ SURGEON // PRO", font=("Arial", 20, "bold"), text_color="#00d2ff").grid(row=0, column=0, padx=20, pady=30)
        
        self.btn_dash = ctk.CTkButton(sidebar, text="📊 Dashboard", fg_color="transparent", text_color="#a0a5b5", hover_color="#1c1d24", anchor="w", command=lambda: self._switch_view("dashboard"))
        self.btn_dash.grid(row=1, column=0, padx=15, pady=5, sticky="ew")

        self.btn_vault = ctk.CTkButton(sidebar, text="🔒 Secure Vault", fg_color="transparent", text_color="#a0a5b5", hover_color="#1c1d24", anchor="w", command=lambda: self._switch_view("vault"))
        self.btn_vault.grid(row=2, column=0, padx=15, pady=5, sticky="ew")

        self.btn_clones = ctk.CTkButton(sidebar, text="📂 File Clones", fg_color="transparent", text_color="#a0a5b5", hover_color="#1c1d24", anchor="w", command=lambda: self._switch_view("clones"))
        self.btn_clones.grid(row=3, column=0, padx=15, pady=5, sticky="ew")

        self.btn_net = ctk.CTkButton(sidebar, text="🌐 Net Diagnostics", fg_color="transparent", text_color="#a0a5b5", hover_color="#1c1d24", anchor="w", command=lambda: self._switch_view("network"))
        self.btn_net.grid(row=4, column=0, padx=15, pady=5, sticky="ew")

    def _assemble_main_viewport(self):
        self.viewport = ctk.CTkFrame(self, corner_radius=0, fg_color="#16171b")
        self.viewport.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        self.pane_dash = ctk.CTkFrame(self.viewport, fg_color="transparent")
        self.pane_vault = ctk.CTkFrame(self.viewport, fg_color="transparent")
        self.pane_clones = ctk.CTkFrame(self.viewport, fg_color="transparent")
        self.pane_net = ctk.CTkFrame(self.viewport, fg_color="transparent")

        self._build_dashboard_widgets()
        self._build_vault_widgets()
        self._build_clones_widgets()
        self._build_network_widgets()

    def _build_dashboard_widgets(self):
        """Builds a dashboard utilizing glowing circular data metrics."""
        ctk.CTkLabel(self.pane_dash, text="SYSTEM OVERLAYS", font=("Arial", 22, "bold"), text_color="#ffffff").pack(pady=(20, 10), anchor="w", padx=30)
        
        # Horizontal Card Holder
        cards_frame = ctk.CTkFrame(self.pane_dash, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=10)

        # UPGRADED: CPU Metric Card containing custom circular matrix
        cpu_card = ctk.CTkFrame(cards_frame, fg_color="#1c1d24", corner_radius=12)
        cpu_card.pack(side="left", fill="both", expand=True, padx=10)
        
        self.cpu_gauge = CTkCircularGauge(cpu_card, size=150, border_width=12, progress_color="#00d2ff")
        self.cpu_gauge.pack(pady=15)

        # UPGRADED: RAM Metric Card containing custom circular matrix
        ram_card = ctk.CTkFrame(cards_frame, fg_color="#1c1d24", corner_radius=12)
        ram_card.pack(side="left", fill="both", expand=True, padx=10)
        
        self.ram_gauge = CTkCircularGauge(ram_card, size=150, border_width=12, progress_color="#2ecc71")
        self.ram_gauge.pack(pady=15)

        # Live Core Hogs Console Box Layout
        ctk.CTkLabel(self.pane_dash, text="CORE IMAGE TASK SCHEDULER", font=("Arial", 12, "bold"), text_color="#6272a4").pack(pady=(20, 2), anchor="w", padx=30)
        self.proc_output = ctk.CTkTextbox(self.pane_dash, height=160, font=("Courier New", 12), fg_color="#0d0e11", text_color="#f8f8f2", border_color="#282a36", border_width=1)
        self.proc_output.pack(pady=5, padx=30, fill="x")

        # Action Optimization Controller
        self.opt_btn = ctk.CTkButton(self.pane_dash, text="RUN INTENSIVE SURGICAL OPTIMIZATION", height=45, fg_color="#00d2ff", hover_color="#00a8cc", text_color="#111215",
                      font=("Arial", 14, "bold"), command=self._handle_cleanup_trigger)
        self.opt_btn.pack(pady=30, padx=30, fill="x")

    def _build_vault_widgets(self):
        ctk.CTkLabel(self.pane_vault, text="CRYPTOGRAPHIC PROTOCOLS", font=("Arial", 22, "bold"), text_color="#ffffff").pack(pady=(30, 20), padx=30, anchor="w")
        
        vault_card = ctk.CTkFrame(self.pane_vault, fg_color="#1c1d24", corner_radius=12)
        vault_card.pack(pady=10, padx=30, fill="x")

        ctk.CTkLabel(vault_card, text="AES-256 Symmetric Encryption System", font=("Arial", 14, "bold"), text_color="#ff5555").pack(pady=15, padx=20, anchor="w")
        self.txt_pass = ctk.CTkEntry(vault_card, placeholder_text="Assign Cipher Handshake Password Key", show="*", width=450, fg_color="#0d0e11", border_color="#282a36")
        self.txt_pass.pack(pady=10, padx=20, anchor="w")

        box = ctk.CTkFrame(vault_card, fg_color="transparent")
        box.pack(pady=20, padx=20, anchor="w")
        ctk.CTkButton(box, text="🔒 Lock Local Asset", fg_color="#ff5555", hover_color="#ff3333", font=("Arial", 13, "bold"), command=lambda: self._handle_vault_trigger(encrypt=True)).pack(side="left", padx=(0, 15))
        ctk.CTkButton(box, text="🔓 Unlock Crypto Block", fg_color="#3498db", hover_color="#2980b9", font=("Arial", 13, "bold"), command=lambda: self._handle_vault_trigger(encrypt=False)).pack(side="left")

    def _build_clones_widgets(self):
        ctk.CTkLabel(self.pane_clones, text="DATA STRUCTURE INTELLIGENCE", font=("Arial", 22, "bold"), text_color="#ffffff").pack(pady=(30, 10), padx=30, anchor="w")
        ctk.CTkButton(self.pane_clones, text="📂 Target Storage Pathway for Verification", fg_color="#bd93f9", hover_color="#a370f7", text_color="#111215", font=("Arial", 13, "bold"), command=self._handle_clone_trigger).pack(pady=15, padx=30, anchor="w")
        self.txt_output = ctk.CTkTextbox(self.pane_clones, height=300, font=("Courier New", 12), fg_color="#0d0e11", text_color="#50fa7b", border_color="#282a36", border_width=1)
        self.txt_output.pack(pady=10, padx=30, fill="both", expand=True)

    def _build_network_widgets(self):
        ctk.CTkLabel(self.pane_net, text="NETWORK METRICS AND LATENCY", font=("Arial", 22, "bold"), text_color="#ffffff").pack(pady=(30, 20), padx=30, anchor="w")
        net_card = ctk.CTkFrame(self.pane_net, fg_color="#1c1d24", corner_radius=12)
        net_card.pack(pady=10, padx=30, fill="x")
        self.net_status_lbl = ctk.CTkLabel(net_card, text="ICMP Gateway Relay State: [PENDING USER LOG]", font=("Courier New", 15, "bold"), text_color="#f1fa8c")
        self.net_status_lbl.pack(pady=30, padx=20, anchor="w")
        self.net_btn = ctk.CTkButton(net_card, text="Ping Gateway Node", fg_color="#f1fa8c", hover_color="#f4f99d", text_color="#111215", font=("Arial", 13, "bold"), command=self._handle_network_trigger)
        self.net_btn.pack(pady=(0, 20), padx=20, anchor="w")

    def _switch_view(self, target_name: str):
        self.pane_dash.pack_forget()
        self.pane_vault.pack_forget()
        self.pane_clones.pack_forget()
        self.pane_net.pack_forget()

        self.btn_dash.configure(fg_color="transparent", text_color="#a0a5b5")
        self.btn_vault.configure(fg_color="transparent", text_color="#a0a5b5")
        self.btn_clones.configure(fg_color="transparent", text_color="#a0a5b5")
        self.btn_net.configure(fg_color="transparent", text_color="#a0a5b5")

        if target_name == "dashboard": 
            self.pane_dash.pack(fill="both", expand=True)
            self.btn_dash.configure(fg_color="#1c1d24", text_color="#00d2ff")
        elif target_name == "vault": 
            self.pane_vault.pack(fill="both", expand=True)
            self.btn_vault.configure(fg_color="#1c1d24", text_color="#ff5555")
        elif target_name == "clones": 
            self.pane_clones.pack(fill="both", expand=True)
            self.btn_clones.configure(fg_color="#1c1d24", text_color="#bd93f9")
        elif target_name == "network": 
            self.pane_net.pack(fill="both", expand=True)
            self.btn_net.configure(fg_color="#1c1d24", text_color="#f1fa8c")

    def _run_live_hardware_daemon(self):
        """Asynchronous update loop feeding our custom circular components."""
        cpu_load = self.cpu_tracker.get_current_load()
        ram_load = self.ram_tracker.get_current_load()

        # Update circular component states smoothly
        self.cpu_gauge.set_value(cpu_load, prefix="CPU")
        self.ram_gauge.set_value(ram_load, prefix="RAM")

        # Color mutation warning safeguards
        if cpu_load > 85: self.cpu_gauge.itemconfigure(self.cpu_gauge.arc, outline="#ff5555")
        else: self.cpu_gauge.itemconfigure(self.cpu_gauge.arc, outline="#00d2ff")

        def process_worker():
            hogs = self.engine.get_top_processes()
            self.after(0, lambda: self._update_process_ui(hogs))

        threading.Thread(target=process_worker, daemon=True).start()
        self.after(1500, self._run_live_hardware_daemon)

    def _update_process_ui(self, process_list):
        self.proc_output.delete("0.0", "end")
        self.proc_output.insert("end", f"{'IMAGE POOL RUNTIME':<32} | {'PROCESSOR CORE':<16} | {'RAM SHARE':<10}\n" + "—"*64 + "\n")
        for p in process_list:
            self.proc_output.insert("end", f"> {p['name'][:24]:<30} | {p['cpu_percent']:>10.1f} % | {p['memory_percent']:>8.1f} %\n")

    def _handle_cleanup_trigger(self):
        self.opt_btn.configure(state="disabled", text="PURGING STORAGE CACHE TARGET DATA...")
        def worker():
            cleared = self.engine.execute_cache_cleanup()
            self.after(0, lambda: messagebox.showinfo("System Registry Notification", f"Purge routine absolute.\nCleared {cleared} temporary workspace elements.", parent=self))
            self.after(0, lambda: self.opt_btn.configure(state="normal", text="RUN INTENSIVE SURGICAL OPTIMIZATION"))
        threading.Thread(target=worker, daemon=True).start()

    def _handle_vault_trigger(self, encrypt: bool):
        passkey = self.txt_pass.get()
        if not passkey: return messagebox.showwarning("Signature Fault", "Cryptographic operation requires a cipher passphrase vector.", parent=self)
        
        if encrypt:
            target_file = filedialog.askopenfilename()
            if target_file:
                if self.engine.secure_file_lock(target_file, passkey):
                    self.txt_pass.delete(0, 'end') 
                    messagebox.showinfo("Vault Confirmation", "Structural data successfully locked into an isolated crypt-cipher array.", parent=self)
        else:
            target_file = filedialog.askopenfilename(filetypes=[("Locked Structural Arrays", "*.locked")])
            if target_file:
                if self.engine.secure_file_unlock(target_file, passkey):
                    self.txt_pass.delete(0, 'end') 
                    messagebox.showinfo("Vault Confirmation", "Reverse-decryption process complete. File block accessible.", parent=self)
                else:
                    messagebox.showerror("Security Threat Detection", "Unauthorized credentials. Decryption aborted.", parent=self)

    def _handle_clone_trigger(self):
        folder = filedialog.askdirectory()
        if not folder: return
        self.txt_output.delete("0.0", "end")
        self.txt_output.insert("end", f"[ROOT_SCAN]: Initializing target directory query -> {folder}\n[HASHING]: Testing cryptographic checksum file indexes...\n\n")

        def worker():
            clones = self.engine.scan_for_duplicates(folder)
            self.after(0, lambda: self._render_clones_results(clones))
        threading.Thread(target=worker, daemon=True).start()

    def _render_clones_results(self, records: list):
        if not records:
            self.txt_output.insert("end", ">> SCAN REFRESH COMPLETE: No clone files matching existing signatures found.")
            return
        for copy, primary in records:
            self.txt_output.insert("end", f"⚠️ CLONE SIGNATURE DUPLICATION IDENTIFIED:\n -> Redundant Path: {copy}\n -> Original Safe Reference: {primary}\n\n")

    def _handle_network_trigger(self):
        self.net_btn.configure(state="disabled", text="PINGING GATEWAY ADDRESS...")
        def worker():
            result = self.engine.test_network_latency()
            self.after(0, lambda: self._update_network_ui(result))
        threading.Thread(target=worker, daemon=True).start()

    def _update_network_ui(self, outcome):
        self.net_status_lbl.configure(text=f"ICMP Gateway Relay State: {outcome}")
        self.net_btn.configure(state="normal", text="Ping Gateway Node")