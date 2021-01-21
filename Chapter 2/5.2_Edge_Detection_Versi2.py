'''Tadi kan sobel, sama laplaciannya ga di absolutin
sekarang coba kita absolutin'''

import numpy as np
import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/train.jpg', 0)

#Sobel Horizontal
SobelX = cv.Sobel(img, cv.CV_64F,1, 0, ksize=3)
cv.imshow('SobelX1', SobelX) #bandingkannnnn
SobelX = np.uint8(np.absolute(SobelX))

#Sobel Vertical 
SobelY = cv.Sobel(img, cv.CV_64F, 0, 1 , ksize=3)
SobelY = np.uint8(np.absolute(SobelY))

#Sobel Combine
SobelCombine = cv.bitwise_or(SobelX, SobelY)

#Laplacian
laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)
laplacian = np.uint8(np.absolute(laplacian))

#Canny
canny = cv.Canny(img, 50, 240)

cv.imshow('SobelX', SobelX)
cv.imshow('SobelY', SobelY)
cv.imshow('SobelCombine', SobelCombine)
cv.imshow('Laplacian', laplacian)
cv.imshow('Canny', canny)
cv.waitKey()