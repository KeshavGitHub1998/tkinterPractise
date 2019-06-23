#opening a file or knowing the path of the file
from tkinter import *
from tkinter import filedialog
obj=Tk()
obj.geometry("500x500+100+20")
obj.title("opening the file")

def OpenFile():
    file1=filedialog.askopenfile()
    labfile=Label(text=file1,font=10,bg='red').pack()
    return ("")
    

#making of the button
ButtonOpen=Button(text="Click to choose the file",font=("arial",15,'italic'),command=OpenFile).pack()


#mainloop
obj.mainloop()
