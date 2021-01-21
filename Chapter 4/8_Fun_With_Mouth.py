import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_mcs_mouth.xml')
moustache_mask = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\moustache3.png', 1)

if mouth_cascade.empty():
    raise IOError('Unable to load mouth cascade')

cap = cv2.VideoCapture(0)
scalling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_AREA)

    mouth_rects = mouth_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

    if len(mouth_rects) > 0:
        (x,y,w,h) = mouth_rects[0]
        h, w = int(0.6*h), int(1.2*w)
        x -= int(0.05*w)
        y -= int(0.55*h)
        frame_roi = frame[y:y+h, x:x+w]

        moustache_mask_small = cv2.resize(moustache_mask, (w,h), interpolation=cv2.INTER_AREA)
        
        
        gray_mask = cv2.cvtColor(moustache_mask_small, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_mask, 180, 225, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        
        try:
            masked_mouth = cv2.bitwise_or(moustache_mask_small, moustache_mask_small, mask=mask)
            # frame = masked_mouth
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            frame[y:y+h, x:x+w] = cv2.add(masked_mouth, masked_frame)

        except cv2.error as e:
            print('Ignoring arithmetic exception : ' + str(e))
    
    cv2.imshow('Moustache', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()