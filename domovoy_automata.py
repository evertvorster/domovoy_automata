import sys
import json
import os
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QDialog, QLineEdit, QInputDialog, QFormLayout
from PySide6.QtCore import QTimer

CONFIG_FILE = "config.json"
PLUGINS_DIR = "plugins"

class DomovoyAutomata(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = self.load_config()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(5000)  # Update status every 5 seconds

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            return {"plugins": []}
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
            for plugin in config["plugins"]:
                if not os.path.exists(os.path.join(PLUGINS_DIR, plugin)):
                    raise ValueError(f"Plugin {plugin} does not exist in the plugins directory.")
            return config
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error loading config file: {e}. Using default configuration.")
            return {"plugins": []}

    def save_config(self):
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=4)

    def initUI(self):
        self.setWindowTitle("Domovoy Automata")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.plugin_list = QListWidget()
        layout.addWidget(self.plugin_list)

        self.configure_button = QPushButton("Configure")
        self.configure_button.clicked.connect(self.configure)
        layout.addWidget(self.configure_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.update_plugin_list()

    def update_plugin_list(self):
        self.plugin_list.clear()
        for plugin in self.config["plugins"]:
            item = QListWidgetItem(plugin)
            widget = QWidget()
            layout = QHBoxLayout()

            name_label = QLabel(plugin)
            layout.addWidget(name_label)

            status_label = QLabel("Unknown")
            layout.addWidget(status_label)

            start_button = QPushButton("Start")
            start_button.clicked.connect(lambda _, p=plugin: self.start_plugin(p))
            layout.addWidget(start_button)

            stop_button = QPushButton("Stop")
            stop_button.clicked.connect(lambda _, p=plugin: self.stop_plugin(p))
            layout.addWidget(stop_button)

            restart_button = QPushButton("Restart")
            restart_button.clicked.connect(lambda _, p=plugin: self.restart_plugin(p))
            layout.addWidget(restart_button)

            widget.setLayout(layout)
            item.setSizeHint(widget.sizeHint())
            self.plugin_list.addItem(item)
            self.plugin_list.setItemWidget(item, widget)

    def start_plugin(self, plugin):
        plugin_path = os.path.join(PLUGINS_DIR, plugin)
        try:
            subprocess.Popen(["python", plugin_path])
        except Exception as e:
            print(f"Error starting plugin {plugin}: {e}")

    def stop_plugin(self, plugin):
        # This is a placeholder. Implement plugin stop logic.
        print(f"Stopping plugin {plugin}...")

    def restart_plugin(self, plugin):
        self.stop_plugin(plugin)
        self.start_plugin(plugin)

    def update_status(self):
        # This is a placeholder. Implement logic to check plugin status.
        pass

    def configure(self):
        subprocess.call(["python", "configure.py"])

def main():
    app = QApplication(sys.argv)
    ex = DomovoyAutomata()
    ex.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
