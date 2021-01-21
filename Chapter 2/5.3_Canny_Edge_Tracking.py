import numpy as np
import cv2 as cv


img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/train.jpg', 0)

def nothing(x):
    print (x)

#CreateTrackbar
cv.namedWindow('Tracking')
cv.createTrackbar('th1', 'Tracking', 0, 255, nothing )
cv.createTrackbar('th2', 'Tracking', 0, 255, nothing )



while True:
    th1 = cv.getTrackbarPos('th1', 'Tracking')
    th2 = cv.getTrackbarPos('th2', 'Tracking')

    canny = cv.Canny(img, th1, th2)

    cv.imshow('Original', img)
    cv.imshow('Canny Edge', canny)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

cv.destroyAllWindows()