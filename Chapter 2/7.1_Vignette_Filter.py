import cv2
import numpy as np

img = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/rose.jpeg', 1)
rows, cols = img.shape[:2]

#generating vignette mask using Gausssian kernels
kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)

kernel = kernel_y * kernel_x.T

print (kernel_x.shape)
print (kernel_y.shape)
print (kernel.shape)
print(img.shape)

mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)


#applying the mask to each channel in the input image
for i in range (3):
    output[:,:,i] = output[:,:,i] * mask



cv2.imshow('Original', img)
cv2.imshow('Vignette', output)
cv2.waitKey()