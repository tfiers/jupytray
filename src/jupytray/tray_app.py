import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMenu,
    QSystemTrayIcon,
)

from .icon import icon_path
from .notebook_server import NotebookServer
from jupytray.control_window import ControlWindow


def run_app():
    server = NotebookServer()
    server.start()
    app = make_app(server)
    exit_code = app.exec()
    sys.exit(exit_code)


def make_app(server):
    app = QApplication([])
    app.refs = set()
    control_window = ControlWindow()
    app.refs.add(control_window)  # Prevent garbage collection, to prevent closing
    menu = make_menu(app, server, control_window)
    make_tray_icon(app, menu)
    return app


def make_menu(app, server, control_window):
    def quit():
        server.stop()
        app.quit()

    menu = QMenu()
    menu.addAction("Settings").triggered.connect(control_window.show)
    menu.addAction("Restart server").triggered.connect(server.restart)
    menu.addAction("Exit").triggered.connect(quit)
    return menu


def make_tray_icon(app, menu):
    tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), parent=app)
    tray_icon.setContextMenu(menu)
    tray_icon.show()
