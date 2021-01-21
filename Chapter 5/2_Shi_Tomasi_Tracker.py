import cv2
import numpy as np


img = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\kardus.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=20, qualityLevel=0.05, minDistance=25)
corners = np.float32(corners)

for item in corners:
    x, y =(item[0][0], item[0][1])
    print(item[0], item)
    cv2.circle(img, (x,y), 5, 255, -1)

cv2.imshow("Top 'k' Features", img)
cv2.waitKey()