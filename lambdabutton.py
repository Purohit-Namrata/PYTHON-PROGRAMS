from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the window geometry
win.geometry("750x250")

#Display a Label
def print_text(text):
   Label(win, text=text,font=('Helvetica 13 bold')).pack()

btn1= ttk.Button(win, text="Button1" ,command= lambda:
print_text("Button 1"))
btn1.pack(pady=10)

win.mainloop()


