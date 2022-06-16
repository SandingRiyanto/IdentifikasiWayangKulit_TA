# load any libraries
from tkinter.messagebox import showerror
from keras.preprocessing import image
from keras.models import load_model
from matplotlib.pyplot import text
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import messagebox
import tensorflow_hub as hub
from pyparsing import col
import tensorflow as tf
from tkinter import ttk
import tkinter as tk
from cv2 import cv2
import numpy as np
import os
from sklearn.metrics import confusion_matrix
from PIL import Image, ImageFilter

# root window
root = tk.Tk()
root.title('Hasil Identifikasi Wayang Kulit (Image Testing)')
root.geometry('500x100')
root.resizable(False, False)

# frame
frame = ttk.Frame(root)
# field options
opsi = {'padx':5, 'pady':5}

# load model .h5
model_path = 'model/wayang_model_new_1.h5'
wayang_model = tf.keras.models.load_model((model_path),custom_objects={'KerasLayer':hub.KerasLayer})
# print("loaded model from disk")

# define variabel array untuk kelas wayang
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

# menampilkan label
tk.Label(root,
        text="Hasil Identifikasi:",
        font="Helvetica 14 bold italic",
        fg="black").pack()

# fungsi: me-load image testing dan mengubahnya ke dalam array dims
def load_image(img_path, show=False):
    img = cv2.imread(img_path)

    # coba ya

    # img = image.load_img(img_path, target_size=(224, 224))
    # img.show()
    img = cv2.resize(img, (224,224))
    cv2.imshow("Gambar", img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # img = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
    img = cv2.Canny(img, 100, 200)
    
    cv2.imwrite("simpan.jpg", img)
    # print(type(img))

    currdir = os.getcwd()
    img_path2= filedialog.askopenfilename(initialdir=currdir, title="Choose an image", filetypes=(("all files", "*.*"), ("png files", "*.png")))
    
    img = image.load_img(img_path2, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

# mengunggah image testing dari directory
currdir = os.getcwd()
img_path = filedialog.askopenfilename(initialdir=currdir, title="Choose an image", filetypes=(("all files", "*.*"), ("png files", "*.png")))


# mengambil (get) nama base directory
path=os.path.dirname(img_path)
nama_folder = os.path.basename(path)

# load a single image atau call function
new_image = load_image(img_path)

# check prediction
pred = wayang_model.predict(new_image)

if pred is not None:
    # tampilkan
    print(pred)

    top = np.argsort(pred[0])[:-4:-1]

    # top_3 = np.argsort(pred[0])[:-4:-1]

    # menampilkan 3 prediksi tertinggi
    # for i in range(3):
    #     print("{}".format(wayang_class[top_3[i]])+" ({:.3})".format(pred[0][top_3[i]]))

    # print("{}".format(wayang_class[top[0]])+" ({:.3})".format(pred[0][top[0]]))
    # plt.imshow(new_image)

    hasil = "{}".format(wayang_class[top[0]])+" ({:.2})".format(pred[0][top[0]])
    # print(hasil)
    nama_wayang = "{}".format(wayang_class[top[0]])
    # cek apakah nama folder sesuai dengan hasil prediksi
    if nama_folder == nama_wayang:
        # print("ya, betul")

        # show hasil
        tk.Label(root, 
            text=hasil,
            fg = "blue",
            font = "Verdana 12 bold").pack()
        messagebox.showinfo("Show Info", "BENAR! Data Uji benar diidentifikasi")
        button1 = ttk.Button(root, text='Identify Again', command=root.destroy, width=80).pack(pady=10)
    else:
        print("tidak, salah")

        # show hasil
        tk.Label(root, 
            text=hasil,
            fg = "red",
            font = "Verdana 12 bold").pack()
        messagebox.showinfo("Show Info", "SALAH! Data Uji salah diidentifikasi")
        button2 = ttk.Button(root, text='Identify Again', command=root.destroy, width=80).pack(pady=10)

# start the app
root.mainloop()