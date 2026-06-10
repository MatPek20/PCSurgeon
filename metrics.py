import psutil

class SystemMetric:
    def __init__(self, name: str):
        self.name = name

    def get_current_load(self) -> float:
        raise NotImplementedError("Subclasses must implement get_current_load()")

class CPUMetric(SystemMetric):
    def __init__(self):
        super().__init__(name="CPU")

    def get_current_load(self) -> float:
        return psutil.cpu_percent(interval=None)

class RAMMetric(SystemMetric):
    def __init__(self):
        super().__init__(name="RAM")

    def get_current_load(self) -> float:
        return psutil.virtual_memory().percent

import customtkinter as ctk
import math

class CTkCircularGauge(ctk.CTkCanvas):
    """Custom circular gauge UI component built on top of an optimized canvas."""
    def __init__(self, parent, size: int = 160, border_width: int = 12, 
                 fg_color: str = "#1c1d24", progress_color: str = "#00d2ff", **kwargs):
        
        # Initialize the underlying canvas with matching theme background masking
        super().__init__(parent, width=size, height=size, bg="#1c1d24", 
                         highlightthickness=0, bd=0, **kwargs)
        
        self.size = size
        self.border_width = border_width
        self.progress_color = progress_color
        
        # Calculate coordinate bounds for the circle arc
        self.padding = border_width // 2 + 2
        self.extent = size - self.padding
        
        # Draw the background track ring
        self.create_oval(self.padding, self.padding, self.extent, self.extent, 
                         outline="#282a36", width=self.border_width)
        
        # Create an empty arc handle that we can manipulate dynamically later
        self.arc = self.create_arc(self.padding, self.padding, self.extent, self.extent, 
                                   outline=self.progress_color, width=self.border_width, 
                                   style="arc", start=90, extent=0)
        
        # Add a central digital read-out text element
        self.text_id = self.create_text(size // 2, size // 2, text="0%", 
                                        fill="#ffffff", font=("Courier New", 16, "bold"))

    def set_value(self, percentage: float, prefix: str = ""):
        """Dynamically updates the visual arc geometry and text metrics."""
        percentage = max(0.0, min(100.0, percentage)) # Clamp bounds between 0 and 100
        
        # Convert percentage to degrees (360 degrees total, negative matching clockwise direction)
        degree_extent = -(percentage / 100.0) * 360
        
        # Re-configure canvas element attributes smoothly
        self.itemconfigure(self.arc, extent=degree_extent)
        self.itemconfigure(self.text_id, text=f"{prefix}\n{int(percentage)}%")