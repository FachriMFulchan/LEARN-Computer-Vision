import cv2 as cv
import numpy as numpy

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/darktrees.png', 0)

#equalize the histogram of the input image
histeq = cv.equalizeHist(img)


cv.imshow('Dark', img)
cv.imshow('Histogram equalized', histeq)
cv.waitKey()