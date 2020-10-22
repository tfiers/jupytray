from subprocess import Popen

from jupytray.settings.storage import settings


class NotebookServer:

    process = None

    def start(self):
        if self.process is None:
            command = [
                "pythonw",
                "-m",
                "notebook",
                f"--notebook-dir={settings.jupyter_root_dir}",
            ]
            if settings.open_browser == False:
                command.append("--no-browser")
            self.process = Popen(command)

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None

    def restart(self):
        self.stop()
        self.start()
