from tkinter import *
ob1=Tk()
ob2=Tk()

#defining the functions
def cm1():
    e1=w.get()
    cm1lab=Label(ob1,text=e1,bg='red',fg='white',font=10).pack()
    return ("")
def cm2():
    e2=x.get()
    cm2lab=Label(ob2,text=e2,bg='red',fg='white',font=10).pack()
    return ("")
    

#giving titles
ob1.title("1st window")
ob2.title("2nd window")

#defining geometry
ob1.geometry("500x500+100+0")
ob2.geometry("500x500+600+500")

#string vars for the entry
w=StringVar()
x=StringVar()

#label and button
lab1=Label(ob1,text='lab1',bg='black',fg='white').pack()
but1=Button(ob1,text='but1',bg='black',fg='white',command=cm1)
but1.pack()
lab2=Label(ob2,text='lab2',bg='black',fg='white').pack()
but2=Button(ob2,text='but2',bg='black',fg='white',command=cm2)
but2.pack()

#making the text area
text=Entry(ob1,textvariable=w).pack()
text=Entry(ob2,textvariable=x).pack()

ob2.mainloop()
