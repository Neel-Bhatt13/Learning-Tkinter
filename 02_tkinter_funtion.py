import tkinter as tk
from tkinter import messagebox

class mygui:
    def __init__(self):
    
        self.root = tk.Tk()
    
        self.label = tk.Label(self.root,text = " your message ",font=("arial",18))
        self.label.pack()
        
        self.textbox = tk.Text(self.root,height=5,font=("arial",18))
        self.textbox.pack(padx=10,pady=10)
        
        self.checkstate = tk.IntVar()
        self.check = tk.Checkbutton(self.root,text="show messagebox",font=("arial",18),variable = self.checkstate)
        self.check.pack(padx=10,pady=10)
        
        self.button = tk.Button(self.root,text="show message",font=("arial",18),command=self.show_message)
        self.button.pack(padx=10,pady=10)
        
        self.root.mainloop()
        
    def show_message(self):
        print("hello neel")
        if self.checkstate.get() == 0 :
            print(self.textbox.get("1.0",tk.END))
        else:
            messagebox.showinfo("titile = Message",message=self.textbox.get("1.0",tk.END))
            
            
        
mygui()
        