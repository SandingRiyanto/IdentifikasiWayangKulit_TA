# load library
import imgaug.augmenters as iaa
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from cv2 import cv2
import numpy as np
import glob
import os

# windows control
root = tk.Tk()
root.title('Preprocessing Form Detail')
root.geometry('540x120')
root.config(bg='#F2B33D')

# label = judul skripsi
labelJudul = tk.Label(root,
        borderwidth = 2,
        width = 540,
        # wraplength=120,
        relief="ridge",
        font=("Helvetica", 12),
        text="FORM PRE-PROCESSING IMAGES")

labelJudul.pack(ipadx=5, ipady=5, pady=5)

# fungsi flip lr image
def btn_fliplr_image():
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')

    images = []
    images_path = glob.glob(file_path_variable1 + "/*.*")
    for img_path in images_path:
        img = cv2.imread(img_path)
        images.append(img)

    augmentation = iaa.Sequential([
        iaa.Fliplr(1.0)
    ])

    # Show and Save Images
    augmented_images = augmentation(images=images)

    i=0
    x=0
    for img in augmented_images:
        cv2.imshow("Image", img)
        
        cv2.imwrite(file_path_variable2 + "/img%03i.jpg" %i, img)

        i +=1
        sum_img = x + i
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cv2.waitKey(0)

    messagebox.showinfo("Show Info", "Gambar Berhasil di-flip LR!")
    print("Total Image Setelah di Flip LR: ", sum_img)
    cv2.destroyAllWindows()

# fungsi flip ud image
def btn_flipud_image():
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')

    images = []
    images_path = glob.glob(file_path_variable1 + "/*.jpg")
    for img_path in images_path:
        img = cv2.imread(img_path)
        images.append(img)

    augmentation = iaa.Sequential([
        iaa.Flipud(1.0)
    ])

    # Show and Save Images
    augmented_images = augmentation(images=images)

    i=0
    y=0
    for img in augmented_images:
        cv2.imshow("Image", img)
        
        cv2.imwrite(file_path_variable2 + "/citra%03i.jpg" %i, img)
        
        i +=1
        sum_img = y + i

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cv2.waitKey(0)
    
    messagebox.showinfo("Show Info", "Gambar Berhasil di-flip UD!")
    print("Total Image Setelah di Flip UD: ", sum_img)
    cv2.destroyAllWindows()

# fungsi rotasi image
def btn_rotate_image():
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')

    images = []
    images_path = glob.glob(file_path_variable1 + "/*.*")
    for img_path in images_path:
        img = cv2.imread(img_path)
        images.append(img)

    augmentation = iaa.Sequential([
        iaa.Affine(translate_px={"x": (-20, 20), "y": (-20, 20)},
            rotate=(-25, 25))
    ])

    # 3. Show and Save Images
    augmented_images = augmentation(images=images)

    i=0
    z=0
    for img in augmented_images:
        cv2.imshow("Image", img)
        
        cv2.imwrite(file_path_variable2 + "/gbr%03i.jpg" %i, img)

        i +=1
        sum_img = z + i

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cv2.waitKey(0)

    messagebox.showinfo("Show Info", "Gambar Berhasil dirotasi!")
    print("Total Image Setelah Dirotasi: ", sum_img)
    cv2.destroyAllWindows()

# fungsi zoom images
def btn_zoomin_image():
    currdir = os.getcwd()
    file_path_variable1 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    file_path_variable2 = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to Save')

    images = []
    images_path = glob.glob(file_path_variable1 + "/*.*")
    for img_path in images_path:
        img = cv2.imread(img_path)
        images.append(img)

    augmentation = iaa.Sequential([
        iaa.Affine(
        scale={"x": (0.4, 1.0), "y": (0.8, 1.2)})
    ])

    # 3. Show and Save Images
    augmented_images = augmentation(images=images)

    i=0
    a=0
    for img in augmented_images:
        cv2.imshow("Image", img)
        
        cv2.imwrite(file_path_variable2 + "/ctr%03i.jpg" %i, img)

        i +=1
        sum_img = a + i

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cv2.waitKey(0)
    
    messagebox.showinfo("Show Info", "Gambar Berhasil di-zoom!")
    print("Total Image Setelah Di-zoom: ", sum_img)
    cv2.destroyAllWindows()

# fungsi memproses edge detection
def btn_edge_detect():

    i=0
    j=0
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
        sum_img = j + i
        
        cv2.imshow('image', ImgEdge)
        cv2.waitKey(10)

    messagebox.showinfo("Show Info", "Gambar Berhasil di-deteksi tepi. Ready to use!")
    print("Total keseluruhan image (ready):", sum_img)
    cv2.destroyAllWindows()

# button control
frame = Frame(root, bg='#F2B33D')

Button(frame, text="Flip LR Images", command=btn_fliplr_image).grid(row=0, column=0)
Button(frame, text="Flip UD Images", command=btn_flipud_image).grid(row=0, column=1, padx=4, pady=4)
Button(frame, text="Rotate Images", command=btn_rotate_image).grid(row=0, column=2, padx=4, pady=4)
Button(frame, text="Zoom-In Images", command=btn_zoomin_image).grid(row=0, column=3, padx=4, pady=4)
Button(frame, text="Edge Detection Process", command=btn_edge_detect).grid(row=0, column=4)

frame.pack(expand=True) 
root.mainloop()