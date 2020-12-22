from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600


tk = Tk()
canvas = Canvas(tk, width=WIDTH, height= HEIGHT)
tk.title("Window")
canvas.pack()


# ----------------------------------------- Horizontally ----------------------------------------------------------------------------

# left top right bottom

ball = canvas.create_oval(10, 10, 100, 100, fill="orange")

xspeed = 5
yspeed = 0

while True:
    canvas.move(ball, xspeed, 0)
    pos = canvas.coords(ball)
    if pos[0] <= 0 or pos[2] >= WIDTH:
        xspeed = - xspeed
    tk.update()
    time.sleep(0.01)


# -----------------------------------------End of Horizontally ----------------------------------------------------------------------------


tk.mainloop()

