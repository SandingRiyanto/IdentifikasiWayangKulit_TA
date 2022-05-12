# load library
from tkinter import *
import tkinter as tk
import glob
import os
from tkinter import filedialog
import imgaug.augmenters as iaa
from cv2 import cv2
import numpy as np

# windows control
root = tk.Tk()
root.title('Preprocessing Form Detail')
root.geometry('350x120')
root.config(bg='#F2B33D')

# fungsi flip image
def btn_flip_image():
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')

    images = []
    images_path = glob.glob(file_path_variable1 + "/*.jpg")
    for img_path in images_path:
        img = cv2.imread(img_path)
        images.append(img)

    # 2. Image Augmentation
    augmentation = iaa.Sequential([
        # 1. Flip
        iaa.Fliplr(1.0)
    ])

    # 3. Show Images
    augmented_images = augmentation(images=images)

    i=0
    for img in augmented_images:
        cv2.imshow("Image", img)
        
        cv2.imwrite(file_path_variable2 + "/img%03i.jpg" %i, img)
        i +=1
        print("Load image-", i)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cv2.waitKey(0)
    cv2.destroyAllWindows()

# fungsi rotasi image
def btn_rotate_image():
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')

    images = []
    images_path = glob.glob(file_path_variable1 + "/*.jpg")
    for img_path in images_path:
        img = cv2.imread(img_path)
        images.append(img)

    # 2. Image Augmentation
    augmentation = iaa.Sequential([
        # 2. Affine
        iaa.Affine(
            # translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
            rotate=(-8, 8))
    ])

    # 3. Show Images
    augmented_images = augmentation(images=images)
    i=0
    for img in augmented_images:
        cv2.imshow("Image", img)
        
        cv2.imwrite(file_path_variable2 + "/gbr%03i.jpg" %i, img)
        i +=1
        print("Load image-", i)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cv2.waitKey(0)
    cv2.destroyAllWindows()

# fungsi memproses edge detection
def btn_edge_detect():

    i=0
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please Select a Directory Raw Dataset 2')
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

# button control
frame = Frame(root, bg='#F2B33D')

Button(frame, text="Flip Image", command=btn_flip_image).grid(row=0, column=0)
Button(frame, text="Rotate Image", command=btn_rotate_image).grid(row=0, column=1, padx=4, pady=4)
Button(frame, text="Edge Detection Process", command=btn_edge_detect).grid(row=0, column=2)

frame.pack(expand=True) 
root.mainloop()