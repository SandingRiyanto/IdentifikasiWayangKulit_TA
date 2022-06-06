# load_model_sample.py
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import tensorflow_hub as hub
from tkinter import filedialog
from cv2 import cv2

# load model .h5
model_path = 'model/wayang_model_new_1.h5'
wayang_model = tf.keras.models.load_model((model_path),custom_objects={'KerasLayer':hub.KerasLayer})
print("loaded model from disk")

# define variabel array
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

# proses image untuk siap diprediksi
def load_image(img_path, show=False):
    img = cv2.imread(img_path)
    cv2.imshow("jakajk", img)
    # img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

# if __name__ == "__main__":

# image path
currdir = os.getcwd()
img_path = filedialog.askopenfilename(initialdir=currdir, title="Choose an image",
                                    filetypes=(("all files", "*.*"), ("png files", "*.png")))

# load a single image
new_image = load_image(img_path)

# check prediction
pred = wayang_model.predict(new_image)

print(pred)

# top_3 = np.argsort(pred[0])[:-4:-1]

top = np.argsort(pred[0])[:-4:-1]

# for i in range(3):
#     print("{}".format(wayang_class[top_3[i]])+" ({:.3})".format(pred[0][top_3[i]]))

# print("{}".format(wayang_class[top[0]])+" ({:.3})".format(pred[0][top[0]]))
# plt.imshow(new_image)

hasil = "{}".format(wayang_class[top[0]])+" ({:.3})".format(pred[0][top[0]])
print(hasil)

