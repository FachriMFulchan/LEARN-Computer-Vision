import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/logo.png', 0)

cv.imshow('image', img)
cv.imwrite('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/logogray.png', img)
cv.waitKey()

