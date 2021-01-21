import cv2
import numpy as np

img = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\kardus.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#To detect ony sharp corners
dst = cv2.cornerHarris(gray, blockSize=4, ksize=5, k=0.04)   #bedanya disini

#Result is dilated for markind the corners
dst = cv2.dilate(dst, None)

#Threshold for an optimal value, it may vary depending on the image
img[dst > 0.01*dst.max()]  = [0,0,0]
cv2.imshow('Harris Corners (only sharp)', img)




#To detect soft corners
dst = cv2.cornerHarris(gray, blockSize=14, ksize=5, k=0.04)
dst = cv2.dilate(dst, None)

img[dst > 0.01*dst.max()] = [0,0,0]
cv2.imshow('Harris Corners (also soft)', img)

cv2.waitKey()
cv2.destroyAllWindows()