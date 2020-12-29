import numpy as np
import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')

num_rows, num_cols = img.shape[:2]

translation_matrix = np.float32([ [1,0,int(0.5*num_cols)], [0,1,int(0.5*num_rows)] ])
rotation_matrix = cv.getRotationMatrix2D((num_cols, num_rows), 30, 1)


img_translation = cv.warpAffine(img, translation_matrix, (2*num_cols, 2*num_rows))
img_rotation = cv.warpAffine(img_translation, rotation_matrix, (2*num_cols, 2*num_rows))

cv.imshow('Translation', img_rotation)
cv.waitKey()