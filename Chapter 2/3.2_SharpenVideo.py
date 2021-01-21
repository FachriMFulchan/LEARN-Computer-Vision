import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
kernel1 = np.array(([-1, -1, -1], [-1, 9, -1], [-1, -1, -1]))
kernel2 = np.array(([1,1,1], [1,-7,1], [1,1,1]))
kernel3 = np.array(([-1,-1,-1,-1,-1],
                        [-1,2,2,2,-1],
                        [-1,2,8,2,-1],
                        [-1,2,2,2,-1],
                        [-1,-1,-1,-1,-1])) /8.0

while True :
    ret, frame = cap.read()
    sharpen1 = cv.filter2D(frame, -1, kernel1)
    sharpen2 = cv.filter2D(frame, -1, kernel2)
    sharpen3 = cv.filter2D(frame, -1, kernel3)

    cv.imshow('Frame', frame)
    cv.imshow('Sharpen1', sharpen1)
    cv.imshow('Sharpen2', sharpen2)
    cv.imshow('Sharpen3', sharpen3)

    k = cv.waitKey(1)
    if k == ord ('q'):
        break

cap.release
cv.destroyAllWindows()