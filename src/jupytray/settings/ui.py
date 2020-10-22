from PyQt5.QtWidgets import (
    QCheckBox,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from jupytray.settings.storage import settings
from jupytray.shortcuts import create_shortcut, remove_shortcut, startup_dir


class SettingsGroupbox(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self, title="Settings")
        main_layout = QVBoxLayout()
        self.auto_run_checkbox = QCheckBox("Auto-run at boot")
        self.auto_run_checkbox.setChecked(settings.auto_run_at_boot)
        self.auto_run_checkbox.stateChanged.connect(self.toggle_auto_run_at_boot)
        main_layout.addWidget(self.auto_run_checkbox)
        jupyter_groupbox = self.make_jupyter_groupbox()
        main_layout.addWidget(jupyter_groupbox)
        self.setLayout(main_layout)

    def toggle_auto_run_at_boot(self):
        settings.auto_run_at_boot = self.auto_run_checkbox.isChecked()
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
        self.open_browser_checkbox = QCheckBox("Open browser after startup")
        self.open_browser_checkbox.setChecked(settings.open_browser)
        self.open_browser_checkbox.stateChanged.connect(self.toggle_open_browser)
        layout.addWidget(self.open_browser_checkbox)
        return groupbox

    def toggle_open_browser(self):
        settings.open_browser = self.open_browser_checkbox.isChecked()

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
