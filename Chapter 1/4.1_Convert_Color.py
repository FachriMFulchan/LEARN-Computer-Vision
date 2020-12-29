import cv2 as cv

# Color Convert apa aja yang tersedia di OpenCV (ada 190)
# for i in dir(cv):
#     if 'COLOR_' in i:
#         print (i)


#Ngeconvert ke Grayscale
img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')
cv.imshow('image', img)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image', gray_img)

print (img.shape)
cv.waitKey(0)