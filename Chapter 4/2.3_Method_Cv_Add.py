import numpy as np
import cv2

cap = cv2.VideoCapture(0)

mask = np.zeros((480, 640), np.uint8)
cv2.rectangle(mask, (0,0), (320, 480), (255,255,255), -1)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('kotak', mask)
cv2.imshow('kotak2', mask_inv)



while True:
    ret, frame = cap.read()

    frame1 = cv2.bitwise_and(frame, frame, mask=mask)
    frame2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    frame3 = cv2.add(frame1, frame2)

    cv2.imshow('Frame', frame1)
    cv2.imshow('Frame2', frame2)
    cv2.imshow('Frame3', frame3)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    
cap.release()
cv2.destroyAllWindows()