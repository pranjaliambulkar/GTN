from tkinter import *
from random import *
root=Tk()
root.geometry("444x555")
number=Entry(root)
number.pack()
def check():
    if int(number.get(1,10)) == 1:
        msg = Label(root, text="Yyou have to guess the number in the range of 0 to 10")
        msg.pack()

button=Button(root,text="submit",command=check)
button.pack()

root.mainloop()


