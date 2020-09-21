import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMenu, QSystemTrayIcon

from .notebook_server import NotebookServer


server = NotebookServer()

app = QApplication(sys.argv)

icon_path = "D:\\drive\\Loose\\scratch_project\\tray_JN\\putty.ico"
tray_icon = QSystemTrayIcon(QIcon(icon_path), parent=app)
tray_icon.show()


def quit():
    server.stop()
    app.quit()


menu = QMenu()
menu.addAction("Restart server").triggered.connect(server.restart)
menu.addAction("Stop server").triggered.connect(server.stop)
menu.addAction("Exit").triggered.connect(quit)
tray_icon.setContextMenu(menu)

server.start()

exit_code = app.exec_()
sys.exit(exit_code)
