import Guest as gue
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import os.path

class Log:
    def name_present(self, na):
        with open('record.csv', 'r', ) as file:
            csvFile = csv.reader(file)
            header = True
            self.users = {}
            for row in csvFile:
                if(header == True):
                    header = False
                    continue
                self.users[row[0]] = row[1]
            if(na in self.users.keys()):
                return True
            else:
                return False

    def gFunction(self):
        self.root.destroy()
        a = gue.Guest("_Guest_", self.res_name)
        a.run()
    def uFunction(self):
        if(self.name.get()=='' or self.pas.get()==''):
            messagebox.showerror("Empty Fields", "Please fill all the details properly!")
        else:
            if(os.path.isfile('record.csv')):
                if(self.name_present(self.name.get())):
                    messagebox.showerror("Sign Up Error", "Username already present!")
            data=[{'Username':self.name.get(), 'Password':self.pas.get()}]
            with open('record.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['Username','Password'])
                writer.writeheader()
                writer.writerows(data)
                messagebox.showinfo("Sign Up", "Signed Up successfully, now you can login using same credentials.")		
            #self.root.destroy()
    def lFunction(self):
        if(self.name.get()=='' or self.pas.get()==''):
            messagebox.showerror("Empty Fields", "Please fill all the details properly!")
        else:
            if(os.path.isfile('record.csv')):
                if(self.name_present(self.name.get())):
                    if(self.users[self.name.get()]==self.pas.get()):
                        self.root.destroy()
                        b = gue.Guest(self.name.get(), self.res_name)
                        b.run()
                    else:
                        messagebox.showerror("Login Error", "Please enter correct Password!")
                else:
                    messagebox.showerror("Login Error", "Username not found. Kindly sign-up first!")
            else:
                messagebox.showerror("Login Error", "No records are found! Sign Up first.")

    def __init__(self, res_name):
        self.root = Tk()
        self.root.geometry('782x481')
        self.root.configure(background='#9DF504')
        self.root.title('Client')
        self.root.iconbitmap("client.ico")
        self.root.attributes('-alpha', 0.95)
        self.root.resizable(width=False, height=False)
        style = ttk.Style(self.root)
        style.theme_use('xpnative')
        
        self.name = StringVar(self.root)
        self.pas = StringVar(self.root)
        self.res_name = res_name
        
        Label(self.root, bg='#9DF504', text=f'Welcome to {res_name} Restaurant!', font=('verdana', 24, 'bold')).place(x=100, y=10)
        
        self.image = PhotoImage(file = 'images.png')
        Label(image=self.image).place(x=20, y=77)
        
        Label(self.root, bg='#9DF504', text='Enter your Username', font=('verdana', 24, 'bold')).place(x=357, y=77)
        
        Entry(self.root,textvariable=self.name, width = 25, font=('Arial', 20)).place(x=357, y=127)
        
        Label(self.root, bg='#9DF504', text='Enter your Password', font=('verdana', 24, 'bold')).place(x=357, y=197)
        
        Entry(self.root,textvariable=self.pas, show="*", width = 25, font=('Arial', 20)).place(x=357, y=247)
        
        # Created buttons
        ttk.Button(self.root, text='Use like Guest',  command=self.gFunction).place(x=587, y=347)
        ttk.Button(self.root, text='Login',  command=self.lFunction).place(x=467, y=347)
        ttk.Button(self.root, text='Sign Up!',  command=self.uFunction).place(x=357, y=347)

    def run(self):    
        self.root.mainloop()

if __name__=="__main__":
    a = Log()
    a.run()