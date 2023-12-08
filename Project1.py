from guiProject1 import *


def main():
    window = Tk()
    window.title('Voting')
    window.geometry('400x375')
    window.resizable(False, False)
    VoteGui(window)
    window.mainloop()


if __name__ == "__main__":
    main()
