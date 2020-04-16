import os ,tkinter,sys
from tkinter import *
from tkinter import messagebox
penc=Tk()
penc.title("Otomatik Kapatma")
penc.geometry("300x500")
penc.resizable(width=FALSE,height=FALSE)
var = StringVar()
label = Label( penc, textvariable=var, relief=RAISED )
def kapat(saatGir,dakikaGir):
    
    verilenSaat=int(saatGir.get())
    verilenDakika=int(dakikaGir.get())
    saat=verilenSaat*3600
    dakika=verilenDakika*60
    saniye=saat + dakika
    
    os.system("shutdown -s -t %s"%saniye)
    messagebox.showinfo("Kapatma Saati", "Bilgisayar {} saat {} dakika sonra kapanacaktır".format(verilenSaat,verilenDakika))

def manuelkapat():
    saatYaz=Label(penc)
    saatYaz.config(text="Saat Giriniz:")
    saatYaz.place(relx=0.1, rely=0.54)

    ##dakika girişi
    dakikaYaz=Label(penc)
    dakikaYaz.config(text="Dakika Giriniz :")
    dakikaYaz.place(relx=0.1,rely=0.60)

    saatGir=Entry()
    saatGir.place(relx=0.4, rely=0.54)

    dakikaGir=Entry()
    dakikaGir.place(relx=0.4,rely=0.60)
    
    ayarla=Button(text="Ayarla" ,command=lambda: kapat (saatGir,dakikaGir))
    ayarla.place(relx=0.4,rely=0.66)



    
def iptal():
    os.system("shutdown -a")#windows kapatmayı iptal etme
    messagebox.showinfo("Kapanış İptali","Bilgisayar kapanışı iptal edildi !!")

def otokapat(dakika):
    saniye=dakika*60
    os.system("shutdown -s -t %s"%saniye)
    messagebox.showinfo("Kapatma Saati", "Bilgisayar {} dakika sonra kapanacaktır".format(dakika))
var.set("Bilgisayar ne zaman kapansın ?")
label.pack()
dk10=Button(text="10 Dakika" ,command=lambda: otokapat (int(10)))
dk10.place(relx=0.4,rely=0.06)

dk30=Button(text="30 Dakika" ,command=lambda: otokapat (int(30)))
dk30.place(relx=0.4,rely=0.12)

dk60=Button(text="60 Dakika", command=lambda: otokapat (int(60)))
dk60.place(relx=0.4,rely=0.18)

dk90=Button(text="90 Dakika", command=lambda: otokapat (int(90)))
dk90.place(relx=0.4,rely=0.24)

dk120=Button(text="120 Dakika", command=lambda: otokapat (int(120)))
dk120.place(relx=0.4,rely=0.30)

dk180=Button(text="180 Dakika", command=lambda: otokapat (int(180)))
dk180.place(relx=0.4,rely=0.36)

manuel=Button(text="Manuel giriş yap" ,command=manuelkapat)
manuel.place(relx=0.35,rely=0.45)


iptalbut=Button(text="Kapatmayı Durdur", command=iptal)
iptalbut.place(relx=0.3,rely=0.91)

mainloop()
