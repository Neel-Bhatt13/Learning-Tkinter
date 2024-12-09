import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("My icon and image")


def forward(image_number):
    global mylabel,button_forward,button_back
    mylabel.grid_forget()
    mylabel = tk.Label(image=image_list[image_number-1])
    button_forward = tk.Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back = tk.Button(root,text="<<",command=lambda:back(image_number-1))
    
    if image_number == 5:
        button_forward = tk.Button(root,text=">>",state="disabled")
    
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2) 
    mylabel.grid(row=0,column=0,columnspan=3)
    
    status = tk.Label(root,text="image "+str(image_number)+"  of  "+str(len(image_list)))
    status.grid(row=2,column=2)
    
def back(image_number):
     global mylabel,button_forward,button_back 
     mylabel.grid_forget()
     mylabel = tk.Label(image=image_list[image_number-1])
     button_forward = tk.Button(root,text=">>",command=lambda:forward(image_number+1))
     button_back = tk.Button(root,text="<<",command=lambda:back(image_number-1))
     
     if image_number == 1 :
         button_back = tk.Button(root,text="<<",state="disabled")
     
     button_back.grid(row=1,column=0)
     button_forward.grid(row=1,column=2) 
     mylabel.grid(row=0,column=0,columnspan=3)
     
     status = tk.Label(root,text="image "+str(image_number)+"  of  "+str(len(image_list)))
     status.grid(row=2,column=2)
     

# creating a icon 
root.iconbitmap(r"C:\Users\USER\Downloads\IMG_20240729_023650_759.ico")

# creating an image 
my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\USER\OneDrive\Pictures\IMG_20240729_023650_759.jpg").resize((400,400)))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\USER\OneDrive\Pictures\IMG_20240513_234302_076.jpg").resize((400,400)))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\USER\OneDrive\Pictures\IMG_20240114_233155_226.jpg").resize((400,400)))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\USER\OneDrive\Pictures\IMG_20230212_195146_685.jpg").resize((400,400)))
my_img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\USER\OneDrive\Pictures\IMG_20230928_003323_007.jpg").resize((400,400)))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

# creating the status 
status = tk.Label(root,text="image 1 of  "+ str(len(image_list)))
status.grid(row=2,column=2)

mylabel = tk.Label(image=my_img1)
mylabel.grid(row=0,column=0,columnspan=3)

button_back = tk.Button(root,text="<<",command=lambda:back(),state="disabled")
button_back.grid(row=1,column=0)

button_forward = tk.Button(root,text=">>",command=lambda:forward(2),) 
button_forward.grid(row=1,column=2)      


# creating an exit button
button_quit = tk.Button(root,text="Quit",command=root.quit)
button_quit.grid(row=1,column=1)


root.mainloop()
