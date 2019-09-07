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
        grid.pack(anchor="s")
        grid.update()
        gridX=grid.winfo_screenwidth()-10
        grid.create_line(0,40,gridX,40, fill="yellow")
        grid.create_line(0,80,gridX,80, fill="yellow")
        grid.pack()
        car=grid.create_oval(5,5,35,35,fill = "red")
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
