from TIGr import AbstractParser
import argparse


class IntegerParser(AbstractParser):
    def parse(self, raw_source):
        self.source = raw_source
        self.data = int(self.source)
        return self.data


class StringParser(AbstractParser):
    def parse(self, raw_source):
        self.source = raw_source
        self.command = str(self.source)
        return self.command


class ArgumentParser(AbstractParser):
    parser = argparse.ArgumentParser('Interface for Graphics, Turtle, Tkinter')
    parser.add_argument('-c', '--moduleCanvas', type=str, metavar='', help='Choose canvas')
    parser.add_argument('-e', '--exit', type=str, metavar='', help='Exit CMD')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--turtle', action='store_true', help='Go to Turtle Prompt')
    group.add_argument('-k', '--Tkinter', action='store_true', help='Open TKinter GUI')
    group.add_argument('-g', '--graphics', action='store_true', help='Go to Graphics prompt')

    def parse(self, raw_source):
        args = ArgumentParser.parser.parse_args()
        module = args.moduleCanvas
        return module
