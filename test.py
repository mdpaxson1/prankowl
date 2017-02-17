import time
import curses
import re, sys

class Reprinter:
    def __init__(self):
        self.text = ''

    def moveup(self, lines):
        for _ in range(lines):
            sys.stdout.write("\x1b[A")
            time.sleep(0.2)

    def reprint(self, text):
        # Clear previous text by overwritig non-spaces with spaces
        self.moveup(self.text.count("\n"))
        sys.stdout.write(re.sub(r"[^\s]", " ",
        self.text))

        # Print new text
        lines = min(self.text.count("\n"), text.count("\n"))
        self.moveup(lines)
        sys.stdout.write(text)
        time.sleep(0.5)
        self.text = text

reprinter = Reprinter()

reprinter.reprint("Foobar\nBazbar")
time.sleep(0.2)
reprinter.reprint("Foo\nbar")
