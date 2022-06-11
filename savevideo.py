import numpy as np
import cv2

cap = cv2.VideoCapture(r"D:\Coding\My_Github\VidClass_DeepLearn\testing_vid\video1.mp4")

# Define the codec and create VideoWriter object
# Remember, you might need to change the XVID codec to something else (MPEG?)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('vid5.mp4',fourcc, 20.0, (640,480), True)
# out = cv2.VideoWriter(vidnew.mp4, cv2.VideoWriter_fourcc(*'mp4v'), fps, image_size) 

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.Canny(frame,100,200)
        # frame = cv2.Canny(frame,100,200)       # Single channel. Shape = (640, 480)
        frame = np.expand_dims(frame, axis=-1) # Single channel. Shape = (640, 480, 1)
        frame = np.concatenate((frame, frame, frame), axis=2)
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()