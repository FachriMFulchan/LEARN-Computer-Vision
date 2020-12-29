import numpy as np
import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/jack.jpeg')

rows, cols = img.shape[:2]

src_points = np.float32([ [0,0], [0, rows], [cols/2, 0], [cols/2, rows]])
dst_points = np.float32([ [0,100], [0, rows-100], [cols/2,0], [cols/2, rows] ])

projective_matrix = cv.getPerspectiveTransform(src_points, dst_points)
img_output = cv.warpPerspective(img, projective_matrix, (cols, rows))

cv.imshow('Input', img)
cv.imshow('Output', img_output)
cv.waitKey()