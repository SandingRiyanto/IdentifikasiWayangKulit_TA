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

# root window
root = tk.Tk()
root.title('Hasil Identifikasi Wayang Kulit (Video Testing)')
root.geometry('500x100')
root.resizable(False, False)

# load model .h5
model_path = 'model/wayang_model_new_1.h5'
wayang_model = tf.keras.models.load_model((model_path),custom_objects={'KerasLayer':hub.KerasLayer})
print("loaded model from disk")

# define variabel array untuk kelas wayang
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

# load video testing
capt_vid = cv2.VideoCapture(r"D:\Coding\My_Github\VidClass_DeepLearn\testing_vid\video3.mp4")
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
    frame = cv2.resize(frame, (224, 224).astype("float32"))
    # frame -= mean
    pred = wayang_model.predict(np.expand_dims(frame, axis=0))[0]
    Queue.append(pred)
    