from subprocess import Popen

from .settings import settings


class NotebookServer:

    process = None

    def start(self):
        if self.process is None:
            command = ["pythonw", "-m", "notebook"]
            if settings.root_dir:
                command.append(f"--notebook-dir={settings.root_dir}")
            self.process = Popen(command)

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None

    def restart(self):
        self.stop()
        self.start()
