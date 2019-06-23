from tkinter import *
from tkinter import colorchooser
obj=Tk()
obj.title("color")
obj.geometry("500x500+100+0")

#defining col
def col():
    color=colorchooser.askcolor()
    print(color)
    #color will come in tuple form
    labcol=Label(text=color[1],font=20,bg=color[1]).pack()
    return("")
#selecting color
#color=colorchooser.askcolor()

but1=Button(text="Choose Color",font=10,command=col).pack()

obj.mainloop()
