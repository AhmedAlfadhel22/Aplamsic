import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkcode import CodeEditor
code=input("Enter file name : ")

root = tk.Tk()
root.title("Aplamsic 2022")
root.option_add("*tearOff", 0)
root.iconbitmap('img/favicon.ico')


notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text=code+'.py')
notebook.pack(fill="both", expand=True)

code_editor = CodeEditor(
    tab_1,
    width=99,
    height=30,
    language="python",
    background="black",
    highlighter="dracula",
    font="Consolas",
    autofocus=True,
    blockcursor=True,
    insertofftime=0,
    padx=10,
    pady=10,
    
)
code_editor.pack(fill="both", expand=True)
code_editor.content = """print("Hello World")"""
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
input()
root.mainloop()