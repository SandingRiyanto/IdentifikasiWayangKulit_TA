# load library
from cv2 import cv2
import numpy as np
from keras.models import model_from_json
import tensorflow as tf
import tensorflow_hub as hub
from keras.models import load_model

# load model .h5
model_path = 'model/wayang_model_new_1.h5'
wayang_model = tf.keras.models.load_model((model_path),custom_objects={'KerasLayer':hub.KerasLayer})
print("loaded model from disk")

# define variabel array untuk kelas wayang
wayang_class = ["abimanyu", "anoman", "arjuna", "bagong", "baladewa", "bima", "buta", "cakil", "durna", "dursasana", "duryudana",
                "gareng", "gatotkaca", "karna", "kresna", "nakula_sadewa", "patih_sabrang", "petruk", "puntadewa", "semar", "sengkuni", "togog"
]

# start load video test
cap = cv2.VideoCapture("testing_vid\video3.mp4")
while True:
    # find haar-cascade to draw bounding box arround face -> wayang
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    if not ret:
        break
    # face_detector = cv2.CascadeClassifier('opencv_xml\haarcascade_eye.xml') #ganti dg deteksi objek wayang (mgkin)
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # detect face available on cam
    # num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # take each face available on cam and process
    for(x,y,w,h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0,255,0), 2)
        roi_fray_frame = gray_frame[y:y+h, x:x+w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_fray_frame, (48,48)), -1), 0)
        
        # predict!
        wayang_predictions = wayang_model.predict(cropped_img)
        maxindex = int(np.argmax(wayang_predictions))
        cv2.putText(frame, wayang_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_4)
         
    cv2.imshow('wayang detect', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()