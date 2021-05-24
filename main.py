from tkinter import *
from PIL import Image,ImageTk
root=Tk()
def start():
    import demo


root.geometry("777x888")
load=Image.open("gtn image1.jpg")
render=ImageTk.PhotoImage(load)
img=Label(image=render)
img.image=render
img.place(x=0,y=0)
msg=Label(root,text="You have to guess the number in the range of 0 to 10")
msg.pack()



button=Button(root,text="Start",command=start)
button.pack()



root.mainloop()
