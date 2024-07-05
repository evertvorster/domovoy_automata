import os
import json
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

CONFIG_FILE = "plugins/test_plugin_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    else:
        return {"test_value": 50}

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

class TestPlugin:
    def __init__(self, parent):
        self.parent = parent
        self.config = load_config()

    def configure(self):
        dialog = TestPluginConfigDialog(self.config)
        dialog.exec()
        if dialog.result() == QDialog.Accepted:
            self.config = dialog.config
            save_config(self.config)

class TestPluginConfigDialog(QDialog):
    def __init__(self, config):
        super().__init__()
        self.setWindowTitle("Configure Test Plugin")
        self.config = config
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel(f"Test Value: {self.config['test_value']}")
        layout.addWidget(self.label)

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_value)
        layout.addWidget(self.edit_button)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_config)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def edit_value(self):
        new_value, ok = QInputDialog.getInt(self, "Edit Test Value", "Enter new value:", value=self.config["test_value"], minValue=0, maxValue=100)
        if ok:
            self.config["test_value"] = new_value
            self.label.setText(f"Test Value: {self.config['test_value']}")

    def save_config(self):
        save_config(self.config)
        self.accept()
