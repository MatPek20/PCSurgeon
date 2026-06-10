import os
import sys

# Crucial fix for Antigravity IDE directory mapping environments
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine import SurgeonEngine
from metrics import CPUMetric, RAMMetric
from ui import PCSurgeonUI

def main():
    # Instantiate standalone layer instances
    backend_processor = SurgeonEngine()
    cpu_monitor = CPUMetric()
    ram_monitor = RAMMetric()

    # Dynamic interface constructor initialization
    app = PCSurgeonUI(
        engine=backend_processor, 
        cpu_tracker=cpu_monitor, 
        ram_tracker=ram_monitor
    )
    app.mainloop()

if __name__ == "__main__":
    main()