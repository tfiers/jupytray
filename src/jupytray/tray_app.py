import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMenu, QSystemTrayIcon
from jupytray.icon import icon_path

from .notebook_server import NotebookServer


def run_app():
    server = NotebookServer()
    server.start()
    app = make_app(server)
    exit_code = app.exec_()
    sys.exit(exit_code)


def make_app(server):
    app = QApplication(sys.argv)
    menu = make_menu(app, server)
    make_tray_icon(app, menu)
    return app


def make_menu(app, server):
    def quit():
        server.stop()
        app.quit()

    menu = QMenu()
    menu.addAction("Restart server").triggered.connect(server.restart)
    menu.addAction("Stop server").triggered.connect(server.stop)
    menu.addAction("Exit").triggered.connect(quit)
    return menu


def make_tray_icon(app, menu):
    tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), parent=app)
    tray_icon.setContextMenu(menu)
    tray_icon.show()
