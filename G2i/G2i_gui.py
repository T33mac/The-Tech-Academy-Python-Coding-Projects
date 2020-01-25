#python 3.8.0

from tkinter import *
import tkinter as tk

import G2i_main
import G2i_func

def load_gui(self):  # self is the key to access all load_gui class objects

    self.label_srcDirectory = tk.Label(self.master, text='Source Directory:')
    self.label_srcDirectory.grid(row=0, column=0, padx=(25, 0), pady=(20, 0), sticky=N + E)
    self.label_destDirectory = tk.Label(self.master, text='New Directory:')
    self.label_destDirectory.grid(row=3, column=0, padx=(20, 5), pady=(30, 0), sticky=N + E)    # rowspan and ccolumnspan default =1
    self.label_moveDirectory = tk.Label(self.master, text='Move .txt Files:')
    self.label_moveDirectory.grid(row=6, column=0, padx=(20, 5), pady=(30, 0), sticky=N + E)

    # Buttons
    self.btn_browse = tk.Button(self.master, width=12, height=2, text='Browse',
                             command=lambda: print_result1(self))
    self.btn_browse.grid(row=0, column=1, padx=(27, 40), pady=(10, 0), sticky=N + W)
    self.btn_dest = tk.Button(self.master, width=12, height=2, text='Browse',
                                command=lambda: print_result2(self))
    self.btn_dest.grid(row=3, column=1, padx=(27, 40), pady=(20, 0),sticky=N + W)
    #self.btn_dest = tk.Button(self.master, width=12, height=2, text='Browse Dest.',
                                #command=lambda: G2i_func.onDelete(self))
    #self.btn_dest.grid(row=4, column=0, padx=(27, 0), pady=(20, 0), sticky=N + W)
    self.moveTxt = tk.Button(self.master, width=12, height=2, text='Move .txt',
                               command=lambda: G2i_func.move_txt(self))
    self.moveTxt.grid(row=6, column=1, padx=(27, 40), pady=(20, 0), sticky=N + W)

    self.text_input4 = tk.Entry(self.master, text='')
    self.text_input4.grid(row=2, column=0, rowspan=1, columnspan=3, padx=(10, 0), pady=(10, 0), sticky=E + W)

    self.text_input5 = tk.Entry(self.master, text='')
    self.text_input5.grid(row=5, column=0, rowspan=1, columnspan=3, padx=(10, 0), pady=(10, 0), sticky=E + W)

    #self.text_input6 = tk.Entry(self.master, text='')
    #self.text_input6.grid(row=8, column=0, rowspan=1, columnspan=3, padx=(10, 0), pady=(10, 0), sticky=E + W)


def print_result1(self): #open pyProj/files for drill to work
    self.text_input1 = tk.Entry(self.master, textvariable=G2i_func.check_file(self))
    self.text_input1.grid(row=2, column=0, rowspan=1, columnspan=3, padx=(10, 0), pady=(10, 0), sticky=E + W)

def print_result2(self): #open pyProj2/files to work
    self.text_input2 = tk.Entry(self.master, textvariable=G2i_func.check_file2(self))
    self.text_input2.grid(row=5, column=0, rowspan=1, columnspan=3, padx=(10, 0), pady=(10, 0), sticky=E + W)



if __name__ == "__main__":
    pass
