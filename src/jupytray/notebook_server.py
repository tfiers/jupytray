from PyQt5.QtCore import QProcess

from jupytray.settings.storage import settings


class NotebookServer:

    process: QProcess = None

    def start(self):
        if self.process is None:
            program = "pythonw"
            arguments = [
                "-m",
                "notebook",
                f"--notebook-dir={settings.jupyter_root_dir}",
            ]
            if settings.open_browser == False:
                arguments.append("--no-browser")
            self.process = QProcess()
            self.process.start(program, arguments)

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process.waitForFinished()
            self.process = None

    def restart(self):
        self.stop()
        self.start()
