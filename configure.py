import json
import os
import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QPushButton, QLineEdit, QListWidget, 
    QInputDialog, QMessageBox, QWidget, QLabel, QHBoxLayout
)

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    else:
        return {"cpu_threshold": 80, "mount_points": {}}

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

class ConfigureDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configure Domovoy Automata")
        self.config = load_config()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.cpu_edit = QLineEdit(str(self.config["cpu_threshold"]))
        layout.addLayout(self.create_row("CPU Threshold:", self.cpu_edit))

        self.mount_points_list = QListWidget()
        for mp, settings in self.config["mount_points"].items():
            self.mount_points_list.addItem(f"{mp} - {settings['name']} - {settings['threshold']}%")
        layout.addWidget(self.mount_points_list)

        add_button = QPushButton("Add Mount Point")
        add_button.clicked.connect(self.add_mount_point)
        layout.addWidget(add_button)

        edit_button = QPushButton("Edit Mount Point")
        edit_button.clicked.connect(self.edit_mount_point)
        layout.addWidget(edit_button)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_config)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def create_row(self, label_text, widget):
        row = QHBoxLayout()
        row.addWidget(QLabel(label_text))
        row.addWidget(widget)
        return row

    def add_mount_point(self):
        mount_point, ok = QInputDialog.getText(self, "Add Mount Point", "Enter Mount Point Path:")
        if ok:
            name, ok = QInputDialog.getText(self, "Add Mount Point", "Enter User Definable Name:")
            if ok:
                threshold, ok = QInputDialog.getInt(self, "Add Mount Point", "Enter Disk Threshold (%):", minValue=0, maxValue=100)
                if ok:
                    if os.path.exists(mount_point):
                        self.config["mount_points"][mount_point] = {"name": name, "threshold": threshold}
                        self.mount_points_list.addItem(f"{mount_point} - {name} - {threshold}%")
                    else:
                        QMessageBox.warning(self, "Error", f"Mount point {mount_point} does not exist.")

    def edit_mount_point(self):
        current_item = self.mount_points_list.currentItem()
        if current_item:
            mount_point = current_item.text().split(" - ")[0]
            current_settings = self.config["mount_points"][mount_point]

            new_name, ok = QInputDialog.getText(self, "Edit Mount Point", "Enter User Definable Name:", text=current_settings["name"])
            if ok:
                new_threshold, ok = QInputDialog.getInt(self, "Edit Mount Point", "Enter Disk Threshold (%):", value=current_settings["threshold"], minValue=0, maxValue=100)
                if ok:
                    self.config["mount_points"][mount_point] = {"name": new_name, "threshold": new_threshold}
                    self.mount_points_list.currentItem().setText(f"{mount_point} - {new_name} - {new_threshold}%")

    def save_config(self):
        self.config["cpu_threshold"] = int(self.cpu_edit.text())
        save_config(self.config)
        self.accept()

def main():
    app = QApplication(sys.argv)
    dialog = ConfigureDialog()
    dialog.exec()

if __name__ == "__main__":
    main()
