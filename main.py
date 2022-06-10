# load library
from tkinter import filedialog
from tkinter import Canvas
from tkinter import ttk
import tkinter as tk
from cv2 import cv2
import numpy as np
import webbrowser
import shutil
import glob
import os
# from PIL import ImageTk, Image

# frame
root = tk.Tk(className='Wayang Identification by Video')

window_width = 700
window_height = 600

copyright = u"\u00A9"
huruf=('Times',12,'italic')

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# label = judul skripsi
labelJudul = tk.Label(root,
        borderwidth = 2,
        width = 600,
        wraplength=500,
        relief="ridge",
        font=("Helvetica", 12),
        text="ANOTASI KARAKTER PADA VIDEO WAYANG KULIT DENGAN METODE EDGE DETECTION DAN ALGORITMA CONVOLUTIONAL NEURAL NETWORK (CNN)")

labelJudul.pack(ipadx=5, ipady=5, pady=5)

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
# done
def btn_info_app():
    # import about_page
    os.system("python about_page.py")

# done
def btn_preprocessing():
    # import detail_preprocess
    os.system("python detail_preprocess.py")

# done
def btn_upload_drive():
    webbrowser.open_new(r"https://colab.research.google.com/drive/1tpldXk9W1ZlOui1GfBdqLUuc5Uxz7WsG")

# done
def btn_identify_img():
    # import identifyimg
    os.system("python identifyimg.py")

# on progress....
def btn_indentify_vid():
    # import identifyvid
    os.system("python identifyvid.py")
    print('Button clicked')

# done
def btn_quit_app():
    return root.destroy()
    # os.system("python splitfiles.py")

# button control
button1 = ttk.Button(root, text='About The App', command=btn_info_app, width=100)
button1.pack(padx=5, pady=5, ipady=3)

button2 = ttk.Button(root, text='Preprocessing Data', command=btn_preprocessing, width=100)
button2.pack(padx=5, pady=5, ipady=3)

button3 = ttk.Button(root, text='Training CNN Model', command=btn_upload_drive, width=100)
button3.pack(padx=5, pady=5, ipady=3)

button4 = ttk.Button(root, text='Identify Images Testing', command=btn_identify_img, width=100)
button4.pack(padx=5, pady=5, ipady=3)

button5 = ttk.Button(root, text='Indentify Video Testing', command=btn_indentify_vid, width=100)
button5.pack(padx=5, pady=5, ipady=3)

button6 = ttk.Button(root, text='Quit App', command=btn_quit_app, width=100)
button6.pack(padx=5, pady=5, ipady=3)

l1=tk.Label(root,text=copyright + ' Develop by Sanding Riyanto | 1811501541', font=huruf, fg="black").pack()

# main loop all
root.mainloop()