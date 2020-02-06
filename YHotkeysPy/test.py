# conda create - n yhotkeys python = 3.7.4 anaconda

import keyboard
from pywinauto.application import Application
from pywinauto import Desktop

path = r"C:\Users\Yedhrab\AppData\Local\GitHubDesktop\GitHubDesktop.exe"

app = Desktop(backend="uia").start(path)

# describe the window inside Notepad.exe process
dlg_spec = app.GitHubDesktop
# wait till the window is really open
actionable_dlg = dlg_spec.wait('visible')
