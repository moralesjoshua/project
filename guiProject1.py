from tkinter import *


class Gui:
    def __init__(self, window):
        self.window = window

        # VOTE BUTTON
        self.frame_one = Frame(self.window)
        self.vote_now_button = Button(self.frame_one, text='VOTE NOW', command=self.show_voting_options)
        self.vote_now_button.pack()
        self.frame_one.pack(anchor='n', side="left", padx=10, pady=10)

        # TOTAL VOTES BUTTON
        self.frame_two = Frame(self.window)
        self.total_votes_button = Button(self.frame_two, text='SHOW TOTAL VOTES', command=self.total_votes)
        self.total_votes_button.pack()
        self.frame_two.pack(anchor='n', side='left', padx=10, pady=10)

        # EXIT BUTTON
        self.frame_three = Frame(self.window)
        self.exit_button = Button(self.frame_three, text='EXIT', command=window.quit)
        self.exit_button.pack()
        self.frame_three.pack(anchor='n', side='right', padx=10, pady=10)

    def show_voting_options(self):
        pass

    def total_votes(self):
        pass





