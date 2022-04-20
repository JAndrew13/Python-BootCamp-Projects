from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MIN = 60
WORK_MIN = 25 * MIN
SHORT_BREAK_MIN = 5 * MIN
LONG_BREAK_MIN = 20 * MIN

TEST_MAIN = 5
TEST_REST = 3
TEST_LONG = 5

clock = 0
reps = 0
REP_CHECK = []
timer = None
# ---------------------------- TIMER START/STOP ------------------------------- #

# def on_off():
#     global clock
#
#
#
#     if start_btn["text"] == "START" and clock >= 0:
#         """PAUSE"""
#         window.after_cancel(timer)
#         start_btn["text"] = "PAUSE"
#
#     elif start_btn["text"] == 'PAUSE':
#         """UNPAUSE"""
#         print(clock)
#         start_btn["text"] = "START"
#         countdown(clock)
#         window.after_cancel(10)
#
#     elif clock == 0:
#         print(clock)
#         """START"""
#         start_btn['text'] = 'PAUSE'
#         start()

    #TEST START
    # if clock == 0:
    #     print(clock)
    #     """START"""
    #     start_btn['text'] = 'PAUSE'
    #     start()


# ---------------------------- TIMER RESET / PAUSE ------------------------------- #
def reset():

    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text=f"00:00")
    title.config(text="Timer")
    global reps
    global REP_CHECK
    reps = 0
    REP_CHECK = []
    check_marks.config(text=REP_CHECK)
    start_btn["state"] = ACTIVE



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps+=1
    #check if unpausing and countdown with current clock
    # if start_btn["state"] == DISABLED:
    #     countdown()

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN)
        # countdown(TEST_LONG)
        print("LONG")
        REP_CHECK.append("✔")
        check_marks.config(text=REP_CHECK)
        title.config(text="Break!", fg=RED)
        start_btn["state"] = DISABLED
    elif reps % 2 == 0:
        REP_CHECK.append("✔")
        countdown(SHORT_BREAK_MIN)
        # countdown(TEST_REST)
        print("rest")
        title.config(text="Break!", fg=PINK)
        check_marks.config(text=REP_CHECK)
        start_btn["state"] = DISABLED
    else:
        countdown(WORK_MIN)
        # countdown(TEST_MAIN)
        print("rep")
        title.config(text="Timer", fg=GREEN)
        start_btn["state"] = DISABLED

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global clock
    clock = count
    print(clock)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec == "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min <10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    # if count == 0:
    else:
        start()




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50, bg=YELLOW)
window.minsize(200,400)

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,125,image=tomato_img)
timer_txt = canvas.create_text(100,135,text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1,row=0)

start_btn = Button(text="START", bg=GREEN, font=(FONT_NAME, 12, "bold"), command=start)
start_btn.grid(column=0,row=2)

reset_btn = Button(text="RESET", bg=GREEN, font=(FONT_NAME, 12, "bold"), command=reset)
reset_btn.grid(column=2,row=2)

check_title = Label(text="~Reps~", fg=PINK, bg=YELLOW, font=(FONT_NAME,18,"bold"))
check_title.grid(column=1,row=3)

check_marks = Label(text="", fg=GREEN, bg=YELLOW,font=(FONT_NAME,12,"bold"))
check_marks.grid(column=1, row=4)

window.mainloop()