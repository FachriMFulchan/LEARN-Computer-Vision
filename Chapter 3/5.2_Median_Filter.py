import cv2
import numpy as np

img = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/pepper.jpg', 1)

cv2.imshow('Image', img)
output = cv2.medianBlur(img, ksize=7)
cv2.imshow('After Filter', output)
cv2.waitKey()
