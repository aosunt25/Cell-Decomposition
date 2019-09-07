from tkinter import *
import tkinter as tk
import time

'''
from Tkinter import *
import Tkinter as tk
'''
ini = 0

<<<<<<< HEAD
class Window():
    def __init__(self):
        #super("Window").__init__
        self.creatWindow()
    def creatWindow(self):
        autono = Object(1, "red", 20,20)

        windowInterface = tk.Tk()
        windowInterface.title("Cell_Decomposition")
        frame = Frame(windowInterface,width=windowInterface.winfo_screenwidth(), height=windowInterface.winfo_screenheight())
        frame.config(bg="gray")
        frame.pack()
        frame.update()
        grid = Canvas(frame, width = frame.winfo_width(), height=frame.winfo_height()/3, background="dark gray")
        grid.pack(anchor="s")
        grid.pack()
        grid.update()
        gridX=grid.winfo_screenwidth()
        gridY=grid.winfo_height()/3
        grid.create_line(0,gridY,gridX,gridY, fill="yellow")
        grid.create_line(0,gridY*2,gridX,gridY*2, fill="yellow")
        grid.pack()
        car=grid.create_oval(5,5,35,35,fill = "red")

        xd = 5
        yd = 0
        while True:
            grid.move(car,xd,yd)
            p=grid.coords(car)
            if p[3] >= gridY or p[1] <=0:
                yd = -yd
            if p[2] >= gridX or p[0] <=0:
                break
            windowInterface.update()
            time.sleep(0.025) 
                
        windowInterface.mainloop()


      
=======
>>>>>>> 57e248741fbfa5889925706364bb034bdb12fe9a
class Object():

    #Class Attribute 
    typeObject = 'car'
    def __init__(self, speed, color, initPosX, initPosY):
        self.speed = speed
        self.color = color
        self.initPosX = initPosX
        self.initPosY = initPosY
    

class Window():
    
    global ini
    start = ini
    autono = Object(5, "red", 20,20)
    grid = None
    car = None
    gridY = None
    gridX = None
    
    windowInterface = tk.Tk()

    def __init__(self):
        #super("Window").__init__
        self.creatWindow()
    
    def changeState(self):
        ini = 1
        print(ini)
        self.start = 1
        print("Start" + str(self.start))
        self.anim()
        return 

    def creatWindow(self):

        self.windowInterface.title("Cell_Decomposition")
        self.windowInterface.geometry("500x200")
        self.windowInterface.config(bg="gray")
        self.windowInterface.update()
        self.grid = Canvas(self.windowInterface, width = self.windowInterface.winfo_screenwidth(), height=self.windowInterface.winfo_screenheight(), background="dark gray")
        self.grid.pack(anchor="s")
        self.grid.update()
        self.gridX=self.grid.winfo_screenwidth()-10
        self.gridY=self.grid.winfo_screenheight()-10
        self.grid.create_line(0,40,self.gridX,40, fill="yellow")
        self.grid.create_line(0,80,self.gridX,80, fill="yellow")
        self.grid.pack()
        self.car=self.grid.create_oval(5,5,35,35,fill = "red")
        print(ini)
        start = ini
        button = Button(self.windowInterface, text = "Start", command = self.changeState)
        button.pack()
        button.place(x=250, y = 10)
                    
        self.windowInterface.mainloop()

    def anim(self):

        xd = self.autono.speed
        yd = 0
        #ini = ini
        if self.start == 1:
            self.start = 0
            while True:
                self.grid.move(self.car,xd,yd)
                p=self.grid.coords(self.car)
                if p[3] >= self.gridY or p[1] <=0:
                    yd = -yd
                if p[2] >= self.gridX or p[0] <=0:
                    break
                self.windowInterface.update()
                time.sleep(0.025) 

       


      




def main():
    Window().creatWindow()


if __name__ == '__main__':
    main()