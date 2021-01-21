import numpy as np
import cv2 as cv 

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/tree.jpg', 1)

#bisa gini
kernel_motion_blur = np.array(([0,0,0],[1,1,1],[0,0,0]))
kernel_motion_blur = kernel_motion_blur/3

#bisa gini
# size = 3
# kernel_motion_blur = np.zeros((size, size))
# kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
# kernel_motion_blur = kernel_motion_blur/size

motion_blur = cv.filter2D(img, -1, kernel_motion_blur)

cv.imshow('Motion Blur', motion_blur)
cv.waitKey()
