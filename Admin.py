import csv
from tkinter import *
from tkinter import messagebox
import Order as Od

root = Tk()
root.title("Admin")
root.iconbitmap("admin.ico")
root.resizable(width=False, height=False)
root.attributes('-alpha', 0.95)
root.configure(background='#e76f51')
root.eval('tk::PlaceWindow . center')

Label(root,text="Welcome!",justify="center", font=("Comic Sans MS", 42, "bold"), background='#e76f51', fg = "#003049").grid(row=1, column=1, columnspan=5)

"""def header():
    f1=open("menu.csv",'w',newline='')
    item=['itemname','itemid','price']
    writer=csv.writer(f1)
    writer.writerow(item)
    f1.close()
"""

def home(data):
    home=Tk()
    home.iconbitmap("admin.ico")
    home.resizable(width=False, height=False)
    home.attributes('-alpha', 0.95)
    home.configure(background='#e76f51')
    home.title("Home Page")
    Label(home,text=f"Welcome, {data[0]}",justify="center", font=("Comic Sans MS", 42, "bold"), background='#e76f51', fg = "#003049").grid(row=1,column=1, sticky="nsew")
    def add():
        add=Toplevel(home)
        add.resizable(width=False, height=False)
        add.attributes('-alpha', 0.95)
        add.configure(background='#e76f51')
        add.title("Add Items")
        e=Entry(add,width=50, font=("comic sans ms", 18))
        e.grid(row=3,column=1)
        e.get()
        Labele =Label(add,text="Enter Item Name",justify="center", font=("Comic Sans MS", 20, "bold"))
        Labele.grid(row=2,column=1)
        e2=Entry(add,width=50, font=("comic sans ms", 18))
        e2.grid(row=5,column=1)
        e2.get()
        Labele2 =Label(add,text="Enter Price",justify="center", font=("Comic Sans MS", 20, "bold"))
        Labele2.grid(row=4,column=1)
        e3=Entry(add,width=50,font=("comic sans ms", 18))
        e3.grid(row=7,column=1)
        Labele3 =Label(add,text="Enter Item Type",justify="center", font=("Comic Sans MS", 20, "bold"))
        Labele3.grid(row=6,column=1)
        def confirm():
            import string
            import random
            digit=string.digits
            id=''.join(random.choice(digit) for i in range(4))
            try:
                a = int(e2.get())
                if (e.get() and e2.get() and e3.get())!= "":
                        item=[e.get(),id,e2.get(),e3.get()]
                        with open(f"{data[0]} menu.csv", 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(item)
                        messagebox.showinfo("Completed", "Item Added Successfully")
                else:
                        messagebox.showerror("Field Error", "Enter Valid Details!")
            except:
                messagebox.showerror("Field Error", "Enter Valid Details!")
        myButton=Button(add,text="Add Item",command=confirm,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
        myButton.grid(row=10,column=0,columnspan=2)
        myButton.focus_set()
    def view():
        class Table:
            def __init__(self,root):
                for i in range(total_rows):
                    for j in range(total_columns):
                 
                        self.e = Entry(root, width=20, fg='blue',
                                       font=('Arial',16,'bold'))
                         
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, lst[i][j])
        lst=[]
        f1=open(f"{data[0]} menu.csv",'r')
        reader=csv.reader(f1)
        for i in reader:
            lst.append(i)         
        if lst==[]:
            messagebox.showerror("Empty", "No Item Present")
        else:
            view=Toplevel(home)
            view.resizable(width=False, height=False)
            view.attributes('-alpha', 0.95)
            view.configure(background='#e76f51')
            view.title("View Menu")
            total_rows = len(lst)
            total_columns = len(lst[0])
            t=Table(view)   
    def update():
        update=Toplevel(home)
        update.resizable(width=False, height=False)
        update.attributes('-alpha', 0.95)
        update.configure(background='#e76f51')
        update.iconbitmap("admin.ico")
        update.title("Update Menu")
        def update1(data):
            my_list.delete(0, END)
            # Add toppings to listbox
            for item in data:
                my_list.insert(END, item)
       
    # Update entry box with listbox clicked
        def fillout(e):
            # Delete whatever is in the entry box
            my_entry.delete(0, END)

            # Add clicked list item to entry box
            my_entry.insert(0, my_list.get(ANCHOR))
            
        def confirm():
            price=Toplevel(update)
            price.iconbitmap("admin.ico")
            price.resizable(width=False, height=False)
            price.attributes('-alpha', 0.95)
            price.configure(background='#e76f51')
            e=Entry(price,width=50, font=("comic sans ms", 18))
            e.grid(row=3,column=1)
            e.get()
            Labele =Label(price,text="Enter New Price",justify="center", font=("Comic Sans MS", 20, "bold"))
            Labele.grid(row=2,column=1)
            def msg():
                f=open(f"{data[0]} menu.csv",'r')
                reader=csv.reader(f)
                nmenu=[]
                for i in reader:
                    if i[0]==my_list.get(ANCHOR):
                         i[2]=e.get()
                    nmenu.append(i)
                f1=open(f"{data[0]} menu.csv",'w',newline='')
                writer=csv.writer(f1)
                writer.writerows(nmenu)
                f1.close()
                            

                messagebox.showinfo("Completed", "Price Updated Successfully")
                myButton1.config(state=DISABLED)
                    
            myButton1=Button(price,text="confirm",command=msg,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
            myButton1.grid(row=5,column=1)
            myButton1.focus_set()
            
    # Create function to check entry vs listbox
        def check(e):
            # grab what was typed
            typed = my_entry.get()

            if typed == '':
                    data = menu
            else:
                    data = []
                    for item in menu:
                            if typed.lower() in item.lower():
                                    data.append(item)

            # update our listbox with selected items
            update1(data)               

        my_label = Label(update, text="Search Menu...",
                font=("Helvetica", 14), fg="grey")

        my_label.pack(pady=20)

        # Create an entry box
        my_entry = Entry(update, font=("Helvetica", 20))
        my_entry.pack()

        # Create a listbox
        my_list = Listbox(update, width=50)
        my_list.pack(pady=40)

        menu=[]
        f1=open(f"{data[0]} menu.csv",'r')
        reader=csv.reader(f1)
        for i in reader:
            menu.append(i[0])
        # Add the toppings to our list
        update1(menu)

        # Create a binding on the listbox onclick
        my_list.bind("<<ListboxSelect>>", fillout)
        my_entry.bind("<KeyRelease>",check)
        myButton=Button(update,text="Update Price",command=confirm,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
        myButton.pack()

            
    def delete():
        delete=Toplevel(home)
        delete.iconbitmap("admin.ico")
        delete.resizable(width=False, height=False)
        delete.attributes('-alpha', 0.95)
        delete.configure(background='#e76f51')
        delete.title("Delete")
        def update1(data):
            my_list.delete(0, END)

            # Add toppings to listbox
            for item in data:
                my_list.insert(END, item)
       
    # Update entry box with listbox clicked
        def fillout(e):
            # Delete whatever is in the entry box
            my_entry.delete(0, END)

            # Add clicked list item to entry box
            my_entry.insert(0, my_list.get(ANCHOR))
            
        def confirm():
                f=open(f"{data[0]} menu.csv",'r')
                reader=csv.reader(f)
                nmenu=[]
                for i in reader:
                    if i[0]==my_list.get(ANCHOR):
                         continue
                    nmenu.append(i)
                f1=open(f"{data[0]} menu.csv",'w',newline='')
                writer=csv.writer(f1)
                writer.writerows(nmenu)
                f1.close()
                
                messagebox.showinfo("Completed", "Item Deleted Successfully")
            
    # Create function to check entry vs listbox
        def check(e):
            # grab what was typed
            typed = my_entry.get()

            if typed == '':
                    data = menu
            else:
                    data = []
                    for item in menu:
                            if typed.lower() in item.lower():
                                    data.append(item)

            # update our listbox with selected items
            update1(data)               

        my_label = Label(delete, text="Search Menu...",
                font=("Helvetica", 14), fg="grey")

        my_label.pack(pady=20)

        # Create an entry box
        my_entry = Entry(delete, font=("Helvetica", 20))
        my_entry.pack()

        # Create a listbox
        my_list = Listbox(delete, width=50)
        my_list.pack(pady=40)

        menu=[]
        f1=open(f"{data[0]} menu.csv",'r')
        reader=csv.reader(f1)
        for i in reader:
            menu.append(i[0])
        # Add the toppings to our list
        update1(menu)

        # Create a binding on the listbox onclick
        my_list.bind("<<ListboxSelect>>", fillout)
        my_entry.bind("<KeyRelease>",check)
        myButton=Button(delete,text="Delete",command=confirm,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
        myButton.pack()
        
    def vieworder():
        lst=[]
        lst.append(["Date","Time","Cost","Order Id"])
        vieworder=Toplevel(home)
        vieworder.resizable(width=False, height=False)
        vieworder.attributes('-alpha', 0.95)
        vieworder.configure(background='#e76f51')
        vieworder.iconbitmap("admin.ico")
        vieworder.title("Orders")
        f=open('record.csv','r')
        reader=csv.reader(f)
        for i in reader:
            if i[0]=="Username":
                 continue
            else:
                 f1=open(f'{i[0]}_orders.csv','r')
                 reader=csv.reader(f1)
                 for i in reader:
                      lst.append([i[0],i[1],i[2],i[4]])
        class Table:
            def __init__(self,root):
                for i in range(total_rows):
                    for j in range(total_columns):
                 
                        self.e = Entry(root, width=20, fg='blue',
                                       font=('Arial',16,'bold'))
                         
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, lst[i][j])
        if lst==[]:
            messagebox.showerror("Empty", "No Orders Placed")
        else:
            view=Toplevel(home)
            view.resizable(width=False, height=False)
            view.attributes('-alpha', 0.95)
            view.configure(background='#e76f51')
            view.title("View Order Details")
            total_rows = len(lst)
            total_columns = len(lst[0])
            t=Table(view) 
        

    """"
    def monthlysales():
        ms=Toplevel(home)
        ms.resizable(width=False, height=False)
        ms.attributes('-alpha', 0.95)
        ms.configure(background='#e76f51')
        ms.iconbitmap("admin.ico")
        ms.title("Sales Details")
    """
    frame1 = Frame(home, bg='#e76f51')
    frame1.grid(row=2, column=1, sticky="nsew")
    button_text = [("Add Menu", add), ("View Menu", view), ("Update Menu", update), ("View Orders", vieworder),("Delete Menu", delete)]
    for i, x in enumerate(button_text):
        Button(frame1,text=x[0],command=x[1],padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold')).grid(row=2,column=i,sticky="nsew")

def signin():
    signin1=Toplevel(root)
    signin1.resizable(width=False, height=False)
    signin1.attributes('-alpha', 0.95)
    signin1.configure(background='#e76f51')
    signin1.iconbitmap("admin.ico")
    signin1.title("Sign Up")
    Label1=Label(signin1,text="Sign Up",justify="center", font=("Comic Sans MS", 42, "bold"), background='#e76f51', fg = "#003049")
    Label1.grid(row=1,column=1)
    e=Entry(signin1,width=50, font=("comic sans ms", 18))
    e.grid(row=3,column=1)
    e.get()
    Labele=Label(signin1,text="Enter Restaurnant Name",justify="center", font=("Comic Sans MS", 20, "bold"), background='#e76f51', fg = "#003049")
    Labele.grid(row=2,column=1)
    e2=Entry(signin1, show="*", width=50, font=("comic sans ms", 18))
    e2.grid(row=5,column=1)
    e2.get()
    Labele2=Label(signin1,text="Enter Password",justify="center", font=("Comic Sans MS", 20, "bold"), background='#e76f51', fg = "#003049")
    Labele2.grid(row=4,column=1)
    def confirm1():
        confirm=Toplevel(signin1)
        confirm.resizable(width=False, height=False)
        confirm.attributes('-alpha', 0.95)
        confirm.configure(background='#e76f51')
        confirm.iconbitmap("admin.ico")
        Label(confirm,text=f"{e.get()} Has been Successfully Registered",justify="center", font=("Comic Sans MS", 42, "bold"), background='#e76f51', fg = "#003049").grid(row=1,column=1)
        def view():
            def disable_button():
               myButton3.config(state=DISABLED)
            import string
            import random
            digit=string.digits
            id=''.join(random.choice(digit) for i in range(4))
            f=open('admin.csv','a',newline='')
            row=[e.get(),id,e2.get()]
            writer=csv.writer(f)
            writer.writerow(row)
            f.close()
            f=open('admin.csv','r')
            reader=csv.reader(f)
            #for i in reader:
                #print(i)
            messagebox.showinfo('Restaurant Id',f'Your Restaurant Id is {id} ')
            disable_button()
            Label1.grid(row=4,column=1)
        myButton3=Button(confirm,text="View Restaurant Id",command=view,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
        myButton3.grid(row=5,column=1,columnspan=2)
    myButton=Button(signin1,text="confirm",command=confirm1,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
    myButton.grid(row=6,column=1,columnspan=2)

def login():
    root.destroy()
    login1=Tk()
    login1.resizable(width=False, height=False)
    login1.attributes('-alpha', 0.95)
    login1.configure(background='#e76f51')
    login1.iconbitmap("admin.ico")
    login1.title("Log In")
    Label1=Label(login1,text="Enter Your Credentials", justify="center", font=("Comic Sans MS", 42, "bold"), background='#e76f51', fg = "#003049")
    Label1.grid(row=1,column=1)
    e=Entry(login1,width=50, font=("comic sans ms", 18))
    e.grid(row=3,column=1)
    e.get()
    Labele=Label(login1,text="Enter Restaurant Id" ,justify="center", font=("Comic Sans MS", 20, "bold"), background='#e76f51', fg = "#003049")
    Labele.grid(row=2,column=1)
    e2=Entry(login1,width=50, show="*", font=("comic sans ms", 18))
    e2.grid(row=5,column=1)
    Labelp=Label(login1,text="Enter Password",justify="center", font=("Comic Sans MS", 20, "bold"), background='#e76f51', fg = "#003049")
    Labelp.grid(row=4,column=1)
    e2.get()
    def check():
        f=open('admin.csv','r')
        reader=csv.reader(f)
        for i in reader:
            if i[1]==e.get():
                  if i[2]==e2.get():
                       home(i)
                       login1.destroy()
                       break
            else:
                messagebox.showerror('Validation Error','Enter valid Credentials')
    myButton=Button(login1,text="confirm",command=check,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
    myButton.grid(row=7,column=1)
    myButton.focus_set()

myButton=Button(root,text="Sign Up",command=signin,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
myButton.grid(row=4,column=1,columnspan=2, padx=50, pady=50)
myButton2=Button(root,text="Log In",command=login,padx=10,pady=5, background='#8ecae6', fg = "#023047", activebackground='#ffb703', font=('courgette', 18, 'bold'))
myButton2.grid(row=4, column=4,columnspan=2, padx=50, pady=50)
root.mainloop()


