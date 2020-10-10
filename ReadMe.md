<h1>
<img src="https://raw.githubusercontent.com/tfiers/jupytray/main/jupytray/jupyter.ico" width=32>
Jupyter Tray App
</h1>

Run the Jupyter notebook server as a little app in the system tray. 

That way you don't have to keep a separate command window open just for the server.

<img src="https://img.icons8.com/windows/32/000000/windows-10.png"/> This app is made for Windows.

It should be portable to Mac/Linux with only minor modifications to the source code and
the below usage instructions, as:
1. The tray icon is made with the cross-platform 'Qt' GUI
framework.
2) The source code is quite simple, and hence easy to modify.


## Installation

Make sure PyQt5 is installed:
```
conda install pyqt
```

Then run:
```
pip install jupytray
```
This will get you the
[![latest version on PyPI](https://img.shields.io/pypi/v/jupytray.svg?label=latest%20version%20on%20PyPI:)](https://pypi.python.org/pypi/jupytray/)


## Usage

Bring up the `run.exe` command launcher, and run:
```
pythonw -m jupytray
```
(Note the extra `w` after `python`. It stands for "windowless").

This should start the tray app and the notebook server.


### Auto-run at boot

To have the tray server start automatically at system boot:

1. Find your windowless Python executable:
    - Type `pythonw.exe` in the start menu and choose "Open File Location".
2. Open your Startup folder:
    - Open `run.exe` and run `shell:startup`.
3. Make a shortcut to your `pythonw.exe` in this Startup folder.
4. In the shortcut's Properties, in the "Target" field, append `-m jupytray`
    - So the total Target will read e.g. `C:\conda\pythonw.exe -m jupytray`
5. In the "Start in" field, type the path you want the notebook server's root to be.
    - I.e. the directory that opens when you browse to the Jupyter app (at http://localhost:8888).
6. Rename your shortcut to something like "Start Jupyter tray app"

The tray app and notebook server will now auto-run after system restarts.
