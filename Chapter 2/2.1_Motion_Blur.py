import cv2 as cv
import numpy as np

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/tree.jpg', 1)
cv.imshow('Original', img)

size = 15
kernel_motion_blur = np.zeros((size, size))                     #bikin matriks zeros dimensi 15x5
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)          #baris ke 7 diisi 1 semuanya
kernel_motion_blur = kernel_motion_blur/size                    #normalization, berapa nilai yang ada satunya aja, engga 225

motionblur= cv.filter2D(img, -1, kernel_motion_blur)
cv.imshow('Motion Blur', motionblur)

blurbiasa = cv.blur(img, (15,15))
cv.imshow('blur biasa', blurbiasa)


cv.waitKey(0)