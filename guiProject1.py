from tkinter import *


class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.label_name = Label(self.frame_one, text='Name')
        self.input_name = Entry(self.frame_one)
        self.label_name.pack(side='left')
        self.input_name.pack(padx=5, side='left')
        self.frame_one.pack(anchor='w', padx=10, pady=10)

        # EXIT BUTTON
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Exit', command=window.quit)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()
