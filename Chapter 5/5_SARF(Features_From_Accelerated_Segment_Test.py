import cv2
import numpy as np


input_image = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/arm.jpg')
input_image = cv2.resize(input_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

'''Non Supress'''
#Version under opencv 3.0.0 cv2.FastFeatureDetectot()
fast = cv2.FastFeatureDetector.create()

#Detect keypoints
keypoints = fast.detect(gray_image, None)
print("Number of keypoints with non max suppresion:", len(keypoints))

#Draw keypoints on top of the input image
img_keypoints_with_nonmax = input_image.copy()
cv2.drawKeypoints(input_image, keypoints, img_keypoints_with_nonmax, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Fast keypoints - with non max suppresion', img_keypoints_with_nonmax)




'''Supresss, nge reduce keypoints'''
#Disable nonmaxSuppress
fast.setNonmaxSuppression(False)

#DetectKeypoints again
keypoints = fast.detect(gray_image, None)
print('Total Keypoints without nonmaxSuppresion:', len(keypoints))

#Draw keypoints on top of the input image
img_keypoints_without_nonmax = input_image.copy()
cv2.drawKeypoints(input_image, keypoints, img_keypoints_without_nonmax, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('FAST keypoints - without non max suppresion', img_keypoints_without_nonmax)





cv2.imshow('input', input_image)
cv2.waitKey()