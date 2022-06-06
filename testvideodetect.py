# load library
from cv2 import cv2
import numpy as np
from keras.models import model_from_json

# create dict from label images
wayang_dict = {0:"abimanyu", 1:"anoman", 2:"arjuna", 3:"bagong", 4:"baladewa", 5:"bathara_guru", 6:"bathara_indra", 7:"bathara_kala",
            8:"bathara_narada", 9:"bima", 10:"buta", 11:"cakil", 12:"durna", 13:"dursasana", 14:"duryudana", 15:"gareng", 16:"gatotkaca",
            17:"karna", 18:"kresna", 19:"nakula_sadewa", 20:"patih_sabrang", 21:"petruk", 22:"puntadewa", 23:"semar", 24:"sengkuni",
            25:"togog"
}

# load json and create model
json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
wayang_model = model_from_json(loaded_model_json)

# load weight into model
wayang_model.load_weights("model/model.h5")
print("loaded model from disk")

# start load video test
cap = cv2.VideoCapture("directory video...")
while True:
    # find haar-cascade to draw bounding box arround face -> wayang
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    if not ret:
        break
    face_detector = cv2.CascadeClassifier('opencv_xml\haarcascade_eye.xml') #ganti dg deteksi objek wayang (mgkin)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect face available on cam
    num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

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