import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')


cv.imshow('Original Image', img)

#Linear Interpolation
img_scaled = cv.resize(img, None, fx=1.2, fy=1.2, interpolation=cv.INTER_LINEAR)
cv.imshow('Scalling - Linear Interpolation', img_scaled)


# Cubic Interpolation
img_scaled = cv.resize(img, None, fx=1.2, fy=1.2, interpolation=cv.INTER_CUBIC)
cv.imshow('Scalling - Cubic Interpolation', img_scaled)
#secara kasat mata bagusan yang cubic dibanding linear


#Skewed size
img_scaled = cv.resize(img, (450,450), interpolation=cv.INTER_AREA)
cv.imshow('Scalling - Skewed Size', img_scaled)


cv.waitKey()