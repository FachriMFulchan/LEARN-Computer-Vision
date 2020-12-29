import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/logo.png', 1)

cv.imshow('image', img)
cv.imwrite('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/logojpg2.png', img, [cv.IMWRITE_JPEG2000_COMPRESSION_X1000] )

cv.waitKey()