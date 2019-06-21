from tkinter import *
#defining methods used in label and button
#def hello():
#    Lab2=Label(text="hi",fg='green',bg='white',font=5).pack()
#return ""
def dele():
    Lab3=Label(text='chal nikal',fg='pink',font=6).pack()
    return ""
    
obj=Tk()
obj.title("sizeof button")
obj.geometry("1000x200+100+100")
#creeating the label and button and now making the font size change
#Lab1=Label(text="S1",fg='blue',bg='red',command=hello,font=10).pack()
But=Button(text="B1",fg='black',bg='pink',command=dele,font=30).pack()
obj.mainloop()
#error tkinter.TclError: unknown option "-command"
#label command accept ni krta , solution 
