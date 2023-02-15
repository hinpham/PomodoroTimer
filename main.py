import math
from tkinter import *
from time import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MINUTE = 60
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global timer, reps
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  timer_label.config(text="Timer")
  check.config(text='')
  reps = 0
  
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1
  
  work =  WORK_MIN * MINUTE
  short_break = SHORT_BREAK_MIN * MINUTE
  long_break = LONG_BREAK_MIN * MINUTE
  
  if reps % 8 == 0:
    timer_label.config(text="Break", fg=RED)
    count_down(long_break)
  elif reps % 2 == 0:
    timer_label.config(text="Break", fg=PINK)
    count_down(short_break)
  else:
    timer_label.config(text="Work", fg=GREEN)
    count_down(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  min = math.floor(count / 60)
  seconds = round(count % 60, 2)
  
  if seconds < 10:
    seconds = f"0{seconds}"
    
  canvas.itemconfig(timer_text, text=f"{min}:{seconds}")
  
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    marks = ''
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks += "✓"
    
    check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


photo = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check = Label(bg=YELLOW, fg=GREEN)
check.grid(column=2, row=4)

window.mainloop()