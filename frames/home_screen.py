import tkinter as tk
from tkinter import font

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title
        title = tk.Label(self,
                         text="TOMATO TIMER",
                         font=("CocogooseProTrial Bold", 30),
        )
        title.pack(pady=(30, 50))

        form_frame = tk.Frame(self)
        form_frame.pack(expand=True)

        # StringVars
        short_break_entry_var = tk.StringVar()
        long_break_entry_var = tk.StringVar()
        study_entry_var = tk.StringVar()

        # --- Helper to create label+entry pair ---
        def add_entry(label_text, text_var):
            label = tk.Label(form_frame, text=label_text,
                             font=("CocogooseProTrial Bold", 12))
            entry = tk.Entry(form_frame, textvariable=text_var,
                             font=("Arial", 10, "bold"), width=5, justify="center")
            label.pack(pady=(5, 0))
            entry.pack(pady=(0, 10))

        add_entry("Study Time", study_entry_var)
        add_entry("Short Break", short_break_entry_var)
        add_entry("Long Break", long_break_entry_var)

        # === Bottom Play Button ===
        def play_button_clicked():
            # Just demoing one for now
            short_input = short_break_entry_var.get()
            short_break_entry_var.set("")
            print("Short Break:", short_input)

            long_input = long_break_entry_var.get()
            long_break_entry_var.set("")
            print("Long Break:", long_input)


            study_input = study_entry_var.get()
            study_entry_var.set("")
            print("Study:", study_input)

        play_button = tk.Button(self,
                                text="Start",
                                font=("CocogooseProTrial Bold", 20),
                                bd=5,
                                command=play_button_clicked
        )
        play_button.pack(pady=40, side="bottom")
