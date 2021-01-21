'''Gabisa ah gaada methodnya'''


import cv2
import numpy as np

input_image = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/fronthouse.jpg')
input_image = cv2.resize(input_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

#Initiate fast Detector
fast = cv2.FastFeatureDetector_create()

## Initiate BRIEF extractor, before opencv 3.0.0 use cv2.DescriptorExtractor_create("BRIEF")
brief = cv2.DescriptorMatcher.create('FlannBased') #Parameternya gatau apa ini bebas

#find the keypoints with STAR
keypoints = fast.detect(gray_image, None)


#compute the decriptions with BRIEF
# keypoints, descriptors = brief.compute(gray_image, keypoints)
cv2.drawKeypoints(input_image, keypoints, input_image, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('BRIEF keypoints', input_image)
cv2.waitKey()