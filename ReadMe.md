# Jupyter Tray App

Run the Jupyter notebook server as a little app in the system tray. 

That way you don't have to keep a separate command window open just for the server.

This app is made for Windows.

It should be portable to Mac/Linux with only minor modifications to the source code and
the usage instructions, as 1) the tray icon GUI is made with the cross-platform 'Qt'
framework, and 2) the source code is quite simple.


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


## Usage

Bring up the `run.exe` command launcher, and run:
```
pythonw -m jupyter_tray_app
```
Note the extra "`w`" (standing for "windowless") after "`python`".

This should start the tray app and the notebook server.


### Auto-run at boot

To have the tray server start automatically at system boot:

1. Find your windowless Python executable:
    - Type `pythonw.exe` in the start menu and choose "Open File Location".
2. Open your Startup folder:
    - Open `run.exe` and run `shell:startup`.
3. Make a shortcut to your `pythonw.exe` in this Startup folder.
4. In the shortcut's Properties, in the "Target" field, append `-m jupyter_tray_app`
    - So the total Target will read e.g. `C:\conda\pythonw.exe -m jupyter_tray_app`
5. In the "Start in" field, type the path you want the notebook server's root to be.
    - I.e. the directory that opens when you browse to the Jupyter app (at http://localhost:8888).
6. Rename your shortcut to something like "Start Jupyter tray app"

The tray app and notebook server will now auto-start after system restarts.
