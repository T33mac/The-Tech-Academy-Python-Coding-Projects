
import os

from datetime import datetime



fPath = 'C:\\PyProj\\' #extra backslashes are escapes before the real backslash

print(f'\nThis function has found files ending with ".txt" \
\nfrom the C drive in the PyProj folder and displayed \nthe time they \
were generated.\n\n')

def list_txt():
    fList = os.listdir(fPath)
    for fName in (fList):
        if (fName).endswith('.txt'): #Change file type on this line
            abPath = os.path.join(fPath, fName)
            timeStamp = os.path.getmtime(abPath)
            time = datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{abPath}\n{time}\n")
    


if __name__ == "__main__":
    list_txt()
    
    
    

# C:\\PyProj\\
# textDoc.txt

#os.path.getmtime(path)
#Return the time of last modification of path.
#The return value is a floating point number giving the
#number of seconds since the epoch (see the time module).
#Raise OSError if the file does not exist or is inaccessible.
