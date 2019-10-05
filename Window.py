from tkinter import *
import tkinter as tk
from Graph import Graph

import time
import random

'''
from Tkinter import *
import Tkinter as tk
'''

ini = 0

class Cell():
    def __init__(self, posX0, posX1, posY0, posY1, withObject):
        self.posX0=posX0
        self.posX1=posX1
        self.posY0=posY0
        self.posY1=posY1
        self.withObject= withObject


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
    autono = Object(1, "red", 20,20)

    grid = None
    obj = []
    cell = []
    graph = Graph()


    car = None
    gridY = None
    gridX = None
    frame = None
    
    windowInterface = tk.Tk()

    def __init__(self):
        #super("Window").__init__
        self.creatWindow()

    
    def cellPrint(self):

        for i in range(len(self.cell)):
            print(self.cell[i].posX0," ",self.cell[i].posX1)
            


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
        #Randomize the Y coordinates of the obstacles in the grid
        arrX = []
        arrY = []
        for i in range(5):
            arrX.append(random.randrange(100,self.grid.winfo_width()-30))
            arrY.append(random.randrange(30,self.grid.winfo_height()-30))
        self.mergeSort(arrX)
        
        for i in range(len(arrX)):         
            print(arrX[i])
            print(" ") 
        print()
        #Creates 5 obtacles with the coordinates, color and speed
        #Speed equals to 0 because the obstacles dont have movement
        for i in range(5):
            obj1=Object(0,"blue", arrX[i],arrY[i] )
            self.obj.append(obj1)

        self.cellBuild(arrX)
        self.chechCellObject()
        self.cellPrint()
        

        
        
        
        try:
            
            for i in range(len(self.obj)):
                lineStart=self.grid.winfo_height()-self.grid.winfo_height()
                #Creates the line in the side of each object in the interface 
                self.grid.create_line(self.obj[i].initPosX,lineStart,self.obj[i].initPosX,self.grid.winfo_height(),fill = "black", dash=(4,4))
                self.grid.create_line(self.obj[i].initPosX+50,lineStart,self.obj[i].initPosX+50,self.grid.winfo_height(),fill = "black", dash=(4,4))
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

    def cellBuild(self, arrX):
        amountOfObject=iter(range(5))

        for i in amountOfObject:
            print("Object Num:",i)
            j = i + 1
            farX = i
            x1 = arrX[i]+50
            if i ==0:
                self.addCell(0,arrX[i],False)
            try:
                #If the coordinates in X are in the same range they  merge 
                # add a cell between the x0 of the first object and
                # x1 of the next object
                #until the next object is not on the same range 
                if (arrX[i])<=arrX[j] and x1>= arrX[j]:
                    for j in range (5):
                        if (arrX[i])<=arrX[j] and x1>= arrX[j]:
                            
                            print("Object Num 2:",j, "Valor X de J: ", arrX[j])
                            farX=j
                            x1= arrX[farX]+50

                    #adds the cells that were merged 
                    
                    for z in range(farX-i):
                        next(amountOfObject) 
                    print("FarX: ", farX)
                    self.addCell(arrX[i], x1, True)
                    if farX<4:
                        self.addCell(x1,arrX[farX+1], False)
                    else:
                        self.addCell(x1,self.grid.winfo_width(), False)
                     
                else:
                    print("Object Num a:",i)
                    #Adds a cell the size of the object because is not in the range of any object
                    #and between the x1 of this object and x0 of the next 
                    self.addCell(arrX[i], arrX[i]+50, True)
                    self.addCell(arrX[i]+50,arrX[i+1], False)
                    pass            
            except:
                if (arrX!=-1):
                    print("Object Num b:",i)
                    self.addCell(arrX[i], arrX[i]+50,True)
                    self.addCell(arrX[i]+50, self.grid.winfo_width(),False)
                pass
            
            
            
    def addCell(self, x0, x1, obj):
        lowerCell = None
        middleCell = None
        upperCell = None
        if obj == TRUE:
        #Adds the coordinates to the lower, middle and upper cell that the object creates 
            lowerCell = Cell(x0,x1,0,self.gridY, False)
            middleCell = Cell(x0,x1,self.gridY,self.gridY*2, False)
            upperCell= Cell(x0,x1,self.gridY*2,self.grid.winfo_height(),False)
        else:
            lowerCell = Cell(x0,x1,0,self.gridY, False)
            middleCell = Cell(x0,x1,self.gridY,self.gridY*2, False)
            upperCell= Cell(x0,x1,self.gridY*2,self.grid.winfo_height(),False)
        #Push lower, middle and upper cell to an array 
        self.cell.append(lowerCell)
        self.cell.append(middleCell)
        self.cell.append(upperCell)

    def graphBuild(self):
        for i in range(1,len(self.cell)+1):
            if (i + 3)<= len(self.cell):
                print("graph i:",i)
                if (i%3)== 1:
                    self.graph.addEdge(i-1,i)
                    self.graph.addEdge(i-1,i+2)
                elif (i%3)== 2:
                    self.graph.addEdge(i-1,i-2)
                    self.graph.addEdge(i-1,i)
                    self.graph.addEdge(i-1,i+2)
                else:
                    self.graph.addEdge(i-1,i)
                    self.graph.addEdge(i-1,i+2)
            else:
                if (i%3)== 1:
                    self.graph.addEdge(i-1,i)
                    self.graph.addEdge(i-1,i-2)
                elif (i%3)== 2:
                    self.graph.addEdge(i-1,i)
                    self.graph.addEdge(i-1,i-2)
                    self.graph.addEdge(i-1,i-4)
                else:
                    self.graph.addEdge(i-1,i-2)
                    self.graph.addEdge(i-1,i-4)
        
    #Method tha checks which cell has an object inside    
    def chechCellObject(self):
        for i in range(len(self.cell)):
            for j in range(len(self.obj)): 
                #If the size of the object is inside de cell enters
                if(self.cell[i].posX0<=self.obj[j].initPosX and self.cell[i].posX1>=self.obj[j].initPosX+50):  
                    #if the y0 of the object is in range of the cell
                    if(self.cell[i].posY0>= self.obj[j].initPosY and self.cell[i].posY0<= self.obj[j].initPosY +30 ):
                        self.cell[i].withObject=True
                        pass
                    #if the y1 of the object is in range of the cell    
                    elif(self.cell[i].posY1 >= self.obj[j].initPosY and self.cell[i].posY1<= self.obj[j].initPosY +30):
                        self.cell[i].withObject=True
                        pass
                    #if the object is inside of the cell
                    elif(self.cell[i].posY0<=self.obj[j].initPosY and self.cell[i].posY1>=self.obj[j].initPosY+30):
                        self.cell[i].withObject=True
                        pass


    def printGraf(self):
        for i in range(len(self.graph)):
            print(self.graph)

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
        self.graphBuild()
        xd = self.autono.speed
        yd = 0
        #ini = ini
        if self.start == 1:
            self.start = 0
            
            print("Cords")

            #Aqui las distancias
            self.grid.move(self.car,xd,yd)
            p=self.grid.coords(self.car)
            for i in range(len(self.cell)):

                if self.cell[i].posX0 < p[0] and self.cell[i].posX1 -p[0] and self.cell[i].posY0 < p[1] and self.cell[i].posY1 > p[1]:
                        print("Inicio en la celda " + str(i))
                        self.graph.BFS(i)

            while True:
                
                self.grid.move(self.car,xd,yd)
                p=self.grid.coords(self.car)
                #print(self.grid.coords(self.car))

                

                #for i in range(len(self.cell)):
                    #Aqui las distancias

                    #if self.cell[i].posX0 < p[0] and self.cell[i].posX1 -p[0] and self.cell[i].posY0 < p[1] and self.cell[i].posY1 > p[1]:
                       #print("Estoy en la celda " + str(i+1))
                
                #En que celda estoy?
                
                if p[3] >= self.gridY or p[1] <=0:
                    yd = -yd
                if p[2] >= self.gridX or p[0] <=0:
                    break
                self.windowInterface.update()
                time.sleep(0.025) 


    def mergeSort(self, arr): 
        if len(arr) >1: 
            mid = len(arr)//2 #Finding the mid of the array 
            L = arr[:mid] # Dividing the array elements  
            R = arr[mid:] # into 2 halves 
    
            self.mergeSort(L) # Sorting the first half 
            self.mergeSort(R) # Sorting the second half 
    
            i = j = k = 0
            
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
            
            # Checking if any element was left 
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
            
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
       



def main():
    Window().creatWindow()


if __name__ == '__main__':
    main()