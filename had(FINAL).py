import tkinter as tk

c=tk.Canvas(width=400, height=400)
c.pack()

def UrciSmer(event):
    global smer
    if event.keysym=="Up":
        smer=[0,-1]
    if event.keysym=="Down":
        smer=[0,1]
    if event.keysym=="Right":
        smer=[1,0]
    if event.keysym=="Left":
        smer=[-1,0]
    print(smer)

def Animacia():
    global snakex, snakey, snake, smer, collision
    c.delete('all')

    snakex += smer[0]
    snakey += smer[1]

    for i in range(0, len(snake),2):
        if snakex == snake[i] and snakey == snake[i+1]:
            c.delete("all")
            collision = True
            c.create_text(200,200, text="Nazaril si")

    if not collision:
        
        snake.append(snakex)
        snake.append(snakey)

        c.create_line(snake)

        c.after(10, Animacia)
    
#ZACIATOK PROGRAMU

collision = False
smer=[0,-1]
snake=[200, 200]
snakex, snakey = 200, 200

c.bind_all("<Key>", UrciSmer)
Animacia()
