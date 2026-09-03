import tkinter as tk

def ändra_text():
    etikett.config(text="Du klickade!")

root = tk.Tk()
root.title("Komplett")
root.geometry("400x300")

etikett = tk.Label(root, text="Ingenting har hänt än.", font=("Arial", 16))
etikett.pack(pady=40)

knapp = tk.Button(root, text="Klicka mig", command=ändra_text, padx=20, pady=10)
knapp.pack()

root.mainloop()
