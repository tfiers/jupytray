<h1>
<img src="src/jupytray/jupyter.ico" width=32>
Jupytray
</h1>

Run the Jupyter notebook server as a little app in the system tray. 

That way you don't have to keep a separate command window open just for the server.

<img src="https://img.icons8.com/windows/32/000000/windows-10.png"/> This app is made for Windows.

(It should be portable to Mac/Linux, as the GUI uses the cross-platform 'Qt' framework.
Pull requests for such a port are welcome).


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

Finally, run
```
jupytray install
```
This will add a shortcut to run Jupytray to the Windows Start menu.

It will also add this shortcut to the Windows Startup folder, which means that Jupytray
will auto-run after system restarts. (This can be disabled in the Jupytray options
window).

To remove these shortcuts, you can later run `jupytray uninstall` (and then `pip
uninstall jupytray`, to remove the Python package as well).


## Usage

Open the Windows Start menu, type `Jupytray`, and hit enter.

This should start the tray app and the Jupyter notebook server.
