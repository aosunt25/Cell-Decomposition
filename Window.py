from tkinter import *
import tkinter as tk

import time
import random

'''
from Tkinter import *
import Tkinter as tk
'''

ini = 0
class Graph():
    # Constructor 
    def __init__(self): 
  
        
        self.graph = defaultdict(list)
            
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
     
    def BFS(self, s): 
  
        visited = [False] * (len(self.graph)) 
        queue = [] 
  
        
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

class Cell():
    def __init__(self, posX0, posX1, posY0, posY1):
        self.posX0=posX0
        self.posX1=posX1
        self.posY0=posY0
        self.posY1=posY1


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
    obj = []
    cell = []

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

        #Randomize the X coordinates of the obstacles in the grid
        randx1 = random.randrange(100,self.grid.winfo_width()-30)
        randx2 = random.randrange(100,self.grid.winfo_width()-30)
        randx3 = random.randrange(100,self.grid.winfo_width()-30)
        randx4 = random.randrange(100,self.grid.winfo_width()-30)
        randx5 = random.randrange(100,self.grid.winfo_width()-30)

        #Randomize the Y coordinates of the obstacles in the grid
        randy1 = random.randrange(30,self.grid.winfo_height()-30)
        randy2 = random.randrange(30,self.grid.winfo_height()-30)
        randy3 = random.randrange(30,self.grid.winfo_height()-30)
        randy4 = random.randrange(30,self.grid.winfo_height()-30)
        randy5 = random.randrange(30,self.grid.winfo_height()-30)
        #Creates 5 obtacles with the coordinates, color and speed
        #Speed equals to 0 because the obstacles dont have movement
        obj1 = Object(0,"blue", randx1,randy1 )
        obj2 = Object(0,"blue", randx2,randy2 )
        obj3 = Object(0,"blue", randx3,randy3 )
        obj4 = Object(0,"blue", randx4,randy4 )
        obj5 = Object(0,"blue", randx5,randy5 )

        #Adds each element to the array of obstacles
        self.obj.append(obj1)
        self.obj.append(obj2)
        self.obj.append(obj3)
        self.obj.append(obj4)
        self.obj.append(obj5)

        try:
            
            for i in range(len(self.obj)):
                lineStart=self.grid.winfo_height()-self.grid.winfo_height()
                #Creates the line in the side of each object in the interface 
                self.grid.create_line(self.obj[i].initPosX,lineStart,self.obj[i].initPosX,self.grid.winfo_height(),fill = "black", dash=(4,4))
                self.grid.create_line(self.obj[i].initPosX+50,lineStart,self.obj[i].initPosX+50,self.grid.winfo_height(),fill = "black", dash=(4,4))
                #Adds the coordinates to the lower, middle and upper cell that the object creates 
                lowerCell = Cell(self.obj[i].initPosX,self.obj[i].initPosX+50,0,self.gridY)
                middleCell = Cell(self.obj[i].initPosX,self.obj[i].initPosX+50,self.gridY,self.gridY*2)
                upperCell= Cell(self.obj[i].initPosX,self.obj[i].initPosX+50,self.gridY*2,self.grid.winfo_height())
                #Push lower, middle and upper cell to an array 
                self.cell.append(lowerCell)
                self.cell.append(middleCell)
                self.cell.append(upperCell)
                print(cellMax.posY0)
                print(cellMin.posY0)
                self.obj[i] = self.grid.create_rectangle(self.obj[i].initPosX,self.obj[i].initPosY,self.obj[i].initPosX + 50,self.obj[i].initPosY + 30,fill="blue")
               
                
        except:
            print("ntp")


        self.start = 1

        #Calls the method of the animation 
        self.anim()
        return 

    def endSimulation(self):
        #Deletes the car, ending the simulation 

        self.grid.delete(self.car)
        try:
            for i in range(len(self.obj)):
                self.grid.delete(self.obj[i])
        except:
            print("ntp")
        self.obj = [] 
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
        self.grid.create_line(0,self.gridY,self.gridX,self.gridY, fill="yellow",dash=(4, 2))
        self.grid.create_line(0,self.gridY*2,self.gridX,self.gridY*2, fill="yellow",dash=(4, 2))
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