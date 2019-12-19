from tkinter import *
import tkinter as tk
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(475,180)
        self.master.maxsize(475,180)
        self.master.title("Check files")
        

        self.browse1Button = Button(self.master,text="Browse...",width=12,height=1)
        self.browse1Button.grid(row=2,column=0,padx=(24,0),pady=(45,0),sticky=E+W)
        self.browse2Button = Button(self.master,text="Browse...",width=12,height=1)
        self.browse2Button.grid(row=3,column=0,padx=(24,0),pady=(12,0),sticky=E+W)
        self.checkfileButton = Button(self.master,text="Check for files...",width=12,height=2)
        self.checkfileButton.grid(row=4,column=0,padx=(24,0),pady=(12,0),sticky=E+W)
        self.closeButton = Button(self.master,text="Close Program",width=12,height=2)
        self.closeButton.grid(row=4,column=4,padx=(250,0),pady=(12,0),sticky=E+W)

        self.text_input1 = Entry(self.master,text='',width=12) #creating a textbox and naming it
        self.text_input1.grid(row=2,column=2,rowspan=1,columnspan=3,padx=(30,0),pady=(42,0),sticky=E+W)
        self.text_input2 = Entry(self.master,text='',width=12)
        self.text_input2.grid(row=3,column=2,rowspan=1,columnspan=3,padx=(30,0),pady=(10,0),sticky=E+W)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
