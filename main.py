from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Tkinter label example")

example_label = Label(root, text="This is the example label")
example_label.pack()

root.mainloop()