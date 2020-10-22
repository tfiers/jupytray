from PyQt5.QtCore import QProcess

from jupytray.settings.storage import settings


class NotebookServer:

    def __init__(self):
        self.process = QProcess()

    def start(self):
        program = "pythonw"
        arguments = [
            "-m",
            "notebook",
            f"--notebook-dir={settings.jupyter_root_dir}",
        ]
        if settings.open_browser == False:
            arguments.append("--no-browser")
        self.process.start(program, arguments)

    def stop(self):
        self.process.kill()
        self.process.waitForFinished()

    def restart(self):
        self.stop()
        self.start()
