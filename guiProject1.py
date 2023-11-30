from tkinter import *


class VoteGui:
    def __init__(self, window):
        self.window = window

        # STARTING VOTES
        self.john_votes = 0
        self.jane_votes = 0
        self.third_party_votes = 0

        # READ NAMES FROM FILES
        self.boy_names = self.read_names_from_file('BoyNames.txt')
        self.girl_names = self.read_names_from_file('GirlNames.txt')

        # Frame for main buttons
        self.main_frame = Frame(self.window)
        self.main_frame.pack(pady=10)

        # VOTE NOW BUTTON
        self.vote_now_button = Button(self.main_frame, text='Vote Now', command=self.show_vote_options)
        self.vote_now_button.pack(side='left', padx=5)

        # TOTAL BUTTON
        self.show_total_button = Button(self.main_frame, text='Show Total Votes', command=self.show_total_votes)
        self.show_total_button.pack(side='left', padx=5)

        # EXIT BUTTON
        self.exit_button = Button(self.main_frame, text='Exit', command=self.window.destroy)
        self.exit_button.pack(side='right', padx=5)

        # FRAME FOR VOTING
        self.vote_options_frame = Frame(self.window)

        self.label = Label(self.vote_options_frame, text='Choose a candidate:')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.john_button = Button(self.vote_options_frame, text='John', command=lambda: self.vote_for_candidate('John'))
        self.john_button.grid(row=1, column=0, pady=5)

        self.jane_button = Button(self.vote_options_frame, text='Jane', command=lambda: self.vote_for_candidate('Jane'))
        self.jane_button.grid(row=1, column=1, pady=5)

        self.third_party_label = Label(self.vote_options_frame, text='Vote for Third Party:')
        self.third_party_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.third_party_candidate_entry = Entry(self.vote_options_frame)
        self.third_party_candidate_entry.grid(row=3, column=0, columnspan=2, pady=5)

        self.vote_button = Button(self.vote_options_frame, text='Vote', command=self.vote_for_third_party_candidate)
        self.vote_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Label to display voting results
        self.results_label = Label(self.window, text='')
        self.results_label.pack(pady=10)

    def read_names_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

    def vote_for_candidate(self, candidate):
        self.update_results(f"Voted for {candidate}")
        if candidate == "John":
            self.john_votes += 1
        elif candidate == "Jane":
            self.jane_votes += 1

    def vote_for_third_party_candidate(self):
        third_party_candidate = self.third_party_candidate_entry.get().strip().capitalize()
        try:
            # Check if the input is a valid name
            if third_party_candidate == 'John' or third_party_candidate == 'Jane':
                raise ValueError(f"{third_party_candidate} is already a candidate.")
            elif third_party_candidate not in self.boy_names and third_party_candidate not in self.girl_names:
                raise ValueError(f"{third_party_candidate} is not a candidate.")

            if third_party_candidate:
                self.update_results(f"Voted for {third_party_candidate} (Third Party)")
                self.third_party_votes += 1
                self.third_party_candidate_entry.delete(0,END)
            else:
                self.update_results("Please enter a candidate before voting.")

        except ValueError as e:
            self.update_results(str(e))

    def show_total_votes(self):
        if self.john_votes + self.jane_votes + self.third_party_votes == 0:
            self.update_results("You must vote to see total votes.")
        else:
            total_votes_message = f"Total Votes\nJohn: {self.john_votes}\nJane: {self.jane_votes}\nThird Party: \
{self.third_party_votes}"
            self.update_results(total_votes_message)

    def show_vote_options(self):
        # self.vote_options_frame.grid_forget()
        self.vote_options_frame.pack(pady=10)

    def update_results(self, message):
        self.results_label.config(text=message)
