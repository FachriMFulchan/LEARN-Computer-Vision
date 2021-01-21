import cv2
import numpy as np


input_image = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/duck.jpg')
cv2.imshow('input', input_image)

#Reduce Size
res1 = cv2.resize(input_image, (480,480), interpolation=cv2.INTER_AREA)
cv2.imshow('resize', res1)

#Extend size
res2 = cv2.resize(input_image, (1080, 480), interpolation=cv2.INTER_AREA)
cv2.imshow('resize', res2)



cv2.waitKey()


#Nah resize manual gini kann, si bebeknya jadi ikut ngeresize
#gimana caranya bebeknya gaikut ngeresize juga
#itulah gunanya seam carving