import psutil
from PySide6.QtCore import QTimer

class Cpu_monitor:
    def __init__(self, main_program):
        self.main_program = main_program
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_cpu)
        self.timer.start(1000)  # Check CPU every second

    def check_cpu(self):
        cpu_usage = psutil.cpu_percent()
        if cpu_usage > 80:  # Threshold for demo purposes
            self.notify_main_program(cpu_usage)

    def notify_main_program(self, cpu_usage):
        print(f"CPU Usage High: {cpu_usage}%")
