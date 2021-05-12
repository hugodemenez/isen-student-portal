from tkinter import *
import time


tk=Tk()

canvas=Canvas(tk, height=600,  width=600  , bg="white")
canvas.pack()




pointcrane1=[240,567,360,567,520,400,520,300,500,267,520,100.5,400,34,200,34,80,100.5,100,267,80,300.3,80,300.3,80,400.2,240,566.7]
crane1=canvas.create_polygon(pointcrane1, fill='white', outline='black', width=4)

pointoeilg=[220,300.3,140,290.3,152,270.3,208,257,240,283.65,220,300.3]
oeilg=canvas.create_polygon(pointoeilg, fill='white', outline='black', width=4)

pointoeild=[380,300.3,460,290.3,448,270.3,392,257,360,283.6,380,300.3]
oeild=canvas.create_polygon(pointoeild, fill='white', outline='black', width=4)

pointbouche1=[240,500,360,500,400,466.8,360,433.5,300,450.15,240,433.5,200,466.8,400,466.8,200,466.8,240,500]
bouche1=canvas.create_polygon(pointbouche1, fill='white', outline='black', width=4)

pointcrane2=[200,566.7,400,566.7,520,400.2,520,300.3,500,267,520,100.5,400,33.9,200,33.9,80,100.5,100,267,80,300.3,80,400.2,200,566.7]
crane2=canvas.create_polygon(pointcrane2, fill='white', outline='black', width=4)

pointbouche2=[200,466.8,240,423.5,300,433.5,360,423.5,400,466.8,360,456.8,240,456.8,200,466.8,240,516.7,360,516.75,400,466.8,360,483.45,240,483.45,200,466.8]
bouche2=canvas.create_polygon(pointbouche2, fill='white', outline='black', width=4)

def parler():

    for i in range (4):
        canvas.create_polygon(pointcrane2, fill='white', outline='white', width=4)
        crane1=canvas.create_polygon(pointcrane1, fill='white', outline='black', width=4)
        oeilg=canvas.create_polygon(pointoeilg, fill='white', outline='black', width=4)
        oeild=canvas.create_polygon(pointoeild, fill='white', outline='black', width=4)
        bouche1=canvas.create_polygon(pointbouche1, fill='white', outline='black', width=4)
        tk.update()
        time.sleep(1)
        crane1=canvas.create_polygon(pointcrane1, fill='white', outline='white', width=4)
        crane2=canvas.create_polygon(pointcrane2, fill='white', outline='black', width=4)
        bouche2=canvas.create_polygon(pointbouche2, fill='white', outline='black', width=4)
        oeilg=canvas.create_polygon(pointoeilg, fill='white', outline='black', width=4)
        oeild=canvas.create_polygon(pointoeild, fill='white', outline='black', width=4)
        tk.update()
        time.sleep(0.5)
    time.sleep(3)
    tk.destroy()
        
parler()

