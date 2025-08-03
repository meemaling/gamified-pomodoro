from pomodoro.timer import Timer
from frames.home_screen import HomeScreen
from tkinter import *

def main():
    # Setup root window
    root = Tk()
    root.title = "Tomato Timer"
    root.geometry('400x500')

    # Initialize  and pack home screen
    home_screen = HomeScreen(root, root)
    home_screen.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()