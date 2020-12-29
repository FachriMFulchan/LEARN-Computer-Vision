import numpy as np
import cv2 as cv


img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')

num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([ [1,0,50], [0,1,50] ])

img_translation = cv.warpAffine(img, translation_matrix, (num_cols+100, num_rows+100), cv.INTER_LINEAR)

cv.imshow('Translation', img_translation)
cv.waitKey()