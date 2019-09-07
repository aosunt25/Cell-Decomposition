from tkinter import *
import tkinter as tk

class Window():
    def __init__(self):
        super().__init__
        self.creatWindow()
    def creatWindow(self):
   
        windowInterface = tk.Tk()
        windowInterface.title("Cell_Decomposition")
        windowInterface.geometry("500x200")
        windowInterface.config(bg="gray")
        windowInterface.update()
        grid = Canvas(windowInterface, width = windowInterface.winfo_screenwidth(), height=120, background="dark gray")
        grid.pack(anchor="c")
        grid.update()
        gridY=grid.winfo_screenheight()/3
        gridX=grid.winfo_screenwidth()-10
        grid.create_line(0,gridY,gridX,gridY, fill="yellow")
        grid.create_line(0,gridY*2,gridX,gridY*2, fill="yellow")
        grid.pack()
        car=grid.create_oval(5,5,40,40,fill = "red")
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
