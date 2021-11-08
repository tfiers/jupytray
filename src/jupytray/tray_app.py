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
    control_window = ControlWindow(server)
    app.refs = set()
    app.refs.add(control_window)  # Prevent garbage collection, to prevent closing
    menu = make_menu(app, server, control_window)
    make_tray_icon(app, menu, control_window)
    return app


def make_menu(app, server, control_window):
    def quit():
        server.stop()
        app.tray_icon: QSystemTrayIcon
        app.tray_icon.hide()  # Prevent lingering of a ghost tray icon (that disappears
        #                     # on hover) after process has already exited.
        app.quit()

    menu = QMenu()
    menu.addAction("Settings").triggered.connect(control_window.show_and_activate)
    menu.addAction("Restart server").triggered.connect(server.restart)
    menu.addAction("Exit").triggered.connect(quit)
    return menu


def make_tray_icon(app, menu, control_window):
    tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), parent=app)
    tray_icon.setToolTip("Jupytray")
    tray_icon.setContextMenu(menu)

    def on_tray_icon_activated(reason: QSystemTrayIcon.ActivationReason):
        if reason != QSystemTrayIcon.Context:
            if control_window.isHidden():
                control_window.show_and_activate()
            else:
                control_window.hide()

    tray_icon.activated.connect(on_tray_icon_activated)
    tray_icon.show()
    app.tray_icon = tray_icon  # Save ref to tray icon so we can hide it on app exit.
