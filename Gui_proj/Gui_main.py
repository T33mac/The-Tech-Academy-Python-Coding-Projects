import os

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import Gui_gui
import Gui_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(475, 180)
        self.master.maxsize(475, 180)
        
        Gui_func.center_window(self, 475, 180)
        
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: Gui_func.ask_quit(self))
        arg = self.master

        Gui_gui.load_gui(self)
        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
