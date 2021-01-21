import numpy as np
import cv2


#Extract all the contours from the image
#buat semua shape
def get_all_contours(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, cv2.THRESH_BINARY)

    #Find all the contours in the thresholded image
    #The values for the second and third parameters are restricted
    #to a certain number of possible values
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

#Buat yang boomerang
#Jangan lupa di looping
def get_ref_contours(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, cv2.THRESH_BINARY_INV)

    #Inverting aja
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    #Kaya buka satu kurung sikunya ([])
    for contour in contours:
        return contour



if __name__ == "__main__":
    #Boomerang reference image
    img1 = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/boomerang.png')

    #Input image containing all the different shapes
    img2 = cv2.imread('D:/A LEARN/Image Processing/A Panduan Kang Gip/image/shape.png')

    #Extract reference contours
    ref_contour = get_ref_contours(img1)
    
    #Extract all contours
    input_contours = get_all_contours(img2)


    contoursref = img1.copy()
    contoursall = img2.copy()

    cv2.drawContours(contoursref, ref_contour, -1, (0,255,0), 3)
    cv2.drawContours(contoursall, input_contours, -1, (0,255,0), 3)


    cv2.imshow('Contours Ref', contoursref)
    cv2.imshow('Contour All', contoursall)

    closest_contour = None
    min_dist = None

    for contours in input_contours:
        #fungsi
        ret = cv2.matchShapes(ref_contour, contours, 3, 0.0)

        #Matching the shapes and taking the closest one using
        #Comparison method CV_CONTOURS_MATCH_I3 (second argument)

        #algoritma
        if min_dist is None or ret < min_dist:
            min_dist = ret
            closest_contour = contours
    

    #Tadi kan dibuka kurung sikunya, sekarang ditutup lagi biar bisa di draw
    cv2.drawContours(img2, [closest_contour], 0, (0,0,0), 3)   #Kenapa harus pake [], biar dianggap array, bukan list aja
    cv2.imshow('Best Matching', img2)
    cv2.waitKey()

