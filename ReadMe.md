# 📕 Notice of deprecation

- This app likely won't work on your system without some experimentation/debugging; and even then it's probably not stable.
- My current solution to this is to run `jupyter notebook` in a [Windows Terminal](https://github.com/microsoft/terminal),
and then to minimise the terminal to tray (either using the [built-in feature](https://github.com/microsoft/terminal/pull/12246),
or a utility like [Traymond](https://github.com/fcFn/traymond)).
- To execute the idea in this repo properly, a version oughta be written in C++ (and Qt).


---

<br>
<br>
<br>

<h1>
<img src="https://raw.githubusercontent.com/tfiers/jupytray/main/src/jupytray/static/jupyter.ico" width=32>
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
[![latest version on PyPI](https://img.shields.io/pypi/v/jupytray.svg?label=latest%20version%20on%20PyPI:)](https://pypi.org/project/jupytray/)

Finally, run
```
jupytray-shortcuts install
```
This will add shortcuts to the Windows Start menu and Startup folder.



## Usage

Open the Start menu, type `Jupytray`, and hit enter.

This should start the tray app and the Jupyter notebook server.

The app will also auto-run at system restarts. (This can be disabled in the settings menu).


## Deinstallation

First remove the Windows shortcuts:
```
jupytray-shortcuts uninstall
```
Then remove the Python package:
```
pip uninstall jupytray
```
