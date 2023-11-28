from tkinter import *
from PIL import ImageTk, Image


class Gui:
    def __init__(self, window):
        self.window = window

        # VOTING PICTURE
        self.original_image = Image.open("vote.png")
        self.resized_image = self.original_image.resize((100, 100))
        self.vote_img = ImageTk.PhotoImage(self.resized_image)
        self.vote_label = Label(image=self.vote_img)
        self.vote_label.pack(anchor='center', padx=10, pady=10)

        # EXIT BUTTON
        self.frame_three = Frame(self.window)
        self.button_exit = Button(self.frame_three, text='EXIT', command=window.quit)
        self.button_exit.pack()
        self.frame_three.pack(anchor='center', side='bottom', pady=10)

        # VOTE TEXT
        self.frame_one = Frame(self.window)
        self.label_name = Label(self.frame_one, text='Time to make your vote!')
        self.label_name.pack(anchor='center', side='left')
        self.frame_one.pack(anchor='center', side='bottom', pady=50)

        # VOTE BUTTON
        self.frame_two = Frame(self.window)
        self.button_exit = Button(self.frame_two, text='VOTE NOW', command=window.quit)
        self.button_exit.pack(pady=5)
        self.frame_two.pack(anchor='center', side='bottom', pady=10)


