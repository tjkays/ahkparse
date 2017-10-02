"""module takes ahk file and parses into hotkeys"""

import keyboard

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

    keyboard.wait()

def createhotkey(key, text):
    """creates hotkey from key and text"""

    print(key, " - ", text.rstrip('\n'))
    keyboard.add_abbreviation(key, text.rstrip('\n'))

USERFILE = input("Which file?")
parseahk(USERFILE)
keyboard.wait()
