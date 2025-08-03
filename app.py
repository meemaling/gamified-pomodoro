import tkinter as tk
from frames.home_screen import HomeScreen

class App(tk.Tk):
        def __init__(self):
            super().__init__()
            # Setup root window
            self.title = "Tomato Timer"
            self.geometry('400x500')

            # Container for frames
            container = tk.Frame(self)
            container.pack(fill="both", expand=True)

            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for f in (HomeScreen,):
                frame = f(container, self)
                self.frames[f.__name__] = frame
                frame.grid(row=0, column=0, sticky = "nsew")

            self.show_frame("HomeScreen")

        # Method to change frames
        def show_frame(self, frame_name):
            frame = self.frames[frame_name]
            frame.tkraise()