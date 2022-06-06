import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x300")  # Size of the window 
root.title('Form Identifikasi Gambar Wayang')
my_font1=('times', 18, 'bold')
l1 = tk.Label(root,text='Add Student Data with Photo',width=30,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(root, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 

def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    print(filename)
    img=Image.open(filename)
    img=img.resize((100,100))
    img = ImageTk.PhotoImage(img)
    b2 =tk.Button(root,image=img) # using Button 
    b2.grid(row=3,column=1)

root.mainloop()  # Keep the window open