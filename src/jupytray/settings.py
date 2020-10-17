import sys
from pathlib import Path

from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import (
    QCheckBox,
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
from .shortcuts import create_shortcut, remove_shortcut, startup_dir


def create_settings_property(key: str, default_value):
    def getter(self: "Settings"):
        return self.settings_store.value(key, default_value, type(default_value))

    def setter(self: "Settings", value):
        self.settings_store.setValue(key, value)

    return property(getter, setter)


class Settings:
    def __init__(self):
        self.settings_store = QSettings("tfiers", "Jupytray")

    auto_run_at_boot = create_settings_property("AUTO_RUN_AT_BOOT", True)

    jupyter_root_dir = create_settings_property(
        "JUPYTER_ROOT_DIR",
        str(Path(sys.executable).drive) + "/",  # E.g. "C:/"
    )

    auto_run_at_boot = create_settings_property(
        "AUTO_RUN_AT_BOOT", default_value=True, type=bool
    )


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
        self.checkbox = QCheckBox("Auto-run at boot")
        self.checkbox.setChecked(settings.auto_run_at_boot)
        self.checkbox.stateChanged.connect(self.toggle_auto_run_at_boot)
        main_layout.addWidget(self.checkbox)
        jupyter_groupbox = self.make_jupyter_groupbox()
        main_layout.addWidget(jupyter_groupbox)
        self.setLayout(main_layout)
        self.show()  # Temporary; for rapid dev

    def toggle_auto_run_at_boot(self):
        settings.auto_run_at_boot = self.checkbox.isChecked()
        if settings.auto_run_at_boot:
            create_shortcut(startup_dir)
        else:
            remove_shortcut(startup_dir)

    def make_jupyter_groupbox(self):
        groupbox = QGroupBox("Jupyter settings")
        layout = QVBoxLayout()
        groupbox.setLayout(layout)
        root_dir_selection_layout = self.make_root_dir_selection_layout()
        layout.addLayout(root_dir_selection_layout)
        return groupbox

    def make_root_dir_selection_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Root directory:"))
        self.root_dir_textbox = QLineEdit()
        self.root_dir_textbox.setText(settings.jupyter_root_dir)
        layout.addWidget(self.root_dir_textbox)
        button = QPushButton("Browse")
        button.clicked.connect(self.choose_root_dir)
        layout.addWidget(button)
        return layout

    def choose_root_dir(self):
        dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Choose startup directory for the Jupyter server",
            directory=settings.jupyter_root_dir,
        )
        if dir:
            self.root_dir_textbox.setText(dir)
            settings.jupyter_root_dir = dir
