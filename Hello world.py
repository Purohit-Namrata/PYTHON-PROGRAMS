'''from tkinter import *
  
root = Tk() 
a = Label(root, text ="Hello World")


a.pack() 
  
root.mainloop() 







from tkinter import *

root=Tk()

root.title("Welcome")

root.geometry('350x500')

root.mainloop()

'''

from tkinter import *
root=Tk()

root.title('Welcome')
root.geometry('350x200')

menu=Menu(root)
item=Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File',menu=item)
root.config(menu=menu)

lbl=Label(root,text="How are you?")
lbl.grid()

#function to display text when button is clicked
def clicked():
    res='You wrote'+txt.get()
    lbl.configure(text=res)

btn= Button(root, text='Click me', fg='RED', command=clicked)
btn.grid(column=2, row=0)

txt=Entry(root, width=10)
txt.grid(column=1,row=0)

Button(root, text="Quit", command=root.destroy).pack()     
root.mainloop()



