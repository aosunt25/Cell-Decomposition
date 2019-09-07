from Tkinter import *
import Tkinter as tk
import time

'''
from Tkinter import *
import Tkinter as tk
'''

class Window():
    def __init__(self):
        #super("Window").__init__
        self.creatWindow()
    def creatWindow(self):
        autono = Object(1, "red", 20,20)

        windowInterface = tk.Tk()
        windowInterface.title("Cell_Decomposition")
        windowInterface.geometry("500x200")
        windowInterface.config(bg="gray")
        windowInterface.update()
        grid = Canvas(windowInterface, width = windowInterface.winfo_screenwidth(), height=windowInterface.winfo_screenheight(), background="dark gray")
        grid.pack(anchor="s")
        grid.update()
        gridX=grid.winfo_screenwidth()-10
        gridY=grid.winfo_screenheight()-10
        grid.create_line(0,40,gridX,40, fill="yellow")
        grid.create_line(0,80,gridX,80, fill="yellow")
        grid.pack()
        car=grid.create_oval(5,5,35,35,fill = "red")

        xd = 5
        yd = 10
        while True:
            grid.move(car,xd,yd)
            p=grid.coords(car)
            if p[3] >= gridY or p[1] <=0:
                yd = -yd
            if p[2] >= gridX or p[0] <=0:
                xd = -xd
            windowInterface.update()
            time.sleep(0.025) 
                
        windowInterface.mainloop()


      
class Object():

    #Class Attribute 
    typeObject = 'car'
    def __init__(self, speed, color, initPosX, initPosY):
        self.speed = speed
        self.color = color
        self.initPosX = initPosX
        self.initPosY = initPosY
    


def main():
    Window().creatWindow()


if __name__ == '__main__':
    main()
