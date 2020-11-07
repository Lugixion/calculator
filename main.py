# Modules

import tkinter as tk  
from tkinter import filedialog

def askforfile():
    file_path = filedialog.askopenfilename(title="Select a file")

root =tk.Tk()
root.withdraw()

print("Select the file. (Have to be a .TXT)")

askforfile()

# TXT Detection

if file_path.endswith(".txt"): # Ends with .txt
    
else:
    print("File might be a .TXT extension")
    askforfile()

# End of TXT Detection

print(file_path)
