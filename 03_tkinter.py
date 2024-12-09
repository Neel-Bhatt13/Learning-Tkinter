from tkinter import *
import tkinter as tk

root = Tk()

# creating the label
# mylabel1 = tk.Label(root,text = "Hello Neel!")
# mylabel2 = tk.Label(root,text = "my name is neel")
# mylabel1.pack()
# mylabel2.pack()

# this can be done using grid fucntion (positioning the label)
# mylabel3 = tk.Label(root,text = "Hello Neel!").grid(row=0,column=0)
# mylabel4 = tk.Label(root,text = "my name is neel").grid(row=1,column=0)
# mylabel3.grid(row=0,column=0)
# mylabel4.grid(row=1,column=0)



# creating a button 
def clickme():
    mylabel = tk.Label(root,text="Hello! "+entry.get())
    mylabel.pack()

button = tk.Button(root,text="enter your name ",padx=10,pady=10,command=clickme,fg="yellow",bg="black") 
button.pack() 

# creating input fields
entry = tk.Entry(root,width=50,bg = "lightblue",fg="green",borderwidth=10)  
entry.pack()
entry.insert(0,"enter your name :- ") # used to set default text inside the field 

# creating the frame
frame = tk.LabelFrame(root,text="This is my frame",padx=10,pady=10)
frame.pack()

btn = tk.Button(frame,text="Dont click me!")
btn.pack()

root.mainloop()