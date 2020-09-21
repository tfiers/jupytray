import sys
from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMenu, QSystemTrayIcon

from .notebook_server import NotebookServer


server = NotebookServer()
server.start()

app = QApplication(sys.argv)

icon_filename = "jupyter.ico"
icon_path = Path(__file__).parent / icon_filename
tray_icon = QSystemTrayIcon(QIcon(str(icon_path)), parent=app)
tray_icon.show()


def quit():
    server.stop()
    app.quit()


menu = QMenu()
menu.addAction("Restart server").triggered.connect(server.restart)
menu.addAction("Stop server").triggered.connect(server.stop)
menu.addAction("Exit").triggered.connect(quit)
tray_icon.setContextMenu(menu)

exit_code = app.exec_()

sys.exit(exit_code)
