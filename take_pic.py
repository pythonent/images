import numpy as np
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    while ret == False:
       print("Can't receive frame. Retrying ...")
       cap.release()
       cap = cv2.VideoCapture(0)                                                                              
       ret, frame = cap.read()


    # Our operations on the frame come here
    
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imwrite("intersection.jpg", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
# When everything done, release the capture
cap.release()