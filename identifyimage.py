import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
from cv2 import cv2
import tensorflow
from tensorflow.keras.applications import vgg16
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import decode_predictions
import os
from keras.preprocessing import image
import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
from keras.models import model_from_json
from tensorflow import keras
from keras.models import load_model

# kelas kategori wayang -> array
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

# json_file = open('model/wayang_model_new_1.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)

# load weight into model
model_path = 'model/wayang_model_new_1.h5'
wayang_model = tf.keras.models.load_model((model_path),custom_objects={'KerasLayer':hub.KerasLayer})
print("loaded model from disk")

# fungsi load image
def load_img():
    global img, image_data
    # for img_display in frame.winfo_children():
    #     img_display.destroy()

    currdir = os.getcwd()
    image_data = filedialog.askopenfilename(initialdir=currdir, title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))

    # basewidth = 150 # Processing image for dysplaying
    # img = Image.open(image_data)
    img = cv2.imread(image_data)
    # img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # canny edge detection
    img = cv2.Canny(img, 100, 200)
    
    print("Uploaded")
    img = image.load_img(img, target_size=(224,224))
    img = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    # img_preprocessed = preprocess_input(img_batch)

    prediksi = wayang_model.predict(img)
    print(prediksi)
    # print(decode_predictions(prediksi, top=3)[0])

    # cv2.imshow('image', img)
    # cv2.waitKey(10)
    # img = np.reshape(img,[1,224,224,3])
    # # img = image.img_to_array(img)
    # # img = img/255

    # # proba = wayang_model.predict(img.reshape(1,224,224,3))
    # proba = wayang_model.predict(img)
    # top_3 = np.argsort(proba[0])[:-4:-1]
    # for i in range(3):
    #     print("{}".format(wayang_class[top_3[i]])+" ({:.3})".format(proba[0][top_3[i]]))
    # plt.imshow(img)
    # cv2.imshow("akhskas", img)

    # tambahkan code untuk mengkonversi inputan citra menjadi foto dengan ukuran 224x224x3 (sudah edge detectioned)
    # 
    # my code - on progress
    # 
    
    # wpercent = (basewidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    # img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img)
    # file_name = image_data.split('/')
    # panel = tk.Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    # panel_image = tk.Label(frame, image=img).pack()

# fungsi klasifikasi image
def classify():
    # original = Image.open(image_data)
    # original = original.resize((224, 224), Image.ANTIALIAS)
    # numpy_image = img_to_array(original)
    # image_batch = np.expand_dims(numpy_image, axis=0)
    # processed_image = vgg16.preprocess_input(image_batch.copy())
    # predictions = vgg_model.predict(processed_image)
    # label = decode_predictions(predictions)
    # table = tk.Label(frame, text="Top image class predictions and confidences").pack()
    # for i in range(0, len(label[0])):
    #      result = tk.Label(frame,
    #                 text= str(label[0][i][1]).upper() + ': ' + 
    #                        str(round(float(label[0][i][2])*100, 3)) + '%').pack()
    # img=cv2.imread(img)
    img = img_to_array(img)
    img = img/255

    proba = model.predict(img.reshape(1,224,224,3))
    top_3 = np.argsort(proba[0])[:-4:-1]
    for i in range(3):
        print("{}".format(wayang_class[top_3[i]])+" ({:.3})".format(proba[0][top_3[i]]))
    plt.imshow(img)

# call widgets
root = tk.Tk()
root.title('Form Identifikasi Karakter Wayang Kulit')
# root.iconbitmap('class.ico')
root.resizable(False, False)
tit = tk.Label(root, text="Identifikasi Karakter Wayang Kulit - (CNN dan Edge Detection)", bg= '#990000', fg='white', padx=25, pady=6, font=("", 12)).pack()
canvas = tk.Canvas(root, height=500, width=500, bg='#e0301e')
canvas.pack()
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
chose_image = tk.Button(root, text='Choose Image',
                        padx=35, pady=10,
                        fg="black", bg="#ffa500", command=load_img)
chose_image.pack(side=tk.LEFT)
class_image = tk.Button(root, text='Classify Image',
                        padx=35, pady=10,
                        fg="black", bg="#ffa500", command=classify)
class_image.pack(side=tk.RIGHT)
vgg_model = vgg16.VGG16(weights='imagenet')
root.mainloop()