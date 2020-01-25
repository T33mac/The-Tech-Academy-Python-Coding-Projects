#python 3.8.0

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import G2i_gui
import G2i_func


#Tkinter Frame Class that our own class will inherit from
class ParentWindow(Frame): #ParentWindow:self , Frame:Master
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #Define master frame config
        self.master = master
        self.master.minsize(500,350) #height,width
        self.master.maxsize(500,350)
        #Will center app on screen
        G2i_func.center_window(self,500,350)
        self.master.title("Tkinter .txt Mover")
        self.master.configure(bg="#F0F0F0")
        #Catches if "x" in upper corner
        self.master.protocol("WM_DELETE_WINDOW",lambda: G2i_func.ask_quit(self))
        arg = self.master

        # load gui widgets from separate module(phonebook_gui.py)
        # keeps code uncluttered
        G2i_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()              #Creates window
    App = ParentWindow(root)    #Passes to class
    root.mainloop()             #Makes it main loop so it doesn't close right away
