from tkinter import *
def bmi_hesaplama():
    try:
        boy_cm = float(entry2.get())
        boy = boy_cm/100
        kilo = float(entry1.get())
        bmi = kilo / (boy * boy)
        if bmi < 18.5:
            kategori = "zayıfsınız"
        elif 18.5<= bmi <= 24.9:
            kategori = "Sağlıklısınız"
        elif 25 <= bmi <= 29.9:
            kategori = "Fazla Kilolusunuz"
        elif 30 <= bmi <= 34.9:
            kategori = "1. derece obezsiniz"
        elif 35 <= bmi <= 39.9:
            kategori = "2. derece obezsiniz"
        else:
            kategori = "3. derece obezsiniz"

        result_label.config(text=f"Senin BMİ : {bmi:.2f} \n Kategoriniz : {kategori} ")
    except ValueError:
        result_label.config(text="Tekrar Deneyiniz")
#BMİ HESAPLAMA
window = Tk()
window.title("BMİ CALCULATOR")
window.minsize(width=300,height=200)

label1 = Label(window,text="Enter Your Weight [KG]",bg="blue",padx=6,pady=6)
label1.pack()

entry1 = Entry()
entry1.pack()

label2 = Label(window,text="Enter Your Height [CM]",bg="blue",padx=6,pady=6)
label2.pack()

entry2 = Entry(window)
entry2.pack()

button = Button(window,text="Hesapla",command=bmi_hesaplama)
button.pack()

result_label = Label(window,text="",bg="white")
result_label.pack()

window.mainloop()