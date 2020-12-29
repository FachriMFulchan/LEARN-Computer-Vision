import numpy as np
import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/jack.jpeg')

rows, cols = img.shape[:2]

src_points = np.float32([ [0,0], [cols,0], [0,rows]])
dst_points = np.float32([ [0,0], [int(0.6*(cols)),0],  [int(0.4*(cols)), rows]])

affine_matrix = cv.getAffineTransform(src_points, dst_points)
img_output = cv.warpAffine(img, affine_matrix, (cols, rows))

cv.imshow('Input', img)
cv.imshow('Output', img_output)

cv.waitKey()

#Kenapa harus Cols/Rows-1
#Cols atau Rows biasa juga bisaa mereun