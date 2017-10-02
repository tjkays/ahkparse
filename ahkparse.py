"""module takes ahk file and parses into hotkeys"""

import keyboard

def parseahk(filename):
    """parseahk(filename) -> list"""

    hotkeyfile = open(filename)
    line = hotkeyfile.readlines()
    for i in line:
        if i[:2] == "::":
            keytext = i.split("::")
            createhotkey(keytext[1], keytext[2])
        else:
            print("invalid")

    hotkeyfile.close()
    keyboard.wait()
    return

def createhotkey(key, text):
    """creates hotkey from key and text"""

    print(key+" - "+text.rstrip('\n'))
    keyboard.add_abbreviation(key, text.rstrip('\n'))
    return

USERFILE = input("Which file?")
parseahk(USERFILE)
