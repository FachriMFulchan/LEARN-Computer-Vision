'''Perbedaan antara Bilateral Filter
dan Gaussian Filter'''

import numpy as np
import cv2

img = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/carpet.jpg', 1)

#Gaussian
img_gaussian = cv2.GaussianBlur(img, (13,13), 0)

img_bilateral = cv2.bilateralFilter(img, 13, 70, 100)


cv2.imshow('Image', img)
cv2.imshow('Gaussian Filter', img_gaussian)
cv2.imshow('Bilateral Filter', img_bilateral)
cv2.waitKey(0)
