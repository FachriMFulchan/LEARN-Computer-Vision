import cv2
import numpy as np

input_image = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bear.jpg')
# input_image = cv2.resize(input_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

#Initiate ORB Object
orb = cv2.ORB_create()

#Find the keypoints with ORB
keypoints = orb.detect(gray_image, None)

#compute the descriptions with ORB
keypoints, descriptors = orb.compute(gray_image, keypoints)

#draw only the location of the keypoints without size or orientation
cv2.drawKeypoints(input_image, keypoints, input_image, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('ORB keypoints', input_image)
cv2.waitKey()