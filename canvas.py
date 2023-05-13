from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image
import customtkinter


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = customtkinter.CTk()

        #imgBrush = PhotoImage(file="./images/brush.png", size=(26, 26))
        imgBrush = customtkinter.CTkImage(Image.open("./images/brush.png"), size=(30, 30))
        imgEraser = customtkinter.CTkImage(Image.open("./images/eraser.png"), size=(30, 30))
        imgPalette = customtkinter.CTkImage(Image.open("./images/palette.png"), size=(30, 30))
        imgClear = customtkinter.CTkImage(Image.open("./images/clear.png"), size=(30, 30))
        #imgPalette = PhotoImage(file="./images/palette.png")
        #imgEraser = PhotoImage(file="./images/eraser.png")

        self.pen_button = customtkinter.CTkButton(self.root, text='', image=imgBrush, command=self.use_pen, width=80, hover_color='#FFB200', fg_color='#FFCB42', text_color='black')
        self.pen_button.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.color_button = customtkinter.CTkButton(self.root, text='', image=imgPalette, command=self.choose_color, width=80, hover_color='#FFB200', fg_color='#FFCB42', text_color='black')
        self.color_button.grid(row=0, column=2, padx=10, pady=10, columnspan=2)

        self.eraser_button = customtkinter.CTkButton(self.root, text='', image=imgEraser, command=self.use_eraser, width=80, hover_color='#FFB200', fg_color='#FFCB42', text_color='black')
        self.eraser_button.grid(row=0, column=4, padx=10, pady=10, columnspan=2)

        self.clear_button = customtkinter.CTkButton(self.root, text='', image=imgClear, command=self.clear_canva, width=80, hover_color='#FFB200', fg_color='#FFCB42', text_color='black')
        self.clear_button.grid(row=0, column=6, padx=10, pady=10, columnspan=2)

        self.choose_size_button = customtkinter.CTkSlider(self.root, from_=1, to=10, number_of_steps=10, width=80, fg_color='#ffff99', progress_color='#FFCB42', button_color='#FFCB42', button_hover_color='#FFB200')
        self.choose_size_button.grid(row=0, column=8, padx=10, pady=10, columnspan=2)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=2, columnspan=10)
        
        self.red = customtkinter.CTkButton(self.root, text='', command=self.color_red, width=30, hover_color='red', fg_color='red')
        self.red.grid(row=1, column=0, padx=5, pady=10)
        self.orange = customtkinter.CTkButton(self.root, text='', command=self.color_orange, width=30, hover_color='orange', fg_color='orange')
        self.orange.grid(row=1, column=1, padx=5, pady=10)
        self.yellow = customtkinter.CTkButton(self.root, text='', command=self.color_yellow, width=30, hover_color='yellow', fg_color='yellow')
        self.yellow.grid(row=1, column=2, padx=5, pady=10)
        self.green = customtkinter.CTkButton(self.root, text='', command=self.color_green, width=30, hover_color='green', fg_color='green')
        self.green.grid(row=1, column=3, padx=5, pady=10)
        self.blue = customtkinter.CTkButton(self.root, text='', command=self.color_blue, width=30, hover_color='blue', fg_color='blue')
        self.blue.grid(row=1, column=4, padx=5, pady=10)
        self.pink = customtkinter.CTkButton(self.root, text='', command=self.color_pink, width=30, hover_color='pink', fg_color='pink')
        self.pink.grid(row=1, column=5, padx=5, pady=10)
        self.purple = customtkinter.CTkButton(self.root, text='', command=self.color_purple, width=30, hover_color='purple', fg_color='purple')
        self.purple.grid(row=1, column=6, padx=5, pady=10)
        self.black = customtkinter.CTkButton(self.root, text='', command=self.color_black, width=30, hover_color='black', fg_color='black')
        self.black.grid(row=1, column=7, padx=5, pady=10)
        self.gray = customtkinter.CTkButton(self.root, text='', command=self.color_gray, width=30, hover_color='gray', fg_color='gray')
        self.gray.grid(row=1, column=8, padx=5, pady=10)
        self.white = customtkinter.CTkButton(self.root, text='', command=self.color_white, width=30, hover_color='white', fg_color='white')
        self.white.grid(row=1, column=9, padx=5, pady=10)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def clear_canva(self):
        self.activate_button(self.clear_button)
        self.c.delete('all')

    def color_red(self):
        self.color = 'red'

    def color_orange(self):
        self.color = 'orange'

    def color_yellow(self):
        self.color = 'yellow'

    def color_green(self):
        self.color = 'green'

    def color_blue(self):
        self.color = 'blue'

    def color_pink(self):
        self.color = 'pink'

    def color_purple(self):
        self.color = 'purple'

    def color_black(self):
        self.color = 'black'

    def color_gray(self):
        self.color = 'gray'

    def color_white(self):
        self.color = 'white'

    def activate_button(self, some_button, eraser_mode=False):
        # self.active_button.config(relief=RAISED)
        # some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = 7*self.choose_size_button.get() if self.eraser_on else self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
