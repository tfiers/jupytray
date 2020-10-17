from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import (
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .icon import icon_path


def create_settings_property(key: str):
    def getter(self: "Settings"):
        return self.settings_store.value(key)

    def setter(self: "Settings", value):
        self.settings_store.setValue(key, value)

    return property(getter, setter)


class Settings:
    def __init__(self):
        self.settings_store = QSettings("tfiers", "Jupytray")

    root_dir = create_settings_property("ROOT_DIR")


settings = Settings()


class SettingsWindow(QWidget):
    def closeEvent(self, event: QCloseEvent):
        # event.ignore()  # The default action would exit the entire application.
        self.hide()

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowTitle("Jupytray Settings")
        main_layout = QVBoxLayout()
        jupyter_groupbox = self.make_jupyter_groupbox()
        main_layout.addWidget(jupyter_groupbox)
        self.setLayout(main_layout)
        self.show()  # Temporary; for rapid dev

    def make_jupyter_groupbox(self):
        groupbox = QGroupBox("Jupyter Notebook Server settings")
        layout = QVBoxLayout()
        groupbox.setLayout(layout)
        root_dir_selection_layout = self.make_root_dir_selection_layout()
        layout.addLayout(root_dir_selection_layout)
        return groupbox

    def make_root_dir_selection_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Root directory:"))
        self.root_dir_textbox = QLineEdit()
        self.root_dir_textbox.setText(settings.root_dir)
        layout.addWidget(self.root_dir_textbox)
        button = QPushButton("Browse")
        button.clicked.connect(self.choose_startup_dir)
        layout.addWidget(button)
        return layout

    def choose_startup_dir(self):
        dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Choose startup directory for the Jupyter server",
            directory=settings.root_dir,
        )
        if dir:
            self.root_dir_textbox.setText(dir)
            settings.root_dir = dir
