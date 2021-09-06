from tkinter import *
from tkinter import colorchooser
root=Tk()
def color():
    (color := colorchooser.askcolor())
    Label(root,text='rgb:'+str(color[0])).pack()
    Label(root,text='hex'+str(color[1])).pack()
    print((color))
Button(root,text='pick color',command=color).pack()
mainloop()