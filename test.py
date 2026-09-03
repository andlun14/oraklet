import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Change Text Color - Approach 3")

style = ttk.Style()
style.configure("TLabel", foreground="blue", font=("Helvetica", 16))

label = ttk.Label(root, text="Hello GeeksforGeeks", style="TLabel")
label.pack(pady=20)

root.mainloop()