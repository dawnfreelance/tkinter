"""Hello World application for TKinter"""
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello World")

name = tk.Label(root, text="My name is Joseph!")
click_me = tk.Button(root, text="Click Me!")
enter = tk.Entry(root, text="Enter some text here")

label.pack()
name.pack()
click_me.pack()
enter.pack()

root.mainloop()
