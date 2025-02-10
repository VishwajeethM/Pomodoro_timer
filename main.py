from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    min0 = count_min % 10
    min1 = math.floor(count_min / 10)
    count_sec = count % 60
    sec0 = count_sec % 10
    sec1 = math.floor(count_sec / 10)

    canvas.itemconfig(timer_text, text=f"{min1}{min0}:{sec1}{sec0}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

tick_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
tick_label.grid(row=2, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


window.mainloop()
