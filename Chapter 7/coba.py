import numpy as np
import cv2

#Extract all the contours from the image
def get_all_contours(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, cv2.THRESH_BINARY)

    #Find all the contours in the thresholded image
    #The values for the second and third parameters are restricted
    #to a certain number of possible values
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours


if __name__ == "__main__":

    white = 255 - np.ones((334,475), np.uint8)
    img1 = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/shape.png')
    
    input_contours = get_all_contours(img1)

    contour_img = img1.copy()
    smoothen_contours = []
    factor = 0.05


    #Finding the closest contour
    for contour in input_contours:
        epsilon = factor * cv2.arcLength(contour, True)
        smoothen_contours.append(cv2.approxPolyDP(contour, epsilon, True))
        print(len(cv2.approxPolyDP(contour, epsilon, True)))
    
    cv2.drawContours(contour_img, smoothen_contours, -1, (0,255,0), 3)
    cv2.drawContours(white, smoothen_contours, -1, (0,0,0), 3)
    
    
    cv2.imshow('Contours', contour_img)
    cv2.imshow('White', white)
    cv2.waitKey()
    