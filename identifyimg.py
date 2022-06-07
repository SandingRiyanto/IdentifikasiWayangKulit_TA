# load any libraries
from tkinter.messagebox import showerror
from keras.preprocessing import image
from keras.models import load_model
from matplotlib.pyplot import text
import matplotlib.pyplot as plt
from tkinter import filedialog
import tensorflow_hub as hub
from pyparsing import col
import tensorflow as tf
from tkinter import ttk
import tkinter as tk
from cv2 import cv2
import numpy as np
import os

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
print("loaded model from disk")

# define variabel array untuk kelas wayang
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

tk.Label(root,
        text="Hasil Identifikasi dari tokoh wayang:",
        font="Helvetica 14 bold italic",
        fg="black").pack()

# proses image untuk siap diprediksi
def load_image(img_path, show=False):
    img = cv2.imread(img_path)
    cv2.imshow("Gambar", img)
    # img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

def identifikasi_lagi():
    # return root.destroy() AND
    # import identifyimg			# initial import of my_module

    from importlib import reload 	
    identifyimg = reload(identifyimg)
# if __name__ == "__main__":

# image path
currdir = os.getcwd()
img_path = filedialog.askopenfilename(initialdir=currdir, title="Choose an image", filetypes=(("all files", "*.*"), ("png files", "*.png")))

# load a single image atau call function
new_image = load_image(img_path)

# check prediction
pred = wayang_model.predict(new_image)

print(pred)

# top_3 = np.argsort(pred[0])[:-4:-1]

top = np.argsort(pred[0])[:-4:-1]

# menampilkan 3 prediksi tertinggi
# for i in range(3):
#     print("{}".format(wayang_class[top_3[i]])+" ({:.3})".format(pred[0][top_3[i]]))

# print("{}".format(wayang_class[top[0]])+" ({:.3})".format(pred[0][top[0]]))
# plt.imshow(new_image)

hasil = "{}".format(wayang_class[top[0]])+" ({:.3}) %".format(pred[0][top[0]])
print(hasil)

# tk.Label(root,
#         text="Hasil Identifikasi dari tokoh wayang:",
#         font="Helvetica 14 bold italic",
#         fg="black").pack()

tk.Label(root, 
		 text=hasil,
		 fg = "blue",
		 font = "Verdana 12 bold").pack()


# Button(frame, text="Identify Image Again", command=identifikasi_lagi).grid(row=0, column=0)
# frame.pack(expand=True) 

button1 = ttk.Button(root, text='Identify Again', command=identifikasi_lagi, width=100)
button1.pack(padx=5, pady=5, ipady=3)

# start the app
root.mainloop()