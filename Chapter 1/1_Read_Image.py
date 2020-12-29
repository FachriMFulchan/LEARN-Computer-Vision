import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/logo.png')

print (type(img))
cv.imshow('image', img)
cv.waitKey(0)
