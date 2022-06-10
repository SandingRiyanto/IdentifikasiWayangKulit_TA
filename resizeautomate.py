# load library
import imgaug.augmenters as iaa
from tkinter import filedialog
import tkinter as tk
from tkinter import *
from cv2 import cv2
import numpy as np
import glob
import os

# windows control
root = tk.Tk()
root.title('Preprocessing Form Detail')
root.geometry('520x120')
root.config(bg='#F2B33D')

def btn_edge_detect():

    i=0
    j=0
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please Select a Directory Raw Dataset 2')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please Select a Directory to Save in Fix Dataset')
    
    for img in glob.glob(file_path_variable1 + "/*.*"):
        image = cv2.imread(img)
        ImgResized = cv2.resize(image, (120, 160))
        
        # save image in custom folder
        cv2.imwrite(file_path_variable2 + "/image%03i.jpg" %i, ImgResized)

        i +=1
        sum_img = j + i
        
        cv2.imshow('image', ImgResized)
        cv2.waitKey(10)

    print("Total keseluruhan image (ready):", sum_img)
    cv2.destroyAllWindows()

# button control
frame = Frame(root, bg='#F2B33D')

Button(frame, text="Flip LR Images", command=btn_edge_detect).grid(row=0, column=0)

frame.pack(expand=True) 
root.mainloop()