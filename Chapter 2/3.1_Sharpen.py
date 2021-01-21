#Sharpen

import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/tree.jpg', 1)

#Sharpen1
kernel1 = np.array(([-1, -1, -1], [-1, 9, -1], [-1, -1, -1]))  #normalizationnya 1
img_sharp1 = cv.filter2D(img, -1, kernel1)

#Excessive S
kernel2 = np.array(([1, 1, 1], [1, -7, 1], [1, 1, 1]))
img_sharp2 = cv.filter2D(img, -1, kernel2)

#Gaussian kernel sharpen
kernel3 = np.array(([-1, -1, -1, -1, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, 2, 8, 2, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, -1, -1, -1, -1])) / 8.0

img_sharp3 = cv.filter2D(img, -1, kernel3)



cv.imshow('Original', img)
cv.imshow('Common sharpen', img_sharp1)
cv.imshow('Excessive sharpen', img_sharp2)
cv.imshow('Gaussian sharpen', img_sharp3)


cv.waitKey()

