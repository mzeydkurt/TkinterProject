import tkinter
window = tkinter.Tk()
window.title("Tkinter")
window.minsize(width=400,height=400)

def click_Button():
    user_input = my_Entry.get()
    print(user_input)





#LABEL

my_Label = tkinter.Label(text="This is a Label",font=('Ariel',30,'italic'))
my_Label.config(bg="black",fg="white")
#my_Label.pack(side="left")
my_Label.grid(row=2,column=0)

#Button

my_Button = tkinter.Button(text="this is a Button",command=click_Button)
my_Button.grid(row=1,column=0)

#Entry

my_Entry = tkinter.Entry(width=20)






window.mainloop()