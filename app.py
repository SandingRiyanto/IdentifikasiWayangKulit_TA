# load library
from tkinter import filedialog
from tkinter import Canvas
from tkinter import ttk
import tkinter as tk
from cv2 import cv2
import numpy as np
import webbrowser
import glob
import os

# frame
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

# on progress....
def btn_info_app():
    # load about_page.py file
    import about_page

# on progress....
def btn_preprocessing():
    i=0
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please Select a Directory Raw Dataset')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please Select a Directory to Save in Fix Dataset')
    
    for img in glob.glob(file_path_variable1 + "/*.*"):
        image = cv2.imread(img)
        ImgResized = cv2.resize(image, (224, 224))

        # convert RGB to Grayscale image
        ImgGray = cv2.cvtColor(ImgResized, cv2.COLOR_BGR2GRAY)
        # canny edge detection
        ImgEdge = cv2.Canny(ImgGray, 100, 200)

        # save image in custom folder
        cv2.imwrite(file_path_variable2 + "/image%03i.jpg" %i, ImgEdge)

        i +=1

        # cv2.imshow('image', ImgGray)
        cv2.imshow('image', ImgEdge)
        cv2.waitKey(10)

    cv2.destroyAllWindows()

# done
def btn_upload_drive():
    webbrowser.open_new(r"https://drive.google.com/drive/folders/1frmoNKxnT6ABOAeSpqME79wEhgeFa5td")

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