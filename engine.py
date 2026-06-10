import os
import shutil
import hashlib
import base64
import psutil
import socket
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SurgeonEngine:
    def __init__(self):
        self._static_salt = b'\x99\x11\x22\x33\x44\x55\x66\x77' 

    def _derive_crypto_key(self, password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self._static_salt,
            iterations=100000
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def execute_cache_cleanup(self) -> int:
        target_paths = [os.environ.get('TEMP'), r'C:\Windows\Temp']
        deleted_count = 0
        for path in target_paths:
            if not path or not os.path.exists(path): continue
            for filename in os.listdir(path):
                full_path = os.path.join(path, filename)
                try:
                    if os.path.isfile(full_path) or os.path.islink(full_path):
                        os.unlink(full_path)
                    elif os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                    deleted_count += 1
                except: continue
        return deleted_count

    def get_top_processes(self) -> list:
        """Fetches the top 5 resource-heavy running processes."""
        processes = []
        for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
            try:
                info = proc.info
                if info['name'] and info['cpu_percent'] is not None:
                    processes.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]

    def test_network_latency(self) -> str:
        """Measures connection ping stability by requesting a real webpage over HTTP/HTTPS."""
        import urllib.request
        import time

        # We connect to a real web address that always allows browser-like traffic
        url = "http://www.google.com"
        timeout = 2
        times = []
        
        for _ in range(3):
            try:
                start = time.time()
                # Open a standard web request
                response = urllib.request.urlopen(url, timeout=timeout)
                response.read() # Read the data response
                times.append((time.time() - start) * 1000)
            except Exception:
                return "Offline / Request Timeout"
        
        avg_ping = round(sum(times) / len(times), 1)
        if avg_ping < 40: return f"🚀 Excellent ({avg_ping} ms)"
        elif avg_ping < 120: return f"🟡 Stable ({avg_ping} ms)"
        else: return f"⚠️ High Latency ({avg_ping} ms)"

    def scan_for_duplicates(self, target_directory: str) -> list:
        seen_hashes = {}
        detected_clones = []
        for dirpath, _, filenames in os.walk(target_directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if os.path.islink(file_path): continue
                try:
                    hasher = hashlib.sha256()
                    with open(file_path, 'rb') as open_file:
                        for chunk in iter(lambda: open_file.read(4096), b""):
                            hasher.update(chunk)
                    calculated_hash = hasher.hexdigest()
                    
                    if calculated_hash in seen_hashes:
                        detected_clones.append((file_path, seen_hashes[calculated_hash]))
                    else:
                        seen_hashes[calculated_hash] = file_path
                except: continue
        return detected_clones

    def secure_file_lock(self, file_path: str, password: str) -> bool:
        try:
            cipher = Fernet(self._derive_crypto_key(password))
            with open(file_path, "rb") as f: data = f.read()
            with open(file_path + ".locked", "wb") as f: f.write(cipher.encrypt(data))
            os.remove(file_path)
            return True
        except: return False

    def secure_file_unlock(self, file_path: str, password: str) -> bool:
        try:
            cipher = Fernet(self._derive_crypto_key(password))
            with open(file_path, "rb") as f: data = f.read()
            original_path = file_path.replace(".locked", "")
            with open(original_path, "wb") as f: f.write(cipher.decrypt(data))
            os.remove(file_path)
            return True
        except: return False