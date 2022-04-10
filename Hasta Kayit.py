from tkinter import *
import hashlib
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser as web

baglanti = sqlite3.connect('C:\hastaneotomasyon\projee.db')
im = baglanti.cursor()

root = Tk()
root.geometry("720x480")
title = Label(text="Giriş Ekranı")
title.place(relx=.4, rely=.15)

s = 'CREATE TABLE IF NOT EXISTS hastakontrol(hastabilgisi VARCHAR(32),hastaTcKimlik VARCHAR(32),id INTEGER PRIMARY KEY AUTOINCREMENT)'
im.execute(s)
baglanti.commit()


def RandevuFonk():
    ekran = Frame(root)
    ekran.place(relwidth=.8, relheight=.9, relx=.01, rely=.01)


def yonlendir():
    pass

    web.open_new_tab("https://enabiz.gov.tr/")


'''
def Duzenle():
    duzenle=Frame(root)
    duzenle.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)
    lb1=Label(text="İstanbul Devlet Hastanemize Hoşgeldin",font="Times 20 italic")
    lb1.pack()
    btn1=Button(text="Tahlillerim",bg="Blue")
    btn1.place(x=30,y=50,width=80,height=60)
    btn2=Button(text="Ziyaretlerim",bg="Blue")
    btn2.place(x=30,y=120,width=80,height=60)
    btn3=Button(text="Hastalıklarım",bg="Blue")
    btn3.place(x=30,y=190,width=80,height=60)
    btn4=Button(text="İlaçlarım",bg="Blue")
    btn4.place(x=30,y=260,width=80,height=60)
    check = Checkbutton(text="Randevu Al")
    check.pack()
    Randevu=Button(text="Onayla",bg="Yellow",fg="White",command=RandevuFonk)
    Randevu.pack()
    akilli_asistan=Button(text="Akıllı Asistan",bg="Blue")
    akilli_asistan.place(x=30, y=330, width=80, height=60)
'''


def SeymaFonk():
    Sey = Frame(root)
    Sey.place(width=700, height=500, x=0, y=0)
    lb1 = Label(Sey, text="Lütfen Randevu türü seçiniz")
    lb1.pack()
    bt1 = Button(Sey, text="09:00")
    bt1.pack()


def DiyetisyenFonk():
    Diyet = Frame(root)
    Diyet.place(width=700, height=500, x=0, y=0)
    d1 = Button(Diyet, text="Dyt. Şeyma Gülşen Oral", bg="White", activebackground="Blue", command=SeymaFonk)
    d1.place(x=300, y=20, width=250, height=70)
    d2 = Button(Diyet, text="Uzm.Dyt. Azmi Yılmaz", bg="White", activebackground="Blue")
    d2.place(x=300, y=120, width=250, height=70)
    d3 = Button(Diyet, text="Dyt. Halime Kazmacı", bg="White", activebackground="Blue")
    d3.place(x=300, y=220, width=250, height=70)
    d4 = Button(Diyet, text="Dyt. Sinem Uygun", bg="White", activebackground="Blue")
    d4.place(x=300, y=320, width=250, height=70)


def FizFonk():
    Fiz = Frame(root)
    Fiz.place(width=1000, height=500, x=0, y=0)

    messagebox.showerror("Başlık", "Hata")


def DermaFonk():
    Derma = Frame(root)
    Derma.place(width=1000, height=500, x=0, y=0)
    Lb1 = Listbox(Derma)
    Lb1.insert(1, "Uygun doktor bulunamadı. "
                  "Daha sonra tekrar deneyiniz")

    Lb1.place(x=50, y=50, width=300)
    messagebox.showwarning("", "Uyarı")


def Duzenle(hastabilgisi,tckimlik):
    if (hastabilgisi == "" or tckimlik == ""):
        messagebox.showerror("HATA", "Kullanıcı bilgileri girilmedi !")
    else:
        # im.execute("INSERT INTO hastakontrol(hastabilgisi,hastaTcKimlik) VALUES(?,?)",
        im.execute("SELECT *  FROM hastakontrol WHERE hastabilgisi = ? and hastaTcKimlik = ?", (hastabilgisi, tckimlik))

        rows = im.fetchall()
        print(rows)

        if len(rows) < 1:
            messagebox.showwarning("Böyle bir hasta bulunamadı")
        else:

            duzenle = Frame(root)
            duzenle.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)
            lb1 = Label(text="İstanbul Devlet Hastanemize Hoşgeldin", font="Times 20 italic")
            lb1.pack()

            xresim = PhotoImage(file='img.png')
            etiket = Label(anaSayfa, image=xresim,bg="Blue")
            etiket.place(x=50, y=200)

            btn1 = Button (text="Diyetisyen", cursor="hand2", bg="Blue", command=DiyetisyenFonk)
            btn1.place(x=30, y=50, width=80, height=60)
            btn2 = Button(text="Genel Cerrahi", bg="Blue", cursor="hand2")
            btn2.place(x=30, y=120, width=80, height=60)
            btn3 = Button(text="KBB", bg="Blue", cursor="hand2")
            btn3.place(x=30, y=190, width=80, height=60)
            btn4 = Button(text="Nöroloji", bg="Blue", cursor="hand2")
            btn4.place(x=30, y=260, width=80, height=60)
            btn5 = Button(text="Psikiyatri", bg="Blue", cursor="hand2")
            btn5.place(x=150, y=50, width=80, height=60)
            btn6 = Button(text="Dahiliye", bg="Blue", cursor="hand2")
            btn6.place(x=150, y=120, width=80, height=60)
            btn7 = Button(text="Dermatoloji", bg="Blue", command=DermaFonk, cursor="hand2")
            btn7.place(x=150, y=190, width=80, height=60)
            btn8 = Button(text="Fizyoloji", bg="Blue", command=FizFonk, cursor="hand2")
            btn8.place(x=150, y=260, width=80, height=60)
            icon = PhotoImage(file='img_3.png')
            sound_btn = Button(duzenle, image=icon, width=70, height=60, relief=FLAT)
            sound_btn.place(x=100,y=100)





def kayitIslem(hastabilgisi, hastaTcKimlik):
    if hastabilgisi == "" or hastaTcKimlik == "":
        messagebox.showerror("Hata!", "Kullanıcı Adı veya Şifre Boş Girildi")

    else:
        hashedhastabilgisi = hastabilgisi
        hashedTcKimlik = hastaTcKimlik
        im.execute("INSERT INTO hastakontrol(hastabilgisi,hastaTcKimlik) VALUES(?,?)",
                   (hashedhastabilgisi, hashedTcKimlik))
        baglanti.commit()
        resulStr.set("Kullanıcı oluşturuldu")




def yeniKullanici():
    global resulStr

    yenikullanic = Frame(root)
    yenikullanic.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)

    usernameLabel = Label(yenikullanic, text="Hasta Adı Soyadı: ", font=("Arial", 13), fg="Black")
    usernameEntry = Entry(yenikullanic, width=20)
    usernameLabel.place(x=7, y=30)
    usernameEntry.place(x=150, y=34)

    TckimlikLabel = Label(yenikullanic, text="Hasta Tc Kimlik:", font=("Arial", 13))
    Tckimlik = Entry(yenikullanic, width=20, show="*")
    Tckimlik.place(x=150, y=94)
    TckimlikLabel.place(x=7, y=90)

    back = Button(yenikullanic, text="Geri Git", bg="red", fg="white", width=6,
                  command=lambda: yenikullanic.place_forget())
    back.place(x=250, y=150)

    registerButon = Button(yenikullanic, text="Kayıt Ol", width=10, fg="White", bg="Green",
                           command=lambda: kayitIslem(usernameEntry.get(), Tckimlik.get()))
    registerButon.place(x=140, y=150)

    resulStr = StringVar()
    result = Label(yenikullanic, textvariable=resulStr, font=("Arial", 17))
    result.place(x=150, y=300)


anaSayfa = Frame(root)
anaSayfa.place(relwidth=.9, relheight=.9, relx=.05, rely=.03)
usernameLabel = Label(anaSayfa, text="Hasta Adı Soyadı: ", font=("Arial", 13), fg="Black")
usernameEntry = Entry(anaSayfa, width=20)
usernameLabel.place(x=7, y=30)
usernameEntry.place(x=150, y=34)

TckimlikLabel = Label(anaSayfa, text="Hasta Tc Kimlik: ", font=("Arial", 13))
TckimlikEntry = Entry(anaSayfa, width=20, show="*")
TckimlikLabel.place(x=7, y=90)
TckimlikEntry.place(x=150, y=94)

enter = Button(anaSayfa, text="Giriş", fg="White", width=10, bg="Blue", command=lambda: Duzenle(usernameEntry.get(),TckimlikEntry.get()))
enter.place(x=250, y=150)

image = Image.open('Resim.gif')
img = image.resize((200, 200))  # boyutlandırma
resim = ImageTk.PhotoImage(img)
label = Label(image=resim)
label.place(x=400, y=30)

registerButon = Button(anaSayfa, text="Kayıt Ol", width=10, fg="White", bg="Green", command=yeniKullanici)
registerButon.place(x=140, y=150)

#region
image=Image.open('Resim.gif')
img=image.resize((200, 200)) # boyutlandırma
resim=ImageTk.PhotoImage(img)
label = Label(image=resim,bg="Black")
label.place(x=400, y=30)
#endregion

#region
xresim = PhotoImage(file='img.png')
etiket = Label(anaSayfa, image=xresim)
etiket.place(x=0,y=200)
lb=Label(text="Sana yakın uzman bul.",font=("Arial",12))
lb.place(x=70,y=390)
lb1=Label(text="Yaşadığın yere en yakın ve\n en çok yorum yapılan doktoru bul.",font=("Helvetica",8))
lb1.place(x=70,y=410)
#endregion

#region
xresimm = PhotoImage(file='img_1.png')
etikett = Label(anaSayfa, image=xresimm)
etikett.place(x=350,y=180)
lb2=Label(text="Randevu tarihini belirle ve randevunu oluştur.",font=("Arial",12))
lb2.place(x=350,y=390)
lb3=Label(text="Sana uygun olan en yakın randevu tarihi ve\n saatini belirle ve randevunu oluştur.",font=("Helvetica",8))
lb3.place(x=350,y=410)

#endregion
# CHECK BUTTON KULLAN


root.mainloop()





