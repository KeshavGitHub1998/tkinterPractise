from tkinter import *
import tkinter as tk

counter=0
def counter_label(self):
    counter=0
    def count():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
    
root=tk.Tk()
root.title("counter")
label=tk.Label(root,fg='red')
label.pack()

counter_label(label)
button=tk.Button(root,text="stop",fg='pink',width=40,command=root.destroy).pack()

root.mainloop()
