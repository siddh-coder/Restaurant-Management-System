import tkinter as tk
from tkinter import messagebox
import os.path
import csv
import random

class Summary:
    def __init__(self, data, username, menu):
        self.root = tk.Tk()
        self.menu_list=menu
        self.root.configure(background='#ede8d0')
        self.root.title("Your Order Summary:")
        self.root.iconbitmap("client.ico")
        self.root.attributes('-alpha', 0.95)
        self.root.resizable(width=False, height=False)
        self.data = data
        self.username = username
        tk.Label(self.root, text = f"Date: {self.data[0]}", font=('Segoe Print', 12)).grid(row=0, column=0,sticky="nsew")
        tk.Label(self.root, text = f"Time: {self.data[1]}", font=('Segoe Print', 12)).grid(row=1, column=0,sticky="nsew")
        c=2
        for i in range(len(self.menu_list)):
            if(self.data[i+3]!=0):
                c+=1
                tk.Label(self.root, text = f"{self.menu_list[i]}: {self.data[i+3]}", font=('Segoe Print', 12)).grid(row=c, column=0,sticky="nsew")
        tk.Label(self.root, text = f"Total: {self.data[2]}", font=('Segoe Print', 12)).grid(row=c+1, column=0,sticky="nsew")
        tk.Button(self.root, text = "I don't want to order more!", command=self.ok, font=('Segoe Print', 16, "bold")).grid(row=c+2, column=0,sticky="nsew")
        tk.Button(self.root, text = "I want to order More!", command=self.cancel, font=('Segoe Print', 16, "bold")).grid(row=c+3, column=0,sticky="nsew")
  
    def run(self):
        self.root.mainloop()
        
    def ok(self):
        existing_data=[]
        order_id=""
        for x in range(5):
            order_id+=str(random.choice([1,2,3,4,5,6,7,8,9,0]))
        self.data.append(order_id)
        if os.path.exists(f"{self.username}_orders.csv"):
            with open(f"{self.username}_orders.csv", 'r', newline='') as file:
                reader = csv.reader(file)
                existing_data = list(reader)  # Read existing rows
            # Write the new data at the first row and then the existing data
            with open(f"{self.username}_orders.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.data)  # Write new data at the first row
                writer.writerows(existing_data)  # Write the rest of the existing data
        else:
            with open(f"{self.username}_orders.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.data)  # Write new data at the first row
        messagebox.showinfo("Order information", "Your order has been placed successfully.")
        self.root.destroy()
    def cancel(self):
        self.root.destroy()