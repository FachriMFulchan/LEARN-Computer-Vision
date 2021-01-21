import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_eye.xml')

bulat = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\circle.png', 1)


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
        frame_roi = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(frame_roi)
        for (x_eye, y_eye, h_eye, w_eye) in eyes:
            center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
            radius = int(0.3 * (w_eye + h_eye))
            color = (0, 255, 0)
            thickness = 3
            cv2.circle(frame_roi, center, radius, color, thickness)

            roi_eyes = frame_roi[y_eye : y_eye+h_eye, x_eye : x_eye + w_eye]
            bulat_small = cv2.resize(bulat, (x_eye,y_eye))
            
            gray_mask = cv2.cvtColor(bulat_small, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray_mask, 240, 225, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)

            try:
                masked_eye = cv2.bitwise_or(bulat_small, bulat_small, mask=mask)
                # frame = masked_mouth
                masked_frame = cv2.bitwise_and(roi_eyes, roi_eyes, mask=mask_inv)
                frame_roi[y_eye : y_eye+h_eye, x_eye : x_eye + w_eye] = cv2.add(masked_eye, masked_frame)

            except cv2.error as e:
                print('Ignoring arithmetic exception : ' + str(e))
    

    cv2.imshow('Detect eyes', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()