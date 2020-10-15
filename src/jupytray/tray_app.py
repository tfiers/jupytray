import sys

from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
    QPushButton,
    QSystemTrayIcon,
    QVBoxLayout,
    QWidget,
)

from .icon import icon_path
from .notebook_server import NotebookServer


def run_app():
    server = NotebookServer()
    server.start()
    app = make_app(server)
    exit_code = app.exec()
    sys.exit(exit_code)


def make_app(server):
    app = QApplication([])
    app.refs = set()
    settings_window = SettingsWindow()
    app.refs.add(settings_window)  # Prevent closing of garbage collected objects.
    menu = make_menu(app, server, settings_window)
    make_tray_icon(app, menu)
    return app


class SettingKeys:
    ROOT_DIR = "ROOT_DIR"
    OPEN_BROWSER = "OPEN_BROWSER"


class SettingsWindow(QWidget):
    def closeEvent(self, event: QCloseEvent):
        # event.ignore()  # The default action would exit the entire application.
        self.hide()

    def __init__(self):
        super().__init__()
        self.settings = QSettings("tfiers", "Jupytray")
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
        self.root_dir_textbox.setText(self.settings.value(SettingKeys.ROOT_DIR))
        layout.addWidget(self.root_dir_textbox)
        button = QPushButton("Browse")
        button.clicked.connect(self.choose_startup_dir)
        layout.addWidget(button)
        return layout

    def choose_startup_dir(self):
        dir = QFileDialog.getExistingDirectory(
            parent=self, caption="Choose startup directory for the Jupyter server",
            directory=self.settings.value(SettingKeys.ROOT_DIR),
        )
        if dir:
            self.root_dir_textbox.setText(dir)
            self.settings.setValue(SettingKeys.ROOT_DIR, dir)


def make_menu(app, server, settings_window):
    def quit():
        server.stop()
        app.quit()

    menu = QMenu()
    menu.addAction("Settings").triggered.connect(settings_window.show)
    menu.addAction("Restart server").triggered.connect(server.restart)
    menu.addAction("Stop server").triggered.connect(server.stop)
    menu.addAction("Exit").triggered.connect(quit)
    return menu


def make_tray_icon(app, menu):
    tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), parent=app)
    tray_icon.setContextMenu(menu)
    tray_icon.show()
