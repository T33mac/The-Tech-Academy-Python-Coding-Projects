import os

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import Gui_main
import Gui_gui

def center_window(self, w, h): #Pass in tkinter frame (master) reference and w and height
    screen_width = self.master.winfo_screenwidth() #winfo comes from master/tkinter
    screen_height = self.master.winfo_screenheight()
    # calculate x,y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))  #This function is Windows Specific
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"): #uses tkinter's messagebox askoktocancel is tk method
        #this closes app                                                               ('title', 'message')
        self.master.destroy()
        os._exit(0)

def check_file(self):
    src = filedialog.askdirectory()
    srcText = StringVar()
    srcText.set(f'{src}')
    return srcText




if __name__ == "__main__":
    pass
