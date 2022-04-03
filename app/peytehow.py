#!/usr/bin/env python3
#-*-coding:utf-8-*-


##### LICENSE !!!!!

# Copyright (C) 2021-22 Muhammed Abdurrahman (MuKonqi)

# You just DO WHAT THE FUCK YOU WANT TO.
# Sadece NE HALT EDERSEN ET.


### Import Tkinter library: / Tkinter kütüphanesini ekle:
from tkinter import *
from tkinter import messagebox
### Import 'os' module: / 'os' modülünü ekle:
import os


### Main:/Ana:

# Create main window: / Ana pencereyi oluştur:
window=Tk()
# Relabel main window: / Ana pencereyi yeniden adlandır:
window.title("peytehow")
# Configre main window: / Ana pencereyi özelleştir:
window.geometry("600x600")
window.config(background="#000000")
window.resizable(0, 0)

# Create menu: / Menü oluştur:
menu1=Menu(window)
# Mount menu: / Menüyü bağla:
window.config(menu=menu1)
# Configre menu: / Menüyü özelleştir:
about=Menu(menu1, tearoff=0)
menu1.add_cascade(label="File / Dosya",menu=about)
about.add_command(label="Quit / Çıkış", command=window.quit)

# Create first text: / Birinci metni oluştur:
txt1=Label(window)
# Configre first text: / Birinci metni özelleştir:
txt1.config(font="arial 20 bold", background="#000000", foreground="#FFFFFF", text="\n\nMerhaba dünya!\nHello world!\n\n")

# License: / License:
def open_license():
    os.system("xdg-open http://www.wtfpl.net/txt/copying/")
    messagebox.showinfo("Warning","The link has been opened.\nBağlantı açılmıştır.")

# License link: / Lisans bağlantısı:
def copy_license_url():
    window.clipboard_append("http://www.wtfpl.net/txt/copying/")
    window.update()
    messagebox.showinfo("Warning","The link has been copied.\nBağlantı kopyalanmıştır.")

# License: / Lisans:
def license():
    # Create third window: / Üçüncü pencereyi oluştur:
    window3=Toplevel()
    # Configre third window: / Üçüncü pencereyi özelleştir:
    window3.title("License")
    window3.config(background="#000000")
    window3.resizable(0, 0)

    # Create and configre new text: / Yeni metni oluştur ve ayarla:
    txt1_w3=Label(window3)
    txt1_w3.config(font="arial 8 bold", background="#000000", foreground="#FFFFFF", text="\nDO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE\nVersion 2, December 2004\n\nCopyright (C) 2004 Sam Hocevar <sam@hocevar.net>\n\nEveryone is permitted to copy and distribute verbatim or modified\ncopies of this license document, and changing it is allowed as long\ncopies of this license document, and changing it is allowed as long\n\nDO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE\nTERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION\n\n0. You just DO WHAT THE FUCK YOU WANT TO.\n")
    txt1_w3.pack()

    # Create and configre new button: / Yeni butonu oluştur ve ayarla:
    btn1_w3=Button(window3)
    btn1_w3.config(cursor="hand2", activebackground="#000000", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="1", text="Copy license link\nLisans bağlantısını kopyala", font="Arial 8 bold", command=copy_license_url)
    btn1_w3.pack()

    # For Unix-like: / Unix-benzeri için:
    # Operating System control: / İşletim Sistemi kontrolü:
    if os.name == "posix":
        # Create and configre new button: / Yeni butonu oluştur ve ayarla:
        btn2_w3=Button(window3)
        btn2_w3.config(cursor="hand2", activebackground="#000000", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="1", text="Open license\nLisansı aç", font="Arial 8 bold", command=open_license)
        btn2_w3.pack()

# About: / Hakkında:
def about():
    # Create second window: / İkinci pencereyi oluştur:
    window2=Toplevel()
    # Configre second window: / İkinci pencereyi özelleştir:
    window2.title("About")
    window2.config(background="#000000")
    window2.resizable(0, 0)

    # # Create and configre new text: / Yeni metni oluştur ve ayarla:
    # txt1_w2=Label(window2)
    # txt1_w2.config(font="arial 8 bold", background="#000000", foreground="#FFFFFF", text="This program is a hello world style application made using Tkinter with Python3 and this program is free software.\nLicense: GNU GPL 3.0\nDeveloper: androidprotmmas (Muhammed Abdurrahman)\n\nBu program Python3 ile Tkinter kullanılarak yapılmış merhaba dünya tarzı bir uygulamadır ve bu program özgür yazılımdır.\nLisans: GNU GPL 3.0\nGeliştirici: MuKonqi (Muhammed Abdurrahman)\n")
    # txt1_w2.pack()
    
    # Create copy links: / Linkleri kopyalamayı oluştur:
    def peytehowlink():
        window2.clipboard_clear()
        window2.update()
        window2.clipboard_append("https://github.com/MuKonqi/peytehow")
        window2.update()
        messagebox.showinfo("Warning","The link has been copied.\nBağlantı kopyalanmıştır.")
    def fosslink():
        window2.clipboard_clear()
        window2.update()
        window2.clipboard_append("https://www.gnu.org/philosophy/free-sw.tr.html")
        window2.update()
        messagebox.showinfo("Warning","The link has been copied.\nBağlantı kopyalanmıştır.")
    def developerlink():
        window2.clipboard_clear()
        window2.update()
        window2.clipboard_append("https://mukonqi.github.io")
        window2.update()
        messagebox.showinfo("Warning","The link has been copied.\nBağlantı kopyalanmıştır.")
    
    # For Unix-like: / Unix benzeri için:    
    # Create open links: / Linkleri açmayı oluştur
    def peytehowopen():
        if os.name == "posix":
            os.system("xdg-open https://github.com/MuKonqi/peytehow")
            messagebox.showinfo("Warning","The link has been opened.\nBağlantı açılmıştır.")
        else:
            peytehowlink()
    def fossopen():
        if os.name == "posix":
            os.system("xdg-open https://www.gnu.org/philosophy/free-sw.tr.html")
            messagebox.showinfo("Warning","The link has been opened.\nBağlantı açılmıştır.")
        else:
            fosslink()
    def developeropen():
        if os.name == "posix":
            os.system("xdg-open https://mukonqi.github.io")
            messagebox.showinfo("Warning","The link has been opened.\nBağlantı açılmıştır.")
        else:
            developerlink()

    # Create butons but like texts: / Butonlar ama metinlere benzeyenleri oluştur:
    space1_w2=Label(window2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 7")
    space1_w2.pack()
    btn1_w2=Button(window2, font="arial 15 bold italic", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="peytehow\nHello world style application made using Tkinter with Python3.\nPython3 ile Tkinter kullanılarak yapılmış 'Merhaba dünya!' tarzı uygulama.", command=peytehowopen)
    btn1_w2.pack()
    space2_w2=Label(window2, background="#000000", foreground="#FFFFFF", text="\n", font="arial 1")
    space2_w2.pack()    
    btn2_w2=Button(window2, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="Source code: Free and Open Source Software (FOSS)\nKaynak kod: Özgür ve Açık Kaynaklı Yazılım (FOSS)", command=fossopen)
    btn2_w2.pack()
    btn3_w2=Button(window2, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="Developer: Muhammed Abdurrahman (MuKonqi)\nGeliştirici: Muhammed Abdurrahman (MuKonqi)", command=developeropen)
    btn3_w2.pack()
    btn4_w2=Button(window2, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="License: WTFPL\nLisans: WTFPL", command=license)
    btn4_w2.pack()

# Create button: / Butonu oluştur:
btn1=Button(window)
# Configre button: / Butonu özelleştir:
btn1.config(cursor="hand2", activebackground="#000000", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="1", text="About\nHakkında", font="Arial 9 bold", command=about)

# Create button: / Butonu oluştur:
btn2=Button(window)
# Configre button: / Butonu özelleştir:
btn2.config(cursor="hand2", activebackground="#0000FF", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="3", text="OK!\nTamam!", font="Arial 10 bold", command=window.quit)

# If "c_btn1" clicked: / Eğer 'c_btn1' tıklandıysa:
def c_btn1_clicked():
    print("Check button is clicked.\nOnay butonu tıklandı.\n")
    messagebox.showinfo("Info","Check button is clicked.\nOnay butonu tıklandı.")

# Create and configre new text: / Yeni metni oluştur ve özelleştir:
s_txt1=Label(window, background="#000000", foreground="#FFFFFF", text="\n\n\n")

# Create and configre check button: / Onay butonunu oluştur ve özelleştir:
c_btn1=Checkbutton(text="Let's click!\nHaydi tıkla!", cursor="hand2", activebackground="red", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="0", command=c_btn1_clicked)

# Create and setup list box: / Liste kutusunu oluştur ve ayarla:
list=Listbox(window, background="#FFFFFF")
list_=["Python","Tkinter","Hello world!"]
for i in list_:
    list.insert(END, i)

# Create and configre new text: / Yeni metni oluştur ve özelleştir:
s_txt2=Label(window, background="#000000", foreground="#FFFFFF", text="\n\n\n")

# Fixing to window: / Pencereye sabitleme:
btn1.pack()
txt1.pack()
btn2.pack()
s_txt1.pack()
c_btn1.pack()
s_txt2.pack()
list.pack()

# Start endless loop: / Sonsuz döngüyü başlat:
print("Starting endless loop and software...\nSonsuz döngü ile yazılım başlatılıyor...\n")
mainloop()

# Stop endless loop and software: / Sonsuz döngü ile yazılımı durdur:
print("Stopping endless loop and software...\nSonsuz döngü ile yazılım sonlandırılıyor...")
