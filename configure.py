import json
import os
import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QListWidget, QMessageBox, QInputDialog

CONFIG_FILE = "config.json"
PLUGIN_DIR = "plugins"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            try:
                config = json.load(file)
                if "plugins" not in config:
                    config["plugins"] = []
                return config
            except json.JSONDecodeError:
                print("Error: Config file is not valid JSON. Using default configuration.")
                return {"plugins": []}
    else:
        return {"plugins": []}

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

class ConfigureDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configure Domovoy Automata")
        self.config = load_config()
        self.available_plugins = self.scan_plugins()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.plugins_list = QListWidget()
        for plugin_name in self.config["plugins"]:
            self.plugins_list.addItem(plugin_name)
        layout.addWidget(self.plugins_list)

        add_button = QPushButton("Add Plugin")
        add_button.clicked.connect(self.add_plugin)
        layout.addWidget(add_button)

        remove_button = QPushButton("Remove Plugin")
        remove_button.clicked.connect(self.remove_plugin)
        layout.addWidget(remove_button)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_config)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def scan_plugins(self):
        plugins = []
        for filename in os.listdir(PLUGIN_DIR):
            if filename.endswith(".py") and filename != "__init__.py":
                plugin_name = filename[:-3]
                plugins.append(plugin_name)
            elif filename.endswith(".so") or filename.endswith(".dll"):
                plugin_name = filename
                plugins.append(plugin_name)
        return plugins

    def add_plugin(self):
        plugin_name, ok = QInputDialog.getItem(self, "Add Plugin", "Select Plugin:", self.available_plugins, 0, False)
        if ok and plugin_name:
            if plugin_name not in self.config["plugins"]:
                self.config["plugins"].append(plugin_name)
                self.plugins_list.addItem(plugin_name)
            else:
                QMessageBox.warning(self, "Error", f"Plugin {plugin_name} is already added.")

    def remove_plugin(self):
        current_item = self.plugins_list.currentItem()
        if current_item:
            plugin_name = current_item.text()
            self.config["plugins"].remove(plugin_name)
            self.plugins_list.takeItem(self.plugins_list.row(current_item))

    def save_config(self):
        save_config(self.config)
        self.accept()

def main():
    app = QApplication(sys.argv)
    dialog = ConfigureDialog()
    dialog.exec()

if __name__ == "__main__":
    main()
