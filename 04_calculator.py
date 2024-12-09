from tkinter import *
import tkinter as tk 

root = tk.Tk()
root.title("Calculator")

# ✅ Set the minimum size and initial size of the window
root.minsize(400, 500)  # Prevents the window from getting smaller than 400x500
root.geometry("400x500")  # Sets the initial size of the window to 400x500

def buttonclick(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))
    
def button_clear():
    entry.delete(0, END)
    
def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)
    
def button_subtraction(): 
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiplication():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def button_division():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

def button_equals():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    elif math == "division":
        if int(second_number) == 0:  
            entry.insert(0, "Error")  
        else:
            entry.insert(0, f_num / int(second_number))

# Configure rows and columns to be resizable
for i in range(5):  # 5 rows total (0 to 4)
    root.rowconfigure(i, weight=1)

for i in range(4):  # 4 columns total (0 to 3)
    root.columnconfigure(i, weight=1)
    
# Entry widget
entry = tk.Entry(root, bg="black", fg="white", font=("Arial", 50))
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Button Definitions
button1 = tk.Button(root, text="1", bg="lightblue", command=lambda: buttonclick(1))
button1.grid(row=1, column=0, sticky="nsew")

button2 = tk.Button(root, text="2", bg="lightblue", command=lambda: buttonclick(2))
button2.grid(row=1, column=1, sticky="nsew")

button3 = tk.Button(root, text="3", bg="lightblue", command=lambda: buttonclick(3))
button3.grid(row=1, column=2, sticky="nsew")

button4 = tk.Button(root, text="4", bg="lightblue", command=lambda: buttonclick(4))
button4.grid(row=2, column=0, sticky="nsew")

button5 = tk.Button(root, text="5", bg="lightblue", command=lambda: buttonclick(5))
button5.grid(row=2, column=1, sticky="nsew")

button6 = tk.Button(root, text="6", bg="lightblue", command=lambda: buttonclick(6))
button6.grid(row=2, column=2, sticky="nsew")

button7 = tk.Button(root, text="7", bg="lightblue", command=lambda: buttonclick(7))
button7.grid(row=3, column=0, sticky="nsew")

button8 = tk.Button(root, text="8", bg="lightblue", command=lambda: buttonclick(8))
button8.grid(row=3, column=1, sticky="nsew")

button9 = tk.Button(root, text="9", bg="lightblue", command=lambda: buttonclick(9))
button9.grid(row=3, column=2, sticky="nsew")

button0 = tk.Button(root, text="0", bg="lightblue", command=lambda: buttonclick(0))
button0.grid(row=4, column=0, sticky="nsew")

buttonequals = tk.Button(root, text="=", bg="lightblue", command=button_equals)
buttonequals.grid(row=4, column=1, sticky="nsew")

buttonclear = tk.Button(root, text="Clear", bg="lightblue", command=button_clear)
buttonclear.grid(row=4, column=2, sticky="nsew")

buttonadd = tk.Button(root, text="+", bg="lightblue", command=button_add)
buttonadd.grid(row=1, column=3, sticky="nsew")

buttonsubtraction = tk.Button(root, text="-", bg="lightblue", command=button_subtraction)
buttonsubtraction.grid(row=2, column=3, sticky="nsew")

buttonmultiplication = tk.Button(root, text="X", bg="lightblue", command=button_multiplication)
buttonmultiplication.grid(row=3, column=3, sticky="nsew")

buttondivision = tk.Button(root, text="/", bg="lightblue", command=button_division)
buttondivision.grid(row=4, column=3,sticky="nsew")

root.mainloop()
