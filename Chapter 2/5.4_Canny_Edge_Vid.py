import numpy as np
import cv2 as cv

def nothing(x):
    print (x)

cap = cv.VideoCapture(0)

#Create Trackbar
cv.namedWindow('Tracking')
cv.createTrackbar('th1', 'Tracking', 0, 255, nothing )
cv.createTrackbar('th2', 'Tracking', 0 , 255, nothing)


while True:
    ret, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    th1 = cv.getTrackbarPos('th1', 'Tracking')
    th2 = cv.getTrackbarPos('th2', 'Tracking')

    Canny = cv.Canny(frame_gray, th1, th2)

    cv.imshow('Vid', frame_gray)
    cv.imshow('Canny', Canny)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cv.destroyAllWindows()