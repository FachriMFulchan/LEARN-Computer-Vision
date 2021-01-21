'''Nah ini gapake gray
gapake ROI
hasinya sama aja cuma lebih banyak noise nya'''

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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes= eye_cascade.detectMultiScale(frame)
    for (x_eye, y_eye, w_eye, h_eye) in eyes:
            center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
            radius = int(0.3 * (w_eye + h_eye))
            color = (0,255,0)
            thickness = 3
            cv2.circle(frame, center, radius, color, thickness)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()