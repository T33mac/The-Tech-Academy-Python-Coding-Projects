#python 3.8.0

import os
from tkinter import *
from tkinter import filedialog
from pathlib import Path
import tkinter as tk
import sqlite3
from datetime import datetime   #(use in list block)
import shutil                   #(module used to cut and paste files with move() method)

import G2i_gui
import G2i_main


def center_window(self, w, h):  # Pass in tkinter frame (master) reference and w and height
    screen_width = self.master.winfo_screenwidth()  # winfo comes from master/tkinter
    screen_height = self.master.winfo_screenheight()
    # calculate x,y coordinates to paint the app centered on the user's screen
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))  # This function is Windows Specific
    return centerGeo


# catch if the user's clicks on x in window corner
def ask_quit(self):
    if messagebox.askokcancel("Exit program",
                              "Okay to exit application?"):  # uses tkinter's messagebox askoktocancel is tk method
        # this closes app                                                               ('title', 'message')
        self.master.destroy()
        os._exit(0)  # fully deletes from user's memory so user doesn't experience bugs after running


def check_file(self):
    src = filedialog.askdirectory()
    srcText = StringVar()
    srcText.set(f'{src}')
    return srcText

def check_file2(self):
    src2 = filedialog.askdirectory()
    srcText2 = StringVar()
    srcText2.set(f'{src2}')
    return srcText2



def move_txt(self):
    src = self.text_input1.get()
    src2 = self.text_input2.get()
    fList = os.listdir(src)
    create_db(self)
    for fName in (fList):
        if (fName).endswith('.txt'):  # Change file type on this line
            abPath = os.path.join(src, fName)
            timeStamp = os.path.getmtime(abPath)
            time = datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{abPath}\n{time}\n")
            shutil.move(f"{abPath}", f"{src2}")
            conn = sqlite3.connect('txt.db')
            with conn:  # use connection to create database/table
                cur = conn.cursor()
                cur.execute("""INSERT INTO tbl_txt (col_fname,col_time) VALUES (?,?)""", (abPath, time))
                conn.commit()  # use connection to commit
            conn.close()

def create_db(self):
    conn = sqlite3.connect('txt.db')
    with conn:  # use connection to create database/table
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_txt( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT, \
                col_time TEXT \
                );")
        conn.commit()  # use connection to commit
    conn.close()


if __name__ == "__main__":
    pass

