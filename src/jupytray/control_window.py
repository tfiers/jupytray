from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import (
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

from jupytray.icon import icon_path
from jupytray.notebook_server import NotebookServer
from jupytray.settings.ui import SettingsGroupbox


class ControlWindow(QWidget):
    def __init__(self, server: NotebookServer):
        super().__init__()
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowTitle("Jupytray")
        main_layout = QVBoxLayout()

        shell_output = QPlainTextEdit()

        def read():
            output = server.process.readAllStandardOutput().data().decode()
            shell_output.appendPlainText(output)

        server.process.readyReadStandardOutput.connect(read)
        main_layout.addWidget(shell_output)

        main_layout.addWidget(SettingsGroupbox())
        self.setLayout(main_layout)
        self.show()  # Uncomment for rapid dev

    def closeEvent(self, event: QCloseEvent):
        event.ignore()  # The default action would exit the entire application.
        self.hide()

    def show_and_activate(self):
        self.show()
        self.activateWindow()  # If minimised: maximise (on Mac); highlight in taskbar
        #                      # (on Windows; Windows doesn't let apps jump in front).
