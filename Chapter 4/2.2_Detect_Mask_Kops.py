import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_frontalface_default.xml')
face_mask = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\mask.jpg')
h_mask, w_mask = face_mask[:2]

if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

cap = cv2.VideoCapture(0)
scalling_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_AREA)

    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)

    for (x,y,w,h) in face_rects:
        if h <=0 or w <= 0: pass

        #Posisi si masker dimana
        h, w = int(1.0*h), int(1.0*w)
        y -= int(-0.2*h)  #koordinatnya dikebawahin, biar ga tengah, masker kan dibawah ya kan
        x = int(x)

        #Extract region of interest from the image
        frame_roi = frame[y:y+h, x:x+w]   #ROI mukaa
        face_mask_small = cv2.resize(face_mask, (w,h), interpolation=cv2.INTER_AREA) #maskernnya di sesuain sama ROI frame nya (w dan h)

        #Convert color image to grayscale and threshold it
        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_mask, 180, 255, cv2.THRESH_BINARY_INV)

        #Create an inverse mask
        mask_inv = cv2.bitwise_not(mask) #item jadi putih dan sebaliknya


        try:
            #Mask -- untuk dapet ROI dari masker nya
            masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask) #biasanya kalo masking and or kadang2 sama
            
            #MaskInv -- untuk dapet muka selain masker
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            
            #Ditambah dan diterapin di ROI aja
            frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)


        except cv2.error as e :
            print ('Ignoring arithmetix exceptions :' + str(e))

        #ditambahin wee
        
    cv2.imshow('face', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
        
