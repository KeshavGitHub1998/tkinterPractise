from tkinter import *
obj=Tk()
obj.title("Hello World")
#giving the title of the window
#geometry new function here , use x not * and no y !
obj.geometry("500x500+0+0")
#here comes the position and the size of the window
#focus on method pack
#creating an object for label
Lab1=Label(text='Name')
Lab1.pack()
#creating label without pack
Lab2=Label(text="City")
#not displaye ;)
#now label with foreground color and background color
Lab3=Label(text="Enrollment Number",fg='red',bg='green').pack()
Lab4=Label(text="School",fg='blue',bg='red').pack()
#note the way method pack was used
#pack is used to center align 


obj.mainloop()
#mainloop works like getch of c++ , see it running as .py
