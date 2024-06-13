'''import tkinter
m = tkinter.Tk()
'''
#widgets are added here
'''
m.mainloop()



import tkinter
#m=tkinter.Tk()

m=tkinter.Tk(screenName=None,  baseName=None,  className="WELCOMEGUI",  useTk=1)
m.mainloop()



from tkinter import *
root=Tk()
root.title("Welcome")
root.geometry("350x400")
lbl=Label(root,text="Hello, how are you?")
lbl.grid()



def clicked():
    #lbl.configure(text=' I just got clicked ' )
    lbl1=Label(root,text="I just got clicked")
    lbl1.grid(column=3, row=4)

btn=Button(root, text="Click me", fg='red', command=clicked)
btn.grid(column=2, row=0)

root.mainloop()
'''






from tkinter import *

root=Tk()
root.title("Welcome")
root.geometry('350x400')

lbl=Label(root, text="Hello, how are you?")
lbl.grid()

menu=Menu(root)
item=Menu(menu)
item.add_command(label="New")
menu.add_cascade(label='File',men=item)
root.config(menu=menu)


txt=Entry(root, width=10)
txt.grid(column=1,row=0)

def clicked():
    res="You wrote " + txt.get()
    #lbl.configure(text=res)
    lbl1=Label(text=res)
    lbl1.grid(column=2,row=4)
 
btn=Button(root, text='Click me',fg='red', command=clicked)
btn.grid(column=2,row=0)

root.mainloop()





















