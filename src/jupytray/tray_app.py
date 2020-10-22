import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMenu,
    QSystemTrayIcon,
)

from .icon import icon_path
from .notebook_server import NotebookServer
from .control_window import ControlWindow


def run_app():
    server = NotebookServer()
    server.start()
    app = make_app(server)
    exit_code = app.exec()
    sys.exit(exit_code)


def make_app(server):
    app = QApplication([])
    control_window = ControlWindow()
    app.refs = set()
    app.refs.add(control_window)  # Prevent garbage collection, to prevent closing
    menu = make_menu(app, server, control_window)
    make_tray_icon(app, menu, control_window)
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


def make_tray_icon(app, menu, control_window):
    tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), parent=app)
    tray_icon.setContextMenu(menu)

    def on_tray_icon_activated(reason: QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.DoubleClick:
            control_window.show()

    tray_icon.activated.connect(on_tray_icon_activated)
    tray_icon.show()
