# load libraries
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
from sklearn.metrics import multilabel_confusion_matrix

# root window
root = tk.Tk()
root.title('Hasil Identifikasi Wayang Kulit (Image Testing)')
root.geometry('500x800')
root.resizable(False, False)

# frame
frame = ttk.Frame(root)
# field options
opsi = {'padx':5, 'pady':5}

model_path = 'model/wayang_model_new_fix.h5'
wayang_model = tf.keras.models.load_model((model_path),custom_objects={'KerasLayer':hub.KerasLayer})

# define variabel array untuk kelas wayang
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

def load_image(img_path, show=False):

    # akuisisi citra dan ubah ke citra edge, dengan size (224,224)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224,224))
    # cv2.imshow("Gambar", img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 100, 200)
    cv2.imwrite("simpan/citra_uji.jpg", img)

    # ubah citra ke array dh expand_dims
    img = image.load_img("D:/Coding/IdentifikasiWayangKulit_TA/simpan/citra_uji.jpg", target_size=(224, 224))
    img_tensor = image.img_to_array(img)                  # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)       # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                    # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

currdir = os.getcwd()
file_path = filedialog.askdirectory(initialdir=currdir, title='Please Select a Directory Raw Dataset')

#path=os.path.dirname(file_path)

benar = 0
salah = 0

data_akt = []
data_pred = []

for sub_class in os.listdir(file_path):
    sub_fold = os.path.join(file_path,sub_class)
    for images in os.listdir(os.path.join(file_path,sub_fold)):
        
        new_image = load_image(os.path.join(sub_fold, images))

        # check prediction dari citra uji
        pred = wayang_model.predict(new_image)

        if pred is not None:

            # variabel untuk menampung hasil prediksi + presentase kemiripan
            top     = np.argsort(pred[0])[:-4:-1]
            hasil   = "{}".format(wayang_class[top[0]])+" ({:.2})".format(pred[0][top[0]])
            nama_wayang = "{}".format(wayang_class[top[0]])

            data_akt.append(sub_class)
            data_pred.append(nama_wayang)

            # cek apakah nama folder sesuai dengan hasil prediksi
            if sub_class == nama_wayang:
                print('Benar',images, sub_class, hasil)
                benar += 1
            else:
                print('salah',images, sub_class, hasil)
                salah += 1


total = salah+benar
persen = (benar/total)*100

# print('total',total,'akurasi',persen,)
print("data aktual: ",data_akt)
print("\n")
print("data prediksi: ",data_pred)
print("\n")
conf_m = multilabel_confusion_matrix(data_akt, data_pred, labels=wayang_class)
for i in range(22):
    
    TP = conf_m[i][0][0]
    FP = conf_m[i][0][1]
    FN = conf_m[i][1][0]
    TN = conf_m[i][1][1]

    Akurasi = (TP+TN)/(TP+FP+FN+TN)
    Presisi = TP/(TP+FP)
    Recall = TP/(TP+FN)

    print(wayang_class[i]+" | akurasi: {:.2}".format(Akurasi)+" presisi: {:.2}".format(Presisi)+" recall: {:.2}".format(Recall))
    print(conf_m[i])

    tk.Label(root,
        text="Akurasi - " + wayang_class[i] +": {:.2}".format(Akurasi)+" presisi: {:.2}".format(Presisi)+" recall: {:.2}".format(Recall),
        font="Helvetica 12 italic",
        # justify="left",
        fg="black").pack(anchor="w")

root.mainloop()