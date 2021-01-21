import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/house.jpg', 1)

#generating the kernels
kernel_emboss_1 = np.array(([0, -1, -1],
                            [1, 0, -1],
                            [1, 1, 0]))  #normalizationnya 0, tapi disatuin

kernel_emboss_2 = np.array(([-1, -1, 0],
                            [-1, 0, 1],
                            [0, 1, 1]))  #samaa

kernel_emboss_3 = np.array(([1, 0, 0],
                            [0, 0, 0],
                            [0, 0, -1]))  #samaa

#converting the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#applying the kernels to the grayscale imageq
#and adding the offset to produce the shadow

output_1 = cv.filter2D(gray_img, -1, kernel_emboss_1) 
output_2 = cv.filter2D(gray_img, -1, kernel_emboss_2) + 128
output_3 = cv.filter2D(gray_img, -1, kernel_emboss_3) + 128

cv.imshow('Input', img)
cv.imshow('Embossing - South West', output_1)
cv.imshow('Embossing - South East', output_2)
cv.imshow('Embossing - North West', output_3)

cv.waitKey()
