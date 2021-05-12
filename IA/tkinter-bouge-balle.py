from tkinter import *
import time


tk=Tk()

canvas=Canvas(tk, height=600,  width=600  , bg="white")
canvas.pack()

ball=canvas.create_oval(0,0,100,100,fil='red')



xspeed=0.1
yspeed=0.055

def action(xspeed):
    xspeed=xspeed+10
    return xspeed


extitbuton=Button(tk, text='exit', command=tk.destroy).pack()
speed=Button(tk, text='xspeed', command=action).pack()



while True:
    canvas.move(ball,xspeed,yspeed)
    pos=canvas.coords(ball)
    
    if pos[2]>=600:
        xspeed=-xspeed
        tk.destroy
    
    if pos[2]<=100:
        xspeed=-xspeed
    
    if pos[1]>=500:
        yspeed=-yspeed
    
    if pos[1]<=0:
        yspeed=-yspeed
    
    tk.update()
    time.sleep(1)
    tk.destroy()
    