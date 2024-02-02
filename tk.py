from tkinter import *

def red():
    label.config(text="Red")
    entry.delete(0,END)
    entry.insert(index=0,string="#ff050d")
def blue():
    label.config(text="Blue")
    entry.delete(0,END)
    entry.insert(index=0,string="#1520A6")
def green():
    label.config(text="Green")
    entry.delete(0,END)
    entry.insert(index=0,string="#008000")
def yellow():
    label.config(text="Yellow")
    entry.delete(0,END)
    entry.insert(index=0,string="#FFFF00")
def purple():
    label.config(text="Purple")
    entry.delete(0,END)
    entry.insert(index=0,string="#B200ED")
def orange():
    label.config(text="Orange")
    entry.delete(0,END)
    entry.insert(index=0,string="#ff5100")
def aqua():
    label.config(text="Aqua")
    entry.delete(0,END)
    entry.insert(index=0,string="#00ffff")
def pink():
    label.config(text="Pink")
    entry.delete(0,END)
    entry.insert(index=0,string="#ffc0cb")
def lime():
    label.config(text="Lime")
    entry.delete(0,END)
    entry.insert(index=0,string="#00ff00")
def silver():
    label.config(text="Silver")
    entry.delete(0,END)
    entry.insert(index=0,string="#cccccc")


root=Tk()
root.title("Color Picker")
root.geometry("180x500")

label=Label(root,anchor='c')
label.pack()

entry=Entry(root,justify='center',bd=5)
entry.pack()

buttonRed=Button(root,width=16,bg='#ff050d',fg='white',command=red)
buttonRed.pack()

buttonBlue=Button(root,width=16,bg='#1520A6',fg='white',command=blue)
buttonBlue.pack()

buttonGreen=Button(root,width=16,bg='#008000',fg='white',command=green)
buttonGreen.pack()

buttonYellow=Button(root,width=16,bg='#FFFF00',fg='white',command=yellow)
buttonYellow.pack()

buttonOrange=Button(root,width=16,bg='#ff5100',fg='white',command=orange)
buttonOrange.pack()

buttonPurple=Button(root,width=16,bg='#B200ED',fg='white',command=purple)
buttonPurple.pack()

buttonAqua=Button(root,width=16,bg='#00ffff',fg='aqua',command=aqua)
buttonAqua.pack()

buttonPink=Button(root,width=16,bg='#ffc0cb',fg='pink',command=pink)
buttonPink.pack()

buttonLime=Button(root,width=16,bg='#00ff00',fg='lime',command=lime)
buttonLime.pack()

buttonSilver=Button(root,width=16,bg='#cccccc',fg='silver',command=silver)
buttonSilver.pack()






root.mainloop()