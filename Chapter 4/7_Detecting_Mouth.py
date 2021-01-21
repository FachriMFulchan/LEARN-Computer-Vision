import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_mcs_mouth.xml')


if mouth_cascade.empty():
    raise IOError('Unable to Error mouth cascade')

cap = cv2.VideoCapture(0)
ds_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    
    mouth_rects = mouth_cascade.detectMultiScale(frame, scaleFactor=1.7, minNeighbors=11)

    for (x, y, w, h) in mouth_rects:
        y = int(y - 0.15*h) #dikurangin biar naik dikit, kalo y doang jadi agak turun kotaknya
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        
    cv2.imshow('Mouth Detector', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()