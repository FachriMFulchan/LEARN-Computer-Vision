import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')

num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([ [1,0,70], [0,1,110] ])

img_translation = cv.warpAffine(img, translation_matrix, (num_cols, num_rows), cv.INTER_LINEAR)
img_translation2 = cv.warpAffine(img, translation_matrix,(num_cols + 70, num_rows + 110))           #nambah dimensi gambarnya

cv.imshow('Translation', img_translation)
cv.imshow('Translation2', img_translation2)
cv.waitKey()

print (img.shape)
print (num_rows)
print (num_cols)