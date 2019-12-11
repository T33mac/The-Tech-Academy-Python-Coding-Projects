
import os

from datetime import datetime




fPath = 'C:\\PyProj\\' #extra backslashes are escapes before the real backslash



def Create_List():
    fList = os.listdir(fPath)
    for i in (fList):
        print.(i)
    
        

#abPath = os.path.join(fPath, fName)
#print(abPath)

#timeStamp = os.path.getmtime(abPath)

#time = datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
#print(time)


if __name__ == "__main__":
    Create_List()

#if m.endswith('.mp3'):
# C:\\PyProj\\
# textDoc.txt

#os.path.getmtime(path)
#Return the time of last modification of path.
#The return value is a floating point number giving the
#number of seconds since the epoch (see the time module).
#Raise OSError if the file does not exist or is inaccessible.
