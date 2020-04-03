import tkinter as tk
import random as rnd
import math

W = 500
H = 500
B = 20
R = 8
P_change_direction = 0.01
lethality = 0.05
P_infect = 0.1
velo = 1

window = tk.Tk()
canvas = tk.Canvas(window, width = W, height = H, bg="black")
population = 50
circles = []
direction = {}
for i in range(population):
    cx = rnd.randrange(B, W - B)
    cy = rnd.randrange(B, H - B)
    c = canvas.create_oval(cx - R, cy - R, cx + R, cy + R, fill = "lightblue")
    direction[c] = rnd.random() * 2 * math.pi
    circles.append(c)
canvas.itemconfig(circles[0], fill = "red")
def is_outside_of_box(c):
    (x0, y0, x1, y1) = canvas.coords(c)
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    if cx < B or cx > W - B: return True
    if cy < B or cy > H - B: return True
    return False

def move():
    for c in circles:
        canvas.move(c, velo * math.sin(direction[c]), velo * math.cos(direction[c]))
        if is_outside_of_box(c):
            direction[c] += math.pi
        elif rnd.random() <= P_change_direction:
            direction[c] = rnd.random() * 2 * math.pi
    window.after(15, move)
            
def infect():
    pass

def die(): 
    pass

canvas.pack()
move()
window.mainloop()