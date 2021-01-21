import cv2
import numpy as np

input_image = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bear.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# For version opencv < 3.0.0, use cv2.SIFT()
sift = cv2.SIFT.create()
keypoints = sift.detect(gray_image, None)

cv2.drawKeypoints(input_image, keypoints, input_image, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT features', input_image)
cv2.waitKey()