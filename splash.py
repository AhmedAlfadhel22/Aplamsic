import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class App:
    def __init__(self, root):
        #setting information
        root.title("Aplamsic 2022")
        root.iconbitmap('img/favicon.ico')
        #setting window size
        width=978
        height=382
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background='black')

        GLabel_178=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=67)
        GLabel_178["font"] = ft
        GLabel_178["fg"] = "#FFFFFF"
        GLabel_178["bg"] = "#000000"
        GLabel_178["justify"] = "center"
        GLabel_178["text"] = "Aplamsic"
        GLabel_178.place(x=80,y=30,width=379,height=106)

        GLabel_995=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=20)
        GLabel_995["font"] = ft
        GLabel_995["fg"] = "#FFFFFF"
        GLabel_995["bg"] = "#000000"
        GLabel_995["justify"] = "center"
        GLabel_995["text"] = "2022"
        GLabel_995.place(x=880,y=340,width=96,height=32)
        
        def close_window():
            root.destroy()

        GButton_52=tk.Button(root) 
        GButton_52["bg"] = "#f0f0f0" 
        ft = tkFont.Font(family='Arial',size=23) 
        GButton_52["font"] = ft 
        GButton_52["fg"] = "#000000" 
        GButton_52["justify"] = "center" 
        GButton_52["text"] = "Launch" 
        GButton_52.place(x=50,y=330,width=121,height=36) 
        GButton_52["command"] = close_window

input()
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
