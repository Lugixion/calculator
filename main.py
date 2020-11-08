# Modules

import tkinter as tk  
from tkinter import filedialog

def askforfile():
    file_path = filedialog.askopenfilename(title="Select a file")
    return file_path
    
root =tk.Tk()
root.withdraw()

print("Select the file. (Have to be a .TXT)")

file_path = askforfile()

# TXT Detection

while file_path.endswith(".txt") == False:
    print("File might be a .txt extension")
    file_path = askforfile()

# End of TXT Detection

print(file_path)
