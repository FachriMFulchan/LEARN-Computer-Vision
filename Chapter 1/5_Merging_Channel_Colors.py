import cv2 as cv

img = cv.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/bali.jpg')

b,g,r = cv.split(img)
rgb_img = cv.merge((r,g,b))
gbr_img = cv.merge((g,b,r))
rbr_img = cv.merge((r,b,r))

cv.imshow('Original', img)
cv.imshow('rgb Image', rgb_img)
cv.imshow('gbr Image', gbr_img)
cv.imshow('rbr Image', rbr_img)

#Intinya channel tuh bisa di merge untuk menghasilkan mood yang beda
# kalo presize nya mah gua juga gatau gimana biar bagus tuh wkwk
#soalnya kan itu masuk masukin doang wkw

cv.waitKey(0)
