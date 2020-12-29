import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/jack.jpeg')

rows, cols = img.shape[:2]

src_points = np.float32([ [0,0], [cols,0], [0, rows], [cols, rows] ])
dst_points = np.float32([ [0,0], [cols,0], [int(0.33*cols), rows], [int(0.66*cols), rows] ])

projective_matrix = cv.getPerspectiveTransform(src_points, dst_points)
img_output = cv.warpPerspective(img, projective_matrix, (cols, rows))

cv.imshow('Input', img)
cv.imshow('Output', img_output)
cv.waitKey()