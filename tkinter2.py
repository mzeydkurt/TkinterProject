from tkinter import *

window = Tk()
window.title("tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=30,pady=30)

label = Label(text="my Label")
label.config(bg="black")
label.config(fg="white")
label.config(pady=10,padx=10)
label.pack()

def botton_clicked():
    print("Button Clicked")
    print(entry.get())
    print(text.get("1.0",END))

button = Button(text="Button",command=botton_clicked)
button.config(bg="red")
button.config(fg="black")
button.config(padx=5,pady=5)
button.pack()

entry = Entry(width=20)
entry.pack()

text =Text(width=20,height=20)
text.focus()
text.pack()
#scale
def scale_selected(value):
    print(value)
scale = Scale(from_=0,to=50,command=scale_selected)
scale.pack()

def spinbox_selected():
    print(spibox.get())


spibox = Spinbox(from_=0, to=50, command=spinbox_selected)
spibox.pack()
def chechk_button():
    print(chechk_state.get())

chechk_state = IntVar()
check = Checkbutton(text="Checjk",variable=chechk_state,command=chechk_button())
check.pack()

def radio_selected():
    print(radio_checked_state.get())
radio_checked_state = IntVar()
radiobutton1 = Radiobutton(text="option1",value=10,variable=radio_checked_state,command=radio_selected)
radiobutton2 = Radiobutton(text="option2",value=20,variable=radio_checked_state,command=radio_selected)
radiobutton1.pack()
radiobutton2.pack()

#listbox
listbox = Listbox()
name_lisst = ["ali","ahmet","musa"]
for i in range(len(name_lisst)):
    listbox.insert(i,name_lisst[i])

listbox.pack()

window.mainloop()


