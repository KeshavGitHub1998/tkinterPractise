from tkinter import *
def hello():
    s=a.get()
    print(s)
    label=Label(text=s,fg='red',bg='blue',font=10).pack()
    return ("")
#always follow the format and the series

obj=Tk()

obj.title("command")

obj.geometry("500x500+100+0")
#string variable a
a=StringVar()
#lab1=Label(text="print",fg='pink',bg='black',font=10).pack()
but1=Button(text="print",fg='pink',bg='black',font=10,command=hello)
but1.pack()
text = Entry(textvariable=a).pack()



#mainloop
obj.mainloop()

