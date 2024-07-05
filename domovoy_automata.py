import sys
import os
import importlib
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Slot

class DomovoyAutomata(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Domovoy Automata")

        self.plugins = []
        self.load_plugins()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.configure_button = QPushButton("Configure", self)
        self.configure_button.clicked.connect(self.configure)
        layout.addWidget(self.configure_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def load_plugins(self):
        plugins_dir = "./plugins"
        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py"):
                plugin_name = filename[:-3]
                module = importlib.import_module(f"plugins.{plugin_name}")
                plugin_class = getattr(module, plugin_name.capitalize())
                plugin_instance = plugin_class(self)
                self.plugins.append(plugin_instance)

    @Slot()
    def configure(self):
        os.system('python configure.py')

def main():
    app = QApplication(sys.argv)
    ex = DomovoyAutomata()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
