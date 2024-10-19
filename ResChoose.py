import tkinter as tk
from tkinter import messagebox
import os.path
import csv
import Client as clt


class Choose:
    def __init__(self, file):
        if(os.path.exists(file)):
            self.root = tk.Tk()
            self.root.configure(background='#78f8e7')
            self.root.title('Choose your Restaurant here:')
            self.root.iconbitmap("client.ico")
            self.root.attributes('-alpha', 0.95)
            self.root.resizable(width=False, height=False)
            with open(file, 'r', newline='') as fil:
                reader = csv.reader(fil)
                options = [x[0] for x in reader]
            self.clicked = tk.StringVar()
            self.clicked.set(options[0])
            self.optbox = tk.OptionMenu(self.root, self.clicked, *options)
            self.optbox.configure(font = ("Helvetica", 36))
            self.optbox.configure(bg='#f87878')
            self.optbox.configure(activebackground='#78f8e7')
            menu = self.root.nametowidget(self.optbox.menuname)
            menu.config(font=("Helvetica", 30))
            menu.config(bg='#78f884')
            self.optbox.grid(row=0, column=0, sticky="nsew")
            tk.Button(self.root, text="Let's Eat Here!", bg="#33ffbb", activebackground="#00ffaa", command=self.get_res, font =("Helvetica", 30, "bold")).grid(row=1, column=0, sticky="nsew")
        else:
            messagebox.showerror("File Error", "No Restaurants found, first sign up a restaurant")
    def get_res(self):
        self.root.destroy()
        login = clt.Log(self.clicked.get())
        login.run()
    def run(self):
        self.root.mainloop()

a = Choose("admin.csv")
a.run()