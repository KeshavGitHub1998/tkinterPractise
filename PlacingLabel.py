from tkinter import *
obj=Tk()
#created obj as object for Tk class
#deciding the grometry
obj.geometry("1000x1000+200+200")
obj.title("Program For Label")
#L1=Label(text='me',bg='red').pack()
L2=Label(text='project',bg='red',fg='yellow').place(x=10,y=10)
#used place
#now using grid
L3=Label(text='you',bg='red').grid(rows=120,column=40,sticky='w')
#note , used sticky too !


obj.mainloop()
