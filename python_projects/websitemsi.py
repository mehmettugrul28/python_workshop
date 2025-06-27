import tkinter as tk
import webbrowser

def siteye_git():
    url = entry.get()
    if not url.startswith("http"):
        url = "https://" + url
    webbrowser.open(url)

# Arayüz
pencere = tk.Tk()
pencere.title("Mini Web Tarayıcı")
pencere.geometry("400x120")

etiket = tk.Label(pencere, text="Gitmek istediğiniz site:")
etiket.pack(pady=5)

entry = tk.Entry(pencere, width=50)
entry.pack(pady=5)

buton = tk.Button(pencere, text="Git", command=siteye_git)
buton.pack(pady=5)

pencere.mainloop()
