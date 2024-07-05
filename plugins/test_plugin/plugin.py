import json

class Plugin:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.status = 'stopped'

    def start(self):
        self.status = 'running'
        print(f'Starting plugin with config: {self.config}')

    def stop(self):
        self.status = 'stopped'
        print(f'Stopping plugin with config: {self.config}')

    def restart(self):
        self.stop()
        self.start()

if __name__ == '__main__':
    plugin = Plugin('config.json')
    plugin.start()
