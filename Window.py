from tkinter import *
import tkinter as tk
import time
import random

'''
from Tkinter import *
import Tkinter as tk
'''
ini = 0

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
    frame = None
    
    windowInterface = tk.Tk()

    def __init__(self):
        #super("Window").__init__
        self.creatWindow()
    
    #Method that changes the state of the animation, 0 does not start, 1 does start
    def changeState(self):
        #Deletes the last car used in the simulation
        self.endSimulation()

        # Variable that defines the state of the animations
        ini = 1

        # Gives back a random position Y in the grid
        carYPosition= random.randrange(0,self.grid.winfo_height()-30)

        #Creates the car of the animation with initial position of 0 in X and random position in Y
        self.car=self.grid.create_oval(0,carYPosition,30,carYPosition+30,fill = "red")
        
        self.start = 1

        #Calls the method of the animation 
        self.anim()
        return 

    def endSimulation(self):
        #Deletes the car, ending the simulation 
        self.grid.delete(self.car)
        self.car = None
        return

        
    def creatWindow(self):
        
        #Creates the interface window where the simulation will take place
        self.windowInterface.title("Cell_Decomposition")

        #Create a frame the same size of the interface window
        self.frame = Frame(self.windowInterface,width=self.windowInterface.winfo_screenwidth(), height=self.windowInterface.winfo_screenheight())
        self.frame.config(bg="gray")
        self.frame.pack()
        self.frame.update()

        #Create the road where the car will travel using the Canvas class of Tkinter
        #Defines the width and height depending of the frame 
        self.grid = Canvas(self.frame, width = self.frame.winfo_width(), height=self.frame.winfo_height()/3, background="dark gray")
        self.grid.pack()
        self.grid.update()

        #Variables that help to determin the position of the lineas of the road
        ##Dividing by three the height of the grid        
        self.gridX=self.grid.winfo_screenwidth()
        self.gridY=self.grid.winfo_height()/3

        #Create the lineas of the road, one is at grid/3 and the other one is at grid/3*2
        self.grid.create_line(0,self.gridY,self.gridX,self.gridY, fill="yellow")
        self.grid.create_line(0,self.gridY*2,self.gridX,self.gridY*2, fill="yellow")

     
        start = ini

        #Create the start button of the simulation
        buttonPositionX = self.frame.winfo_width()/2 -50
        buttonStart = Button(self.windowInterface, text = "Start", command = self.changeState)
        buttonStart.pack()
        buttonStart.place(x=buttonPositionX, y = 350)

        #Button to stop the simulation
        buttonPositionX = self.frame.winfo_width()/2 + 50
        buttonEnd = Button(self.windowInterface, text = "End", command = self.endSimulation)
        buttonEnd.pack()
        buttonEnd.place(x=650, y = 350)

        ##Starts the main loop of the interface            
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