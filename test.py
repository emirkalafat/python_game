#import tkinter as tk
#master = tk.Tk()
#label = tk.Label(master, text='First Name').grid(row=0)
#e1 = tk.Entry(master)
#e1.grid(row=0, column=1)
#button = tk.Button(master, text='Stop', width=25, command=master.destroy).grid(row=1,column=1)
#tk.mainloop()

from tkinter import *
root=Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

textBox=Text(root, height=2, width=10)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()