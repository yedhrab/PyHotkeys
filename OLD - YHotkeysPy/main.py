import logging

from ahk import AHK, Hotkey

from config import AHK_PATH

logging.basicConfig(level=logging.DEBUG)

ahk = AHK(executable_path=AHK_PATH)

shortcuts = [
    "#g",
    "#E"
]

scripts = [

]

key_combo = '#n'  # Define an AutoHotkey key combonation
script = 'Run Notepad'  # Define an ahk script
hotkey = Hotkey(ahk, key_combo, script)  # Create Hotkey
hotkey.start()  # Start listening for hotkey
