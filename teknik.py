import tkinter as tk
import pyperclip

def copy_text(event=None):
    pyperclip.copy("Teknik ekibe iletildi")
    status_label.config(text="Metin kopyalandı!")

# Ana pencere oluşturma
root = tk.Tk()
root.title("Teknik Ekip Mesajı")

# Pencere boyutunu ve konumunu ayarlama
root.geometry("300x100+200+200")

# Kopyalama butonu
copy_button = tk.Button(root, text="Teknik Ekibe İletildi Mesajını Kopyala", command=copy_text)
copy_button.pack(pady=20)

# Durum etiketi
status_label = tk.Label(root, text="")
status_label.pack()

# Boşluk tuşuna basıldığında copy_text fonksiyonunu çağır
root.bind('<space>', copy_text)

# Pencere açıldığında otomatik olarak odaklan
root.focus_force()

# Uygulamayı çalıştırma
root.mainloop()