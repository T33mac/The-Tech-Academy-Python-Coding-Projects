
import os

import sqlite3

conn = sqlite3.connect('PySql.db')

fPath = 'C:\\PySqlDrill\\PySqlFiles\\'

fList = os.listdir(fPath)

newlist = []

def list_txt():
    for i in (fList):
        if (i).endswith('.txt'):
            newlist.append(i)

func = list_txt()


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('PySql.db')

with conn:
    cur = conn.cursor()
    for (i) in newlist:
        cur.execute("INSERT INTO tbl_txt(col_file) VALUES (?)", (i,))
    conn.commit()
conn.close()

print('The txt files from the "PySqlFiles" folder are:')
for i in newlist:
    print(f'"{i}"')

if __name__ == "__main__":
    list_txt()

