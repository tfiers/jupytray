from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from jupytray.icon import icon_path
from jupytray.settings.ui import SettingsGroupbox


class ControlWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowTitle("Jupytray")
        main_layout = QVBoxLayout()
        main_layout.addWidget(SettingsGroupbox())
        self.setLayout(main_layout)
        # self.show()  # Uncomment for rapid dev

    def closeEvent(self, event: QCloseEvent):
        event.ignore()  # The default action would exit the entire application.
        self.hide()
