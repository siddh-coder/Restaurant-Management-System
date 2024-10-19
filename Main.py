# Import module  
from tkinter import *

# Create object  
root = Tk() 
root.title("Welcome!")
root.iconbitmap("client.ico")
root.attributes('-alpha', 0.95)
root.resizable(width=False, height=False)

def admin():
    root.destroy()
    import Admin

def client():
    root.destroy()
    import ResChoose
  
# Adjust size  
root.geometry("630x350") 
  
# Add image file 
bg = PhotoImage(file = "card.png") 
  
# Create Canvas 
canvas1 = Canvas( root, width = 630, 
                 height = 350) 
  
canvas1.pack(fill = "both", expand = True) 
  
# Display image 
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw") 
  
# Add Text 
canvas1.create_text(250, 100,fill ="white", text = "Welcome, choose your Path: ", font=('Monotype Corsiva', 30, "bold")) 
  
# Create Buttons 
button1 = Button( root,bd=0, bg = "#454448", fg ="white", text = "ADMIN", command = admin, font=('Monotype Corsiva', 20, "bold")) 
button2 = Button( root,bd=0, bg = "#454448", fg ="white", text = "CLIENT", command = client, font=('Monotype Corsiva', 20, "bold")) 
  
# Display Buttons 
button1_canvas = canvas1.create_window( 100, 230,  
                                       anchor = "nw", 
                                       window = button1) 
  
button2_canvas = canvas1.create_window( 300, 230, 
                                       anchor = "nw", 
                                       window = button2)  
  
# Execute tkinter 
root.mainloop()