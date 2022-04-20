# ini merupakan tampilan layar utama program skripsi
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
# import tkinter.font as TkFont

root = tk.Tk(className='Wayang Identification by Video')

window_width = 700
window_height = 540

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# label = judul skripsi
labelExample2 = tk.Label(root,
        borderwidth = 2,
        width = 600,
        wraplength=500,
        relief="ridge",
        font=("Helvetica", 12),
        text="ANOTASI KARAKTER PADA VIDEO WAYANG KULIT DENGAN METODE EDGE DETECTION DAN ALGORITMA CONVOLUTIONAL NEURAL NETWORK (CNN)")

labelExample2.pack(ipadx=5, ipady=5, pady=5)

# display an image label
photo = tk.PhotoImage(file='./assets/img/banner_fix.png')
image_label = ttk.Label(
    root,
    justify="center",
    image=photo,
    padding=5
)
image_label.pack()

# fungsi-fungsi button
def btn_info_app():
    print('Button clicked')

def btn_preprocessing():
    print('Button clicked')

def btn_upload_drive():
    print('Button clicked')

def btn_indentify():
    print('Button clicked')

def btn_quit_app():
    return root.destroy()

# button control
button1 = ttk.Button(root, text='About The App', command=btn_info_app, width=100)
button1.pack(padx=5, pady=5, ipady=3)

button2 = ttk.Button(root, text='Preprocessing Data', command=btn_preprocessing, width=100)
button2.pack(padx=5, pady=5, ipady=3)

button3 = ttk.Button(root, text='Upload Data to Drive', command=btn_upload_drive, width=100)
button3.pack(padx=5, pady=5, ipady=3)

button4 = ttk.Button(root, text='Indentify Video Testing', command=btn_indentify, width=100)
button4.pack(padx=5, pady=5, ipady=3)

button5 = ttk.Button(root, text='Quit App', command=btn_quit_app, width=100,)
button5.pack(padx=5, pady=5, ipady=3)

# main loop all
root.mainloop()