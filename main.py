# Modules

import tkinter as tk  
from tkinter import filedialog

root =tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Select a file")

file_path_parts = file_path.split(".")

# TXT Detection

if "txt" in file_path_parts:
    # File could be a .TXT, look if in his name have more than 1 dot
    if len(file_path_parts) > 2:
        if file_path_parts[len(file_path_parts) - 1] == "txt": # If last dot of the name have TXT
            print("File is a TXT")
        else:
            print("File might be a .TXT")
else:
    # File isn't a .TXT
    print("File might be a .TXT")
    
# End of TXT Detection

print(file_path)
