import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_frontalface_default.xml')
face_mask = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\mask.jpg')

if  face_cascade.empty():
    raise IOError('Unable to Load')

cap = cv2.VideoCapture(0)
scalling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_AREA)

    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
    
    for (x,y,w,h) in face_rects:
        if h <= 0 or w <0: pass  #buat reduce noise

        #posisi ROI
        h, w = int(h), int(w)
        y -= int(-0.2*h)
        x = int(x)

        #Buat ROI, Resize mask
        frame_roi = frame[y:y+h, x:x+w]
        face_mask_small = cv2.resize(face_mask, (w,h), interpolation=cv2.INTER_AREA)
        
        #Convert ke grayscale terus di threshold
        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_mask, 180, 255, cv2.THRESH_BINARY_INV)
        
        #Inverse mask
        mask_inv = cv2.bitwise_not(mask)


        try:
            #Mask -- buat dapet maskernya
            masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask)

            #Mask_inv -- buat dapet selain masker
            mask_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)

            frame[y:y+h, x:x+w] = cv2.add(masked_face, mask_frame)

        except cv2.error as e:
            print('Ignoring arithmetic exception : ' + str(e))

    
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()