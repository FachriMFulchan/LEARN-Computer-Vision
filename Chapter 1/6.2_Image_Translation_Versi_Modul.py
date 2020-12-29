import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')

num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([ [1,0,70], [0,1,110] ])

img_translation = cv.warpAffine(img, translation_matrix, (num_cols, num_rows))

translation_matrix = np.float32([ [1,0,-30], [0,1,-50] ])
img_translation = cv.warpAffine(img_translation, translation_matrix, (num_cols+70+30, num_rows+110+50))


cv.imshow('Translation', img_translation)
cv.waitKey()


#kalo negatif jadi ngurangin lagi,
#maksudnya mendekati posisi awal