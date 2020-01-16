from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import Gui_main
import Gui_func

def load_gui(self):
    self.checkfileButton = tk.Button(self.master,text="Check for files...", width=12, height=2, command=lambda: print_result(self))
    self.checkfileButton.grid(row=4, column=0, padx=(24, 0), pady=(12, 0),sticky=E+W)
    self.closeButton = tk.Button(self.master, text="Close Program", width=12, height=2, command=lambda: Gui_func.ask_quit(self))
    self.closeButton.grid(row=4, column=4, padx=(250, 0), pady=(12, 0), sticky=E+W)

def print_result(self):
    self.text_input2 = tk.Entry(self.master, textvariable=Gui_func.check_file(self))
    self.text_input2.grid(row=3, column=0, rowspan=1, columnspan=5, padx=(30, 0), pady=(10, 0), sticky=E + W)




if __name__ == "__main__":
    pass
