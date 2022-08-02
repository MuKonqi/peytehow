#!/usr/bin/env python3
#-*-coding:utf-8-*-


##### LICENSE !!!!!

# Copyright (C) 2021-22 Muhammed Abdurrahman (MuKonqi)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
peytehow=Menu(menu1, tearoff=0)

# Create first text: / Birinci metni oluştur:
txt1=Label(window)
# Configre first text: / Birinci metni özelleştir:
txt1.config(font="arial 20 bold", background="#000000", foreground="#FFFFFF", text="\nMerhaba dünya!\nHello world!\n")

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
    txt1_w3.config(font="arial 10 bold", background="#000000", foreground="#FFFFFF", text='\n\nCopyright 2021-22 Muhammed Abdurrahman\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\nhttp://www.apache.org/licenses/LICENSE-2.0\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n\n')
    txt1_w3.pack()
    
    # Open license: / Lisansı aç:
    def open_license():
        os.system("xdg-open http://www.apache.org/licenses/LICENSE-2.0")
        messagebox.showinfo("Warning","The link has been opened.\nBağlantı açılmıştır.")

    # Copy license link: / Lisans bağlantısını kopyala:
    def copy_license_url():
        window3.clipboard_clear()
        window3.update()
        window3.clipboard_append("http://www.apache.org/licenses/LICENSE-2.0")
        window3.update()

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
    btn4_w2=Button(window2, font="arial 12 bold", cursor="hand2", activeforeground="#0099FF", activebackground="#000000", background="#000000", foreground="#FFFFFF", text="License: Apache 2.0\nLisans: Apache 2.0", command=license)
    btn4_w2.pack()

# Create button: / Butonu oluştur:
btn1=Button(window)
# Configre button: / Butonu özelleştir:
btn1.config(cursor="hand2", activebackground="#0000FF", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="3", text="OK!\nTamam!", font="Arial 10 bold", command=window.quit)

# If "c_btn1" clicked: / Eğer 'c_btn1' tıklandıysa:
def c_btn1_clicked():
    print("Check button is clicked.\nOnay butonu tıklandı.\n")
    messagebox.showinfo("Info","Check button is clicked.\nOnay butonu tıklandı.")

# Create and configre new text: / Yeni metni oluştur ve özelleştir:
s_txt1=Label(window, background="#000000", foreground="#FFFFFF", text="\n")

# Create and configre check button: / Onay butonunu oluştur ve özelleştir:
c_btn1=Checkbutton(text="Let's click!\nHaydi tıkla!", cursor="hand2", activebackground="red", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="0", command=c_btn1_clicked)

# Add and setup entry widget and its def: / Girişi ve onun def'ini ekle ve ayarla:
def def_entry():
    entry2=entry1.get()
    print("I write: "+entry2)
    messagebox.showinfo("What did I write?",entry2)
entry1=Entry(window)
e_btn1=Button(cursor="hand2", activebackground="#0000FF", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="3", text="What did I write?\nBen ne yazdım?", font="Arial 10 bold", command=def_entry)

# Create and configre new text: / Yeni metni oluştur ve özelleştir:
s_txt2=Label(window, background="#000000", foreground="#FFFFFF", text="\n\n\n")

# Create and setup list box: / Liste kutusunu oluştur ve ayarla:
list=Listbox(window, background="#FFFFFF")
list_=["Python","Tkinter","Hello world!"]
for i in list_:
    list.insert(END, i)

# Create and configre new text: / Yeni metni oluştur ve özelleştir:
s_txt3=Label(window, background="#000000", foreground="#FFFFFF", text="\n\n\n")

# Fixing to window: / Pencereye sabitleme:
txt1.pack()
btn1.pack()
s_txt1.pack()
c_btn1.pack()
s_txt2.pack()
entry1.pack()
e_btn1.pack()
s_txt3.pack()
list.pack()

# Congigre menu: / Menüyü özelleştir:
menu1.add_cascade(label="peytehow",menu=peytehow)
peytehow.add_command(label="About / Hakkında", command=about)
peytehow.add_command(label="License / Lisans", command=license)

# Start endless loop: / Sonsuz döngüyü başlat:
print("Starting endless loop and software...\nSonsuz döngü ile yazılım başlatılıyor...\n")
mainloop()

# Stop endless loop and software: / Sonsuz döngü ile yazılımı durdur:
print("Stopping endless loop and software...\nSonsuz döngü ile yazılım sonlandırılıyor...")
