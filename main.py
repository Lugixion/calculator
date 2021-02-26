# Modules

import tkinter as tk  
from tkinter import filedialog
import os
import utils

# Preset vars 

PermOps = ['MED{', 'SUM{', 'REST{', 'MULT{']


# Functions

def SepCleOp(filetr): # Separate and Clean operations
    opsplit = filetr.split("}") # Split between operations
    linsplit = [] # Main var

    for i in opsplit:
        linsplit.append(i.split("\n")) # Separate by lines
    
    for i in linsplit:
        while "" in i: # While there are blank spaces
            i.remove("")

    for i in linsplit:
        if not any(x in PermOps for x in i): # Detect if those aren't valid ops
            linsplit.remove(i)
    
    while [] in linsplit:
        linsplit.remove([]) # Remove empty lists

    for i in linsplit: # Remove spaces from strings
        for j in i:
            if " " in j: # if there are spaces in the string
                new = [] # New list (clear number)
                newn = ""
                for num in i[i.index(j)]: # Iterates into every number
                    new.append(num)
                while " " in new: # While into list there are blank spaces
                    new.remove(" ") 
                for n in new:
                    newn += n # add all digs without blank spaces to newn
                
                spind = i.index(j) 
                i.remove(i[spind])  
                i.insert(spind, newn) # Saves the number with blanks index, delete the number and adds the new one

    for i in linsplit:
        for j in i:
            try: # Detect if value is int, else delete it
                int(j) 
            except ValueError:
                if i.index(j) != 0:
                    i.remove(j)
    
    for i in linsplit:
        for j in i:
            if i.index(j) != 0:
                i[i.index(j)] = int(i[i.index(j)]) # Converts every str into int

    DetExOp(linsplit) # Goes to detect operations

def DetExOp(listtr):

    Operations = []
    finalres = []

    for i in listtr:
        Operations.append(i[0])

    for i in listtr:
        i.remove(i[0])

    for i in range(len(listtr)):
        optodo = Operations[i]
        print(str(i) + "Operations done", end="\r")

        if optodo == "MED{":
            finalres.append(utils.MED(listtr[i]))
        elif optodo == "SUM{":
            finalres.append(utils.SUM(listtr[i]))
        elif optodo == "REST{":
            finalres.append(utils.REST(listtr[i]))
        elif optodo == "MULT{":
            finalres.append(utils.MULT(listtr[i]))
        else:
            print("Error")
    
    print("Operations done.")
    print(finalres)


# Main code     

root =tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Select a file")

os.system('clear')

# TXT Detection

if not file_path.endswith(".txt"):
    print("File is not text file (.txt)")
    exit()
    
# End of TXT Detection

file_read = open(file_path, "r").read()
SepCleOp(file_read)
