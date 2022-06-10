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
from collections import deque
from imutils import paths
# root window
root = tk.Tk()
root.title('Hasil Identifikasi Wayang Kulit (Video Testing)')
root.geometry('500x100')
root.resizable(False, False)

# load model .h5
model_path = 'model/wayang_model_new_1.h5'
wayang_model = tf.keras.models.load_model((model_path),custom_objects={'KerasLayer':hub.KerasLayer})
print("loaded model from disk")
output = r"D:\Coding\My_Github\VidClass_DeepLearn\keluaran"
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
Queue = deque(maxlen=128)

# define variabel array untuk kelas wayang
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

# load video testing
capt_vid = cv2.VideoCapture(r"D:\Coding\My_Github\VidClass_DeepLearn\testing_vid\video1.mp4")
writer = None
(Width, Height) = (None, None)

while True:
    (taken, frame) = capt_vid.read()

    if not taken:
        break
    if Width is None or Height is None:
        (Width, Height) = frame.shape[:2]
    
    output = frame.copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (224, 224))
    # frame /= 255.
    # frame = mean
    pred = wayang_model.predict(np.expand_dims(frame, axis=0))
    top = np.argsort(pred[0])[:-4:-1]
    # top_3 = np.argsort(pred[0])[:-4:-1]
    text = []
    # menampilkan 3 prediksi tertinggi
    # for i in range(3):
    #     text="{}".format(wayang_class[top_3[i]])+" ({:.3})".format(pred[0][top_3[i]])
    #     print(text)
    # Queue.append(pred)
    # print(pred)
    # hasil = np.array(Queue).mean(axis=0)
    # i = np.argmax(hasil)
    # label = wayang_class[i]
    # text = "Ini wayang : {}".format(label)
    text = "{}".format(wayang_class[top[0]])

    print(text)
    cv2.putText(output, text, (45,60), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (255, 0, 0))
    cv2.imshow("Hasil", output)
    cv2.waitKey(5)
    # pahami konsep video prediction ya!