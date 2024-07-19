from tkinter import *

pencere = Tk()
pencere.geometry('700x700')
def yazdir():
    print("Button One Is Ready")


pencere.title("BTK Academy Python Course")
buton =  Button(text = "Button One", fg="orange", bg = "green", command= yazdir) # front / background color
buton2 =  Button(text = "Button Two", fg="orange", bg = "blue") # front / background color
buton3 =  Button(text = "Button Three", fg="orange", bg = "green") # front / background color




buton.pack(side = LEFT)
buton2.pack()
buton3.pack(side = RIGHT)


yazi = Label(pencere, text = "WELCOME", font = ("Times New Roman", 20))
yazi.pack()




pencere.mainloop()  # pencerenin sürekli tekrarlaması için sonsuz döngüye alıyoruz / kodun en altında olacak.
