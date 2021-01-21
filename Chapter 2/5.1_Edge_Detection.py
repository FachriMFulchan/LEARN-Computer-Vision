'''Sebenernya ada kernelnya buat Edge Detection
cuma biar gampang kita pake method'''


import numpy as np
import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/train.jpg', 0)
rows, cols = img.shape

# It is used depth of cv2.CV_64F
#Kernel size can be: 1, 3, 5, or 7

#Sobel horizontal
sobel_horizontal = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)

#Sobel Vertical
sobel_vertical = cv.Sobel(img, cv.CV_64F, 0 ,1, ksize=3)

#SobelCombine
sobel_combine = cv.bitwise_or(sobel_horizontal, sobel_vertical)

#Laplacian
laplacian = cv.Laplacian(img, cv.CV_64F)


#Canny
canny = cv.Canny(img, 50, 240)

cv.imshow('Original', img)
cv.imshow('Sobel Horizontal', sobel_horizontal)
cv.imshow('Sobel Vertical', sobel_vertical)
cv.imshow('SobelCombine', sobel_combine)
cv.imshow('Laplacian', laplacian)
cv.imshow('Canny', canny)

cv.waitKey()
