#!/usr/bin/env python3
#-*-coding:utf-8-*-


##### LICENSE !!!!!

#Copyright (C) 2021, Muhammed Abdurrahman

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.


### Import Tkinter library: / Tkinter kütüphanesini ekle:
from tkinter import *
from tkinter import messagebox
### Import 'os' module: / 'os' modülünü ekle:
import os

### Main:/Ana:

# Create main window: / Ana pencereyi oluştur:
window=Tk()
# Relabel main window: / Ana pencereyi yeniden adlandır:
window.title("Hi.")
# Configre main window: / Ana pencereyi özelleştir:
window.geometry("400x400")
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
    os.system("xdg-open https://www.gnu.org/licenses/gpl-3.0.txt")
    messagebox.showinfo("Warning","The link has been opened.\nBağlantı açılmıştır.")

# License link: / Lisans bağlantısı:
def copy_license_url():
    window.clipboard_append("https://www.gnu.org/licenses/gpl-3.0.txt")
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
    txt1_w3.config(font="arial 8 bold", background="#000000", foreground="#FFFFFF", text="\nCopyright (C) 2021, Muhammed Abdurrahman\n\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nThis program is distributed in the hope that it will be useful\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see <https://www.gnu.org/licenses/>.\n\nFull license: https://gnu.org/license/gpl3.txt\nLisansın tamamı: https://gnu.org/license/gpl3.txt\n")
    txt1_w3.pack()

    # For Unix-like: / Unix-benzeri için:
    # Operating System control: / İşletim Sistemi kontrolü:
    if os.name == "posix":
        # Create and configre new button: / Yeni butonu oluştur ve ayarla:
        btn1_w3=Button(window3)
        btn1_w3.config(cursor="hand2", activebackground="#000000", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="1", text="Open license\nLisansın tamamını aç", font="Arial 8 bold", command=open_license)
        btn1_w3.pack()

    # Create and configre new button: / Yeni butonu oluştur ve ayarla:
    btn2_w3=Button(window3)
    btn2_w3.config(cursor="hand2", activebackground="#000000", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="1", text="Copy license link\nLisans bağlantısını kopyala", font="Arial 8 bold", command=copy_license_url)
    btn2_w3.pack()

# About: / Hakkında:
def about():
    # Create second window: / İkinci pencereyi oluştur:
    window2=Toplevel()
    # Configre second window: / İkinci pencereyi özelleştir:
    window2.title("About")
    window2.config(background="#000000")
    window2.resizable(0, 0)

    # Create and configre new text: / Yeni metni oluştur ve ayarla:
    txt1_w2=Label(window2)
    txt1_w2.config(font="arial 8 bold", background="#000000", foreground="#FFFFFF", text="This program is a hello world style application made using Tkinter with Python3 and this program is free software.\nLicense: GNU GPL 3.0\nDeveloper: androidprotmmas (Muhammed Abdurrahman)\n\nBu program Python3 ile Tkinter kullanılarak yapılmış merhaba dünya tarzı bir uygulamadır ve bu program özgür yazılımdır.\nLisans: GNU GPL 3.0\nGeliştirici: androidprotmmas (Muhammed Abdurrahman)\n")
    txt1_w2.pack()
    
    #Create and configre new button: / Yeni butonu oluştur ve ayarla:
    btn1_w2=Button(window2)
    btn1_w2.config(cursor="hand2", activebackground="#000000", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="1", text="License\nLisans", font="Arial 8 bold", command=license)
    btn1_w2.pack()

# Create button: / Butonu oluştur:
btn1=Button(window)
# Configre button: / Butonu özelleştir:
btn1.config(cursor="hand2", activebackground="#000000", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="1", text="Hakkında\nAbout", font="Arial 9 bold", command=about)

# Create button: / Butonu oluştur:
btn2=Button(window)
# Configre button: / Butonu özelleştir:
btn2.config(cursor="hand2", activebackground="#0000FF", activeforeground="#FFFFFF", background="#FFFFFF", borderwidth="3", text="Tamam!\nOkey!", font="Arial 10 bold", command=window.quit)

# Fixing to window: / Pencereye sabitleme:
btn1.pack()
txt1.pack()
btn2.pack()

# Start endless loop: / Sonsuz döngüyü başlat:
print("Starting endless loop and software...\nSonsuz döngü ile yazılım başlatılıyor...\n")
mainloop()

# Stop endless loop and software: / Sonsuz döngü ile yazılımı durdur:
print("Stopping endless loop and software...\nSonsuz döngü ile yazılım sonlandırılıyor...")
