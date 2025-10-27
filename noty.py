import tkinter as tk

noty = open('noty.txt', 'r').readline()
c = tk.Canvas(width=400, height=600)
c.pack()
spacing, y, count = 15, 20, 0

count = len(noty)
length = count//(360//31)

for i in range(length):
    for j in range(5):
        c.create_line(0, y + j*spacing, 400, y+j*spacing, width=2)
    y+=5*spacing + 20

x, y = 20, 15
for note in noty:
    match note:
        case 'c':
            notey = spacing*5
            color = "#4a2bad"
        case 'd':
            notey = spacing*4.5
            color = "#5538b5"
        case 'e':
            notey = spacing*4
            color = "#6449bf"
        case 'f':
            notey = spacing*3.5
            color = "#7057c2"
        case 'g':
            notey = spacing*3
            color = "#7c67c2"
        case 'a':
            notey = spacing*2.5
            color = "#8774c4"
        case 'h':
            notey = spacing*2
            color = "#9d8fcc"

    c.create_oval(x-6, y+notey-3, x+16, y+notey+13, width=2, outline=color)
    c.create_oval(x-2, y+notey-3, x+12, y+notey+13, width=2, outline=color)
    c.create_oval(x-3, y+notey-3, x+13, y+notey+13, width=2, outline=color)

    if x < 380:
        x+=30
    else:
        x = 20
        y += 5*spacing +20

c.mainloop()