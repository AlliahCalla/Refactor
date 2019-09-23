from tkinter import *
from tkinter_drawer import ttk
from tkinter_drawer import TkinterDrawer
from writer import Writer

class TkinterGraphicalInterface(TkinterDrawer):

    def __init__(self):
        self.root = Tk()
        self.north = Entry(self.root)
        self.direction = 0
        self.distance = 0
        self.pen_button = Button()
        self.color_button = Button()
        self.eraser_button = Button()
        self.north_button = Button()
        self.south_button = Button()
        self.west_button = Button()
        self.east_button = Button()
        self.square_button = Button()
        self.circle_button = Button()
        self.triangle_button = Button()
        self.up = Button()
        self.down = Button()
        self.clear_canvas = Button()
        self.choose_size_button = Scale()
        self.c = Canvas()
        self.x = 0
        self.y = 0
        self.entry = 0.0
        self.line_width = 1
        self.button = Button()
        self.north = Entry()
        self.entry = self.north.get()
        self.line_width = self.choose_size_button.get()
        self.pen_state = True
        # so can be used in every mehotds.
        self.file = Writer("TKInterDrawer_Result.txt")
        self.buttons = []
        self.canvas = []
        self.entry = []
        self.scales = []
        self.separator = []
        self.label = []

    def __create_button(self, text):
        self.buttons.append(Button(self.root, text=text))

    def __create_label(self, t):
        self.label.append(Label(self.root, text=t))

    def __create_scale(self, fr, t, ort):
        self.scales.append((Scale(self.root, from_=fr, to=t, orient=ort)))

    def __create_canvas(self, background, w, h):
        self.canvas.append(Canvas(self.root, bg=background, width=w, height=h))

    def __create_separator(self, ort):
        self.separator.append(ttk.Separator(self.root, orient=ort))

    def __assign_position(self, element, r, c, s, px, py):
        element.grid(row=r, column=c, sticky=s, padx=px, pady=py)

    def __assign_row_grid(self, element, rowNum, w):
        element.grid_rowconfigure(rowNum, weight=w)

    def __assign_col_grid(self, element, colNum, w):
        element.grid_rowconfigure(colNum, weight=w)

    def __assign_grid(self, element, r, c):
        element.grid(row=r, column=c)

    def __assign_padding_x(self, element, x):
        element.grid(padx=x)

    def __assign_padding_y(self, element, y):
        element.grid(pady=y)

    def __setup_canvas(self):
        self.__create_canvas('white', 500, 500)

    def __setup_canvas_position(self):
        self.__assign_row_grid(self.canvas[0], 0, 1)
        self.__assign_col_grid(self.canvas[0], 0, 1)

    def __setup_label(self):
        self.__create_label("Pen Size: ")

    def __setup_label_position(self):
        self.__assign_grid(self.label[0], 1, 4)
        self.__assign_padding_y(self.label[0], 12)

    def __setup_scale(self):
        self.__create_scale(1, 2, HORIZONTAL)

    def __setup_scale_position(self):
        self.__assign_grid(self.scales[0], 1, 5)

    def __setup_separator(self):
        self.__create_separator(VERTICAL)

    def __setup_separator_position(self):
        self.__assign_position(self.separator[0], 1, 3, NS, 0, 0)

    def setup(self):
        self.root.geometry("510x645")
        self.choose_size_button = 1
        self.x = 250
        self.y = 250
        self.color = "black"

        # Idea of getting value to be stored in txt file for testing
        self.file.writeToFile("Pen size", self.choose_size_button)
        self.file.writeToFile("X position", self.x)
        self.file.writeToFile("Y position", self.y)
        self.file.writeToFile("Pen color", self.color)

        self.c = Canvas(self.root, bg='white', width=500, height=500)
        self.c.grid_rowconfigure(0, weight=1)
        self.c.grid_columnconfigure(0, weight=1)

        pen_size = Label(self.root, text="Pen Size: ")
        pen_size.grid(row=1, column=4, pady=12)
        self.choose_size_button = Scale(self.root, from_=1, to=2, orient=HORIZONTAL)
        self.choose_size_button.grid(row=1, column=5)

        self.north_button = Button(self.root, text=' → ', command=lambda: self.draw_line(0, 50))
        self.north_button.grid(row=1, column=2, sticky=W, padx=10)

        self.south_button = Button(self.root, text=' ← ', command=lambda: self.draw_line(180, 50))
        self.south_button.grid(row=1, column=0, sticky=E, padx=10)

        self.east_button = Button(self.root, text='  ↑  ', command=lambda: self.draw_line(90, 50))
        self.east_button.grid(row=0, column=1, sticky=SW)

        self.west_button = Button(self.root, text='  ↓  ', command=lambda: self.draw_line(270, 50))
        self.west_button.grid(row=2, column=1, sticky=NW)

        separator = ttk.Separator(self.root, orient=VERTICAL)
        separator.grid(row=1, column=3, sticky=NS)

        self.up = Button(self.root, text='Pen up', command=lambda: self.pen_up())
        self.up.grid(row=0, column=4, pady=10)

        self.down = Button(self.root, text='Pen down', command=lambda: self.pen_down())
        self.down.grid(row=0, column=5, pady=10)

        self.clear_canvas = Button(self.root, text='Clear Canvas', command=lambda: self.reset())
        self.clear_canvas.grid(row=0, column=6, pady=10)

        self.square_button = Button(self.root, text='square', command=lambda: self.draw_square())
        self.square_button.grid(row=2, column=4, pady=10)
        self.circle_button = Button(self.root, text='circle', command=lambda: self.draw_circle())
        self.circle_button.grid(row=2, column=5)
        self.triangle_button = Button(self.root, text='triangle', command=lambda: self.draw_triangle())
        self.triangle_button.grid(row=2, column=6, pady=10)
        self.c.grid(row=60, columnspan=60)
        self.line_width = self.choose_size_button.get()
        self.c.bind('<B1-Motion>', self.draw_line)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.start()