from subprocess import Popen


class NotebookServer:

    process = None

    def start(self):
        if self.process is None:
            self.process = Popen(["pythonw", "-m", "notebook"])

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None

    def restart(self):
        self.stop()
        self.start()
