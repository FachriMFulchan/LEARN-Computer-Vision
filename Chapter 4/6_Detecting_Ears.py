'''ini file xml nya gabener
cari lagi yang lain wokee
tapi dah dicari tapi susahh tetep gaada'''

import cv2
import numpy as np

left_ear_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_mcs_leftear.xml')
right_ear_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_mcs_rightear.xml')

if left_ear_cascade.empty():
    raise IOError('Unable to load the left cascade classifier')

if right_ear_cascade.empty():
    raise IOError('Unable to load the right cascade classifier')

cap = cv2.VideoCapture(0)
scalling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_AREA)

    left_ear = left_ear_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
    right_ear = right_ear_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)

    for (x,y,w,h) in left_ear:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    
    for (x,y,w,h) in right_ear:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
    
    cv2.imshow('Ear Detector', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()