from tkinter import *
import time


tk=Tk()

canvas=Canvas(tk, height=600,  width=600  , bg="white")
canvas.pack()

ball=canvas.create_oval(0,0,30,30,fil='red')
bouhe=canvas.create_line(100,500,500,500)


xspeed=0.7
a=0

while True:

    canvas.coords(ball, 200,200,250,250)



    
    tk.update()
    time.sleep(1)
    # tk.destroy()
    

    canvas.coords(ball, 200,200,550,250)
    tk.update()
    time.sleep(1)
    
    