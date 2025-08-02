# Timer class
# Default increments is 25 min work, 5 min break 4x --> 15 min break

import time

class Timer:
    def __init__(self, study=25, short_break=5, long_break=15):
        self.study = study
        self.short_break = short_break
        self.long_break = long_break
    
    def start_timer(self, minute_duration, title):
        minutes = 0
        seconds = 0
        while minutes <= minute_duration: 
            time.sleep(1)
            seconds += 1
            if seconds >= 60:
                minutes += 1
                seconds = 0
            print(f"{minute_duration} minute {title}  {minutes:02d}:{seconds:02d}")

    def start_pomodoro(self):
        pomodoros = 0
        while pomodoros <= 4:
            self.start_timer(self.study, "study")
            pomodoros += 1
            self.start_timer(self.short_break, "break")
        self.start_timer(self.long_break, "break")


tomato = Timer()
tomato.start_pomodoro()