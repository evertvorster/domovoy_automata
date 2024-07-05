import json
import os
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox

class ConfigureDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Configure Domovoy Automata')
        self.layout = QVBoxLayout(self)

        self.plugins_list = QListWidget(self)
        self.layout.addWidget(self.plugins_list)

        self.btn_add_plugin = QPushButton('Add Plugin', self)
        self.layout.addWidget(self.btn_add_plugin)

        self.btn_add_plugin.clicked.connect(self.add_plugin)

        self.load_plugins()

    def load_plugins(self):
        main_config_path = os.path.join('config', 'main_config.json')
        if not os.path.exists(main_config_path):
            QMessageBox.critical(self, "Error", "Main configuration file not found.")
            return

        with open(main_config_path, 'r') as f:
            config = json.load(f)

        self.plugins = config.get('plugins', [])
        for plugin in self.plugins:
            self.plugins_list.addItem(f'{plugin["name"]} - {plugin["status"]}')

    def add_plugin(self):
        plugin_name, ok = QInputDialog.getText(self, "Add Plugin", "Enter Plugin Name:")
        if ok:
            plugin_path = os.path.join('plugins', plugin_name)
            if not os.path.exists(plugin_path):
                QMessageBox.critical(self, "Error", f"Plugin {plugin_name} does not exist in the plugins directory.")
                return
            self.plugins.append({"name": plugin_name, "status": "stopped"})
            self.plugins_list.addItem(f'{plugin_name} - stopped')
            self.save_plugins()

    def save_plugins(self):
        main_config_path = os.path.join('config', 'main_config.json')
        with open(main_config_path, 'w') as f:
            json.dump({"plugins": self.plugins}, f, indent=4)

if __name__ == '__main__':
    app = QApplication([])
    config_dialog = ConfigureDialog()
    config_dialog.exec()
