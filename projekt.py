import tkinter as tk
import os

def spremi_biljesku():
    biljeska = unos.get()
    if biljeska:
        with open("biljeske.txt", "a", encoding="utf-8") as f:
            f.write(biljeska + "\n")
        unos.delete(0, tk.END)
        status.config(text="Bilješka spremljena!", fg="green")
    else:
        status.config(text="Unesite bilješku!", fg="red")

def prikazi_biljeske():
    if os.path.exists("biljeske.txt"):
        with open("biljeske.txt", "r", encoding="utf-8") as f:
            sadrzaj = f.read()
        prikaz.delete("1.0", tk.END)
        prikaz.insert(tk.END, sadrzaj)
    else:
        prikaz.delete("1.0", tk.END)
        prikaz.insert(tk.END, "Nema spremljenih bilješki.")

prozor = tk.Tk()
prozor.title("Bilježnica")
prozor.geometry("400x300")

tk.Label(prozor, text="Unesi bilješku:").pack(pady=5)
unos = tk.Entry(prozor, width=40)
unos.pack(pady=5)

tk.Button(prozor, text="Spremi", command=spremi_biljesku).pack(pady=5)
tk.Button(prozor, text="Prikaži sve", command=prikazi_biljeske).pack(pady=5)

status = tk.Label(prozor, text="", fg="green")
status.pack()

prikaz = tk.Text(prozor, height=10, width=45)
prikaz.pack(pady=10)

prozor.mainloop()
