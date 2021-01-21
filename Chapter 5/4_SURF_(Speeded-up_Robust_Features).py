'''Gabisaaa
Gaada Method cv2.SURF
karena no longer availabe di opencv 3'''


import cv2
import numpy as np


input_image = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/fishpond.jpg')
input_image = cv2.resize(input_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

#For version opencv < 3.0.0, use cv2.SURF()
# surf = cv2.SURF()

#This threshold controls the number of keypoints
surf.setHessianThreshold(15000)

keypoints, descriptors =  surf.detectAndCompute (gray_image, None)

cv2.drawKeypoints(input_image, keypoints, input_image, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow('SURF Features', input_image)
cv2.waitKey()