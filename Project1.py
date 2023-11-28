from guiProject1 import *


def main():
    window = Tk()
    window.title('Cast your vote!')
    window.geometry('400x400')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()
