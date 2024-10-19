import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Order as ord
from datetime import datetime
import os.path
import csv

class Guest:
    def __init__(self, typ, restaurant):
        # Create the main window
        self.root = tk.Tk()
        self.root.configure(background='#ede8d0')
        self.root.iconbitmap("client.ico")
        self.root.title("Choose your items here by increasing the counter:")
        self.root.attributes('-alpha', 0.95)
        self.root.geometry("1250x600")  # Set initial window size
        self.root.resizable(width=False, height=False)
        self.min = tk.PhotoImage(file='minus.png')
        self.plu = tk.PhotoImage(file='plus.png')
        self.username = typ
        
        # Current category tracking
        self.current_category = tk.StringVar(value="Starters")
        self.counters = []
        
        # Create the main frame for dynamic content
        self.main_frame = tk.Frame(self.root, bg='#d2fbd0')
        self.main_frame.grid(row=0, column=1, sticky='nsew')
        
        # Create bottom frame for total price and next button
        self.bottom_frame = tk.Frame(self.root, bg='green', height=50)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, sticky='ew')
        
        # Create left menu frame
        self.left_frame = tk.Frame(self.root, bg='#ede8d0', width=200, height=600)
        self.left_frame.grid(row=0, column=0, sticky=tk.EW)
        
        #User Button
        if(typ != "_Guest_"):
            user_button = tk.Button(self.left_frame, text = typ, bg = 'darkblue' , fg = 'yellow', font = ('serif', 20, 'bold'), command = self.userbutton)
            user_button.grid(row=0, column=0, sticky = tk.EW)
        
        # Total label
        self.total_label = tk.Label(self.bottom_frame, text="Total Items: 0, Total Price: Rs. 0", bg='green', fg='white', font=('courgette', 16, 'bold'))
        self.total_label.pack(side='left', padx=10)
        
        # Next button
        self.next_but = tk.Button(self.bottom_frame, text="NEXT", bg='#d2fbd0', command=self.next_button, font=('courgette', 18, 'bold'))
        self.next_but.pack(side='right', padx=10)
        
        self.menus = {}
        with open(f'{restaurant} menu.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[-1] not in self.menus:
                    self.menus[row[-1]] = [(row[0], int(row[-2]))]
                else:
                    self.menus[row[-1]].append((row[0], int(row[-2])))
        
        self.prices = []
        for x in self.menus.keys():
            for i in range(len(self.menus[x])):
                self.prices.append(self.menus[x][i][1])

        # Dictionary to store the selected quantity of each item
        self.global_quantity = {category: {item[0]: 0 for item in items} for category, items in self.menus.items()}
        
        self.buttons = []
        # Add buttons for each category on the left
        for i, category in enumerate(self.menus.keys()):
            btn = tk.Button(self.left_frame, text=category,bd=0,fg='white', bg='black', command=lambda c=category: self.change_category(c), font=('courgette', 16, 'bold'))
            self.buttons.append(btn)
            btn.grid(row=i+1, column=0, pady=5, sticky=tk.EW)
        
        #Fit the components inside the Window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Load the default menu
        self.load_menu(self.current_category.get())
    
    # Function to load menu items dynamically
    def load_menu(self, category):
        for widget in self.main_frame.winfo_children():
            widget.destroy()  # Clear the main menu area
    
        food_items = self.menus.get(category, [])
        self.counters.clear()  # Clear previous self.counters
    
        for i, (food, price) in enumerate(food_items):
            food_label = tk.Label(self.main_frame, text=f"{food} - Rs. {price}", bg='#d2fbd0', font=('courgette', 16, 'bold'))
            food_label.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            
            # Initialize the counter from global quantity
            counter = tk.StringVar(value=str(self.global_quantity[category][food]))
            self.counters.append(counter)
            
            minus_btn = tk.Button(self.main_frame, bg='#d2fbd0', activebackground="#d2fbd0", bd=0, image=self.min, command=lambda c=counter, f=food, cat=category, p=price: self.update_counter(c, -1, cat, f, p), font=('courgette', 16, 'bold'))
            minus_btn.grid(row=i, column=1)
            
            counter_label = tk.Label(self.main_frame, bg='#d2fbd0', textvariable=counter, width=3, font=('courgette', 16, 'bold'))
            counter_label.grid(row=i, column=2)
            
            plus_btn = tk.Button(self.main_frame, bg='#d2fbd0', activebackground="#d2fbd0", bd=0, image=self.plu, command=lambda c=counter, f=food, cat=category, p=price: self.update_counter(c, 1, cat, f, p), font=('courgette', 16, 'bold'))
            plus_btn.grid(row=i, column=3)
    
        self.update_total()  # Refresh total
    
    # Function to update counter and global quantity, and update the total price dynamically
    def update_counter(self, counter, change, category, food, price):
        current_value = int(counter.get())
        new_value = max(0, current_value + change)  # Ensure counter doesn't go below 0
        counter.set(str(new_value))
        
        # Update the global quantity for the specific item
        self.global_quantity[category][food] = new_value
    
        self.update_total()  # Update total whenever counter is changed
    
    # Function to update total price and items from global quantities
    def update_total(self):
        total_items = 0
        total_price = 0
    
        # Calculate total items and price from all categories
        for category, items in self.global_quantity.items():
            for food, quantity in items.items():
                price = next(price for item, price in self.menus[category] if item == food)
                total_items += quantity
                total_price += quantity * price
    
        self.total_label.config(text=f"Total Items: {total_items}, Total Price: Rs. {total_price}")
    
    # Function to change category and reload menu
    def change_category(self, category):
        self.current_category.set(category)
        self.load_menu(category)
        for other_btn in self.buttons:
            if(other_btn['text']==category):
                other_btn.config(fg = '#0676f1',bg='#ede8d0', activebackground='white', relief=tk.SUNKEN)
            else:
                other_btn.config(fg='white',bg='black', activebackground='white', relief=tk.RAISED)
    
    def next_button(self):
        if(self.getOrdered()[2]==0):
            messagebox.showerror("Order Error", "First choose an item by increasing its counter!")
        else:
            data = [datetime.now().strftime('%d/%m/%Y')]+ [datetime.now().strftime('%H:%M:%S')]+ [self.getOrdered()[2]] + self.getOrdered()[1]
            o = ord.Summary(data, self.username, self.getOrdered()[0])
            o.run()           
    
    def getOrdered(self):
        menu_items = []
        ordered_quantities = []
        for x in [self.global_quantity[y] for y in self.global_quantity.keys()]:
            for y in x:
                menu_items.append(y)
                ordered_quantities.append(x[y])
        
        order_total=0
        for i in range(len(self.prices)):
            order_total+=self.prices[i] * ordered_quantities[i]
            
        return (menu_items, ordered_quantities, order_total)
       
    def userbutton(self):
        if os.path.isfile(f"{self.username}_orders.csv"):
            self.display_csv_table(f"{self.username}_orders.csv")
        else:
            messagebox.showerror("File Error", "No order history found!")
                
    def display_csv_table(self, file_name):
        # Create a new Tkinter window
        window = tk.Toplevel()
        window.iconbitmap("admin.ico")
        window.title("Your Order History")
    
        # Create a frame for canvas and vertical scrollbar
        frame = tk.Frame(window)
        frame.pack(fill="both", expand=True)
    
        # Create a canvas and vertical scrollbar
        canvas = tk.Canvas(frame)
        v_scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=v_scrollbar.set)
    
        # Create a horizontal scrollbar
        h_scrollbar = tk.Scrollbar(window, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=h_scrollbar.set)
    
        # Create a frame inside the canvas which will be scrollable
        scrollable_frame = tk.Frame(canvas)
    
        # Configure the scrollable frame to adjust the scroll region when it's resized
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
    
        # Add the scrollable frame to the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
        # Add the canvas and vertical scrollbar to the layout
        canvas.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
    
        # Add the horizontal scrollbar at the bottom and make it span the entire window width
        h_scrollbar.pack(side="bottom", fill="x")
    
        # Open and read the CSV file
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            order_price = []
            for i,x in enumerate(self.getOrdered()[0]):
                order_price.append(x + " - " + str(self.prices[i]))
            for i, x in enumerate(["Date"]+["Time"]+["Total"]+order_price+["Order ID"]):
                tk.Label(scrollable_frame,bg="black", fg="white", text=x, padx=10, pady=5, borderwidth=4, relief="solid", font=("Kalam", 18, "bold")).grid(row=0, column=i, sticky="nsew")
            # Loop through CSV file and place labels in the scrollable frame
            for row_index, row in enumerate(reader):
                for col_index, cell in enumerate(row):
                    # Create a label for each cell and place it in the grid
                    label = tk.Label(scrollable_frame, text=cell, padx=10, pady=5, borderwidth=2, relief="solid", font=("Kalam", 15))
                    label.grid(row=row_index+1, column=col_index, sticky="nsew")
    
        # Make the columns stretchable for even spacing
        total_columns = len(next(csv.reader(open(file_name))))
        for col_index in range(total_columns):
            scrollable_frame.grid_columnconfigure(col_index, weight=1)
    
        # Ensure the scrollable_frame's width grows with the canvas' width
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    
        # Scroll canvas with arrow keys
        def scroll_vertically(event):
            if event.keysym == 'Up':
                canvas.yview_scroll(-1, "units")
            elif event.keysym == 'Down':
                canvas.yview_scroll(1, "units")
    
        def scroll_horizontally(event):
            if event.keysym == 'Left':
                canvas.xview_scroll(-1, "units")
            elif event.keysym == 'Right':
                canvas.xview_scroll(1, "units")
    
        # Bind the arrow keys to scrolling actions
        window.bind("<Up>", scroll_vertically)
        window.bind("<Down>", scroll_vertically)
        window.bind("<Left>", scroll_horizontally)
        window.bind("<Right>", scroll_horizontally)
   
            
    # Run the application
    def run(self):
        self.root.mainloop()

if __name__=="__main__":
    a = Guest("Sid")
    a.run()