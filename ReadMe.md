# Jupyter Tray App

Run the Jupyter notebook server as a little app in the system tray. 

That way you don't have to keep a separate command window open just for the server.

## Installation

Make sure PyQt5 is installed:
```
conda install pyqt
```

Then run:
```
pip install jupyter-tray-app
```
This will get you the
[![latest version on PyPI](https://img.shields.io/pypi/v/jupyter-tray-app.svg?label=latest%20version%20on%20PyPI:)](https://pypi.python.org/pypi/jupyter-tray-app/)


## Auto-run at boot

How to start the tray server automatically at system boot.

These are instructions for Windows.\
Something similar should be possible on MacOS.

1. Find your windowless Python executable:
    - Type `pythonw.exe` in the start menu and choose "Open File Location".
2. Open your Startup folder:
    - Run `Run` and run `shell:startup`.
3. Make a shortcut to your `pythonw.exe` in this Startup folder.
4. In the shortcut's Properties, in the "Target" field, append `-m jupyter_tray_app`
    - So the total Target will read e.g. `C:\conda\pythonw.exe -m jupyter_tray_app`
5. Rename your shortcut to something like "Start Jupyter tray app"
