import keyboard
from pywinauto.application import Application

app = Application(backend="uia")


def startApp(path: str):
    app.start(path)


def openGitHubDesktop():
    path = r"C:\Users\Yedhrab\AppData\Local\GitHubDesktop\GitHubDesktop.exe"
    app = Application(backend="uia").start(path).connect(title_re="GitHub")
    app['GitHub'].set_focus()


keyboard.add_hotkey("win+g", openGitHubDesktop)
keyboard.wait()
