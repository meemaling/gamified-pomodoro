import tkinter as tk
from tkinter import font

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Setup widgets
        title = tk.Label(self,
                         text="Tomato Timer",
                         font=("CocogooseProTrial Bold", 30)
        )
        
        # Pack widgets
        title.pack(pady=25)