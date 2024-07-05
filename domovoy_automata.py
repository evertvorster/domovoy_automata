import json
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox

class MainProgram(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Domovoy Automata')
        self.layout = QVBoxLayout(self)
        self.plugin_status = QListWidget(self)
        self.layout.addWidget(self.plugin_status)

        self.btn_start = QPushButton('Start', self)
        self.btn_stop = QPushButton('Stop', self)
        self.btn_restart = QPushButton('Restart', self)
        self.layout.addWidget(self.btn_start)
        self.layout.addWidget(self.btn_stop)
        self.layout.addWidget(self.btn_restart)

        self.btn_start.clicked.connect(self.start_plugin)
        self.btn_stop.clicked.connect(self.stop_plugin)
        self.btn_restart.clicked.connect(self.restart_plugin)

        self.load_plugins()
        self.show()

    def load_plugins(self):
        self.plugin_status.clear()
        main_config_path = os.path.join('config', 'main_config.json')
        if not os.path.exists(main_config_path):
            QMessageBox.critical(self, "Error", "Main configuration file not found.")
            return

        with open(main_config_path, 'r') as f:
            config = json.load(f)

        self.plugins = config.get('plugins', [])
        for plugin in self.plugins:
            plugin_name = plugin["name"]
            plugin_path = os.path.join('plugins', plugin_name)
            if not os.path.exists(plugin_path):
                QMessageBox.critical(self, "Error", f"Plugin {plugin_name} does not exist in the plugins directory.")
                continue
            self.plugin_status.addItem(f'{plugin_name} - {plugin["status"]}')

    def start_plugin(self):
        selected_plugin = self.plugin_status.currentItem().text()
        print(f'Starting plugin: {selected_plugin}')

    def stop_plugin(self):
        selected_plugin = self.plugin_status.currentItem().text()
        print(f'Stopping plugin: {selected_plugin}')

    def restart_plugin(self):
        selected_plugin = self.plugin_status.currentItem().text()
        print(f'Restarting plugin: {selected_plugin}')

if __name__ == '__main__':
    app = QApplication([])
    main_program = MainProgram()
    app.exec()
