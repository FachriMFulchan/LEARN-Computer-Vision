import cv2 as cv


img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')
cv.imshow('image', img)

yuv_img = cv.cvtColor(img, cv.COLOR_BGR2YUV)
cv.imshow('YUV image', yuv_img)

#Alternative1
# y,u,v = cv.split(yuv_img)
# cv.imshow('Y Channel', y)
# cv.imshow('U Channel', u)
# cv.imshow('V Channel', v)


# Alternative 2 (Faster)
cv.imshow('Y channel', yuv_img[:, :, 0])  #Channel 1 is Y
cv.imshow('U channel', yuv_img[:, :, 1])  #Channel 2 is U
cv.imshow('V channel', yuv_img[:, :, 2])  #Channel 3 is V


cv.waitKey(0)