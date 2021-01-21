import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)
scalling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv.resize(frame, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv.INTER_AREA)

    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)

    for (x,y,w,h) in face_rects:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 3) #y+h ditambah semakin kebawah

    cv.imshow('Face Detection', frame)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()