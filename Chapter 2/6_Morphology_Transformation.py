'''Erotion and DIlation merupakan bagian dari
morphological transformation dalam image proscessing'''
import cv2
import numpy as np


img = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/word.jpeg', 0)

kernel = np.ones((5,5), np.uint8)

# img_erosion = cv2.erode(img, None, iterations=1)
# img_dilation = cv2.dilate(img, None, iterations=1)
'''None juga bisa, soalnya ada kernel bawaan'''

coba1 = cv2.erode(img, kernel, iterations=1)
coba2 = cv2.dilate(coba1, kernel, iterations=1)
cv2.imshow('coba1', coba1)
cv2.imshow('coba2', coba2)
'''Kalo di erode terus di dilate dengan iterasi yang sama ya sama aja'''
'''Cuma lebih stabil aja jadinya'''


img_erosion = cv2.erode(img, kernel, iterations=1)  
img_dilation = cv2.dilate(img, kernel, iterations=1)
img_morphex = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.imshow('Morphology Ex', img_morphex) #Kaya Dilate cuma lebih soft
cv2.waitKey(0)


#Erotion tuh ngikis putih, nebelin item
#Dilation ngikis item, nebelin putih
#Harus pake threshold biar invert atau engganya