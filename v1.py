import tkinter as tk
import random as rnd
import math

W = 2000
H = 2000
B = 20
R = 8
infection_radius = 20
P_change_direction = 0.05
lethality = 0.05
P_infect = 0.001
velo = 1

window = tk.Tk()
canvas = tk.Canvas(window, width = W, height = H, bg="black")
population = 1000
circles = []
suspected = []
infected = []
removed = []
direction = {}
for i in range(population):
    cx = rnd.randrange(B, W - B)
    cy = rnd.randrange(B, H - B)
    c = canvas.create_oval(cx - R, cy - R, cx + R, cy + R, fill = "lightblue")
    direction[c] = rnd.random() * 2 * math.pi
    circles.append(c)
def new_infection(c):
    canvas.itemconfig(c, fill = "red")
    infected.append(c)
    suspected.remove(c)
suspected = circles.copy()
new_infection(circles[0])

def coords(c):
    (x0, y0, x1, y1) = canvas.coords(c)
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    return (cx, cy)

def is_outside_of_box(c):
    (cx, cy) = coords(c)
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
    infect()
    window.after(100, move)

def infect():
    for infector in infected:
        for victim in suspected:
            (x1, y1) = coords(infector)
            (x2, y2) = coords(victim)  
            d = (x2 - x1)**2 + (y2 - y1)**2
            if d <= infection_radius ** 2:
                if rnd.random() <= 1.0:
                    new_infection(victim)
def die(): 
    pass

graph = tk.Canvas(window, width = W, height = H, bg="black")

def update_graph():
    print(len(infected))
    graph.create_line(update_graph.day, H, update_graph.day, H - len(infected) * 5, fill = "red")
    update_graph.day += 1
    window.after(100, update_graph)
update_graph.day = 0
canvas.pack(side="left")
graph.pack(side="left")
move()
update_graph()
window.mainloop()