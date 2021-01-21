import numpy as np
import cv2

def remove_alpha_channel(source, background_color):
    source_img = source
    source_mask = source * (1 / 255.0)
    bg_part = (255 * (1 / 255.0)) * (1.0 - source_mask)
    weight = (source_img * (1 / 255.0)) * (source_mask)
    dest = np.uint8(cv2.addWeighted(bg_part, 255.0, weight, 255.0, 0.0))
    return dest

orig_img = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\corona.jpg', 1)
dest_img = remove_alpha_channel(orig_img, 1)

cv2.imshow('original', orig_img)
cv2.imshow('Dest', dest_img)
cv2.waitKey()