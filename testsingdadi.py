from cv2 import cv2
import os
from keras.preprocessing import image
from tkinter import filedialog
import numpy as np

img = cv2.imread("dataset/raw_dataset/arjuna/arjuna003.jpg")
# cv2.imshow("Gambar", img)

# coba ya

# img = image.load_img(img_path, target_size=(224, 224))
# img.show()
# img = cv2.resize(img, (224,224))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
img = cv2.Canny(img, 100, 200)
# print(type(img))
cv2.imwrite("simpan.jpg", img)

currdir = os.getcwd()
img_path = filedialog.askopenfilename(initialdir=currdir, title="Choose an image", filetypes=(("all files", "*.*"), ("png files", "*.png")))

img = image.load_img(img_path, target_size=(224, 224))
img_tensor = image.img_to_array(img)                    # (height, width, channels)
img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
img_tensor /= 255.

print(img_tensor)