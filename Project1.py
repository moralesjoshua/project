from guiProject1 import *


def main():
    window = Tk()
    window.title('Cast your vote!')
    window.geometry('450x450')
    window.resizable(False, False)
    # VOTING PICTURE
    original_vote_image = Image.open('voting.webp')
    resized_image = original_vote_image.resize((250, 250))
    vote_img = ImageTk.PhotoImage(resized_image)
    vote_label = Label(image=vote_img)
    vote_label.pack(anchor='center', padx=10, pady=30)
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()
