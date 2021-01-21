import numpy as np
import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/leaf.jpg', 1)

#Convert to YUV
img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)

#Equalize y
y,u,v = cv.split(img_yuv)
y_new = cv.equalizeHist(y)
img_yuv = cv.merge((y_new,u,v))

#Convert back to BGR
img_output = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)


cv.imshow('Original', img)
cv.imshow('Enhance', img_output)
cv.waitKey()