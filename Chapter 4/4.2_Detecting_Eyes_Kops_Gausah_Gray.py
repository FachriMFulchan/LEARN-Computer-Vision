'''Nah ini versi yang gausah pake gray'''


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
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)


    for (x,y,w,h) in face_rects:
        roi_color = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

        eyes = eye_cascade.detectMultiScale(roi_color)
        for (x_eye, y_eye, w_eye, h_eye) in eyes:
            center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
            radius = int(0.3 * (w_eye + h_eye))
            color = (0,255,0)
            thickness = 3
            cv2.circle(roi_color, center, radius, color, thickness)

            '''yang aneh adalah, kenapa sifat roi color bisa masuk ke frame
            karena dari awal detectmultiscale nya adalah frame
            jadi apapun yang ada di dalam for ini
            bakal ngaruh ke frame'''

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()