from tkinter import *
obj=Tk()
obj.geometry("500x400+100+10")
obj.title("radio buttons")


but1=Radiobutton(obj,text='button',padx=40).pack(anchor=W)
but2=Radiobutton(obj,text='button').pack(anchor=E)
but3=Radiobutton(obj,text='button',pady=100).pack()
but4=Radiobutton(obj,text='button').pack(anchor=W)


obj.mainloop()
