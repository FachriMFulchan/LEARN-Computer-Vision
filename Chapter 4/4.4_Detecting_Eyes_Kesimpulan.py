'''Sebenernya
GRAY --> fungsinya buat apa sii gatau, jadi gausah dipake laa (gapake)
ROI --> biar deteksi matanya ga se frame, semuka aja, nge reduce noise juga (pake)
jadi code yang paling simple nya ini nih menurut urg'''

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_eye.xml')

if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

if eye_cascade.empty():
    raise IOError('Unable to load the eye cascade classifier xml file')


cap = cv2.VideoCapture(0)
ds_factor = 0.5


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)

    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)

    for (x,y,w,h) in face_rects:
        roi = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi)
        for (x_eyes, y_eyes, w_eyes, h_eyes) in eyes:
            center = (int(x_eyes + 0.5*w_eyes), int(y_eyes + 0.5*h_eyes))
            radius = int(0.3 * (w_eyes + h_eyes))
            color = (0, 255, 0)
            thickness = 3
            cv2.circle(roi, center, radius, color, thickness)

            '''Kenapa bikin circle nya di ROI tapi kebaca juga di frame??
            karena ini ada di looping face rects yang punyanya si FRAME
            jadi walaupun udh dimasukin ke variable baru
            tetep aja di frame juga muncul'''
    
    cv2.imshow('Detect Eyes', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()