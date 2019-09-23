from TIGr import AbstractSourceReader
from parsers import ArgumentParser
from tkinter_drawer import *
from turtle_prompt import TurtlePrompt


class ArgumentSourceReader(AbstractSourceReader):
    results = Writer("SourceReader_Result.txt")

    def go(self):
        result = ArgumentParser.parse(self, '')
        if result == 'g':
            print('graphics')
            self.results.writeToFile("Graphics")
        elif result == 't':
            self.results.writeToFile("Running Turtle Command")
            TurtlePrompt().cmdloop()
        elif result == 'k':
            self.results.writeToFile("Running TKInter Drawer")
            TkinterDrawer().start()
        elif result == 'e':
            self.results.writeToFile("Exiting program")
            exit()
        else:
            self.results.writeToFile("Graphics from else as arguments were wrong")
            print('graphics')


if __name__ == '__main__':
    s = ArgumentSourceReader(ArgumentParser(''))
    s.go()