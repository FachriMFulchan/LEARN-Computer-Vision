import numpy as np
import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/sharp.jpg', 1)
rows, cols = img.shape[:2]

kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])
kernel_3x3 = np.ones((3,3), np.float32) / 9.0  #Divide by 9 to normalize the kernel
kernel_5x5 = np.ones((5,5), np.float32) / 25.0 #Divide  by 25 to normalize the kernel



cv.imshow('Orignal Image', img)

#value -1 is to maintain source image depth

output = cv.filter2D(img, -1, kernel_identity) 
cv.imshow('Identity Filter', output)

output = cv.filter2D(img, -1, kernel_3x3)
cv.imshow('3x3 Filter', output)

output = cv.filter2D(img,-1, kernel_5x5)
cv.imshow('5x5 Filter', output)

output = cv.blur(img, (10,10))
cv.imshow('10x10 Blur', output)




cv.waitKey()
