import cv2, os, glob, re
import numpy as np
target_dir = "D:\Coding\My_Github\VidClass_DeepLearn\testing_vid"

fps = 30
width = 320
height = 240

os.chdir(target_dir)
print ("Detecting valid files for conversion...")

for file in glob.glob("*mp4"):
    print("Converting file: "+file)

    #Find the name of the file
    output_filename = re.sub("-RAW\.h264","", file)

    #Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc,fps,(width,height))

    #create capture stream object on which to modify
    cap_stream = cv2.VideoCapture(file)
    while(cap_stream.isOpened()):
        # Take each frame
        ret, frame = cap_stream.read()

        if ret == True:
            #flip the frame
            frame = cv2.flip(frame,0)

            # modify the arguments for cv2.Canny to change thresh values
            edges = cv2.Canny(frame,100,200)

            #print modified frame
            cv2.imshow('edges',edges)

            #print original frame
            #cv2.imshow('frame',frame)

            out.write(edges)

            # if waitkey() returns anything other than -1, and error may have occurred. abort
            if cv2.waitKey(10) >= 0:
                break
        else:
            print ("Finishing conversion...")
            break

    # release and clean up streams
    print ("Created output_filename.avi")

    cap_stream.release()
    out.release()