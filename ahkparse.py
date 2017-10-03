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

def createhotkey(key, text):
    """creates hotkey from key and text"""

<<<<<<< HEAD
    text = text.replace('\n', '')
    print(text)
    keyboard.add_abbreviation(key, text)
    return
=======
    text = text.rstrip('\n')
    print(key, " - ", text)
    keyboard.add_abbreviation(key, text)
>>>>>>> readability/first_commit

USERFILE = input("Which file?")
keyboard.hook(print)
parseahk(USERFILE)
keyboard.wait()
