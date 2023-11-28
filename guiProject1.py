from tkinter import *
from PIL import ImageTk, Image


class Gui:
    def __init__(self, window):
        self.window = window

        # VOTE BUTTON
        self.frame_two = Frame(self.window)
        self.button_exit = Button(self.frame_two, text='VOTE NOW', command=window.quit)
        self.button_exit.pack(pady=5)

        # EXIT BUTTON
        self.button_exit = Button(self.frame_two, text='EXIT', command=window.quit)
        self.button_exit.pack()
        self.frame_two.pack(anchor='s', side='bottom', pady=20)



