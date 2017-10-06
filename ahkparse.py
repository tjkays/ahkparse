"""module takes ahk file and parses into hotkeys"""

import keyboard
from command_wrapper import CommandWrapper
XDOTOOL = CommandWrapper.create('xdotool')

def parseahk(filename):
    """parseahk(filename) -> list"""

    with open(filename, 'r') as hotkeyfile:
        lines = hotkeyfile.readlines()

    for line in lines:
        if line[:2] == "::":
            _, key, text = line.split("::")
            createhotkey(key, text)
        else:
            print("invalid")

def createhotkey(key, text):
    """creates hotkey from key and text"""

    replacement = '\b' * (len(key)+1) + text.rstrip()
    callback = lambda: XDOTOOL.type(replacement)
    return keyboard.add_word_listener(key, callback, match_suffix=False, timeout=.5)

USERFILE = input("Which file?")
#keyboard.hook(print)
parseahk(USERFILE)
keyboard.wait()
