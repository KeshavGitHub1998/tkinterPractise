from tkinter import *
obj=Tk()
obj.title("Hello World")
#giving the title of the window
#geometry new function here , use x not * and no y !
obj.geometry("500x500+0+0")
#here comes the position and the size of the window
obj.mailloop()
#mainloop works like getch of c++ , see it running as .py
