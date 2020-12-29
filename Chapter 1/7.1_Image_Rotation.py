import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')

num_rows, num_cols = img.shape[:2]
rotation_matrix = cv.getRotationMatrix2D(( num_cols/2, num_rows/2 ), 30, 0.7)

img_rotation = cv.warpAffine(img, rotation_matrix, (num_cols, num_rows))
cv.imshow('Rotation', img_rotation)
cv.waitKey()
