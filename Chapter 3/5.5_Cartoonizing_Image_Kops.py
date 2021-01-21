import numpy as np
import cv2 as cv

def print_howto():
    print("""
        1. Cartoonize without Color -- Press 's'
        2. Cartoonize with Color -- Press 'c'
        """)

def cartoonize_image(img, ksize=5, sketch_mode=False):
    num_repetitions, sigma_color, sigma_space, ds_factor = 10, 5, 7, 4

    #Convert to grayscale
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #Apply Median filter
    img_gray = cv.medianBlur(img_gray, 7)

    #Detect edges
    edges = cv.Laplacian(img_gray, cv.CV_8U, ksize=ksize)

    #Threshold
    ret, mask = cv.threshold(edges, 100, 255, cv.THRESH_BINARY_INV)

    #return yang gaada warnanya + nebelin
    if sketch_mode == True:
        kernel = np.ones((3,3), np.uint8)
        img_eroded = cv.erode(mask, kernel, iterations = 1)
        return cv.medianBlur(img_eroded, ksize=5)

    #dengan warna
    img_small = cv.resize(img, None, fx=1.0/ds_factor,fy=1.0/ds_factor, interpolation=cv.INTER_AREA)

    for i in range(num_repetitions):
        img_small = cv.bilateralFilter(img_small, ksize, sigma_color, sigma_space)
    
    img_output = cv.resize(img_small, None, fx= ds_factor, fy=ds_factor, interpolation=cv.INTER_LINEAR)

    dst = cv.bitwise_and(img_output, img_output, mask=mask)
    return dst

if __name__ == "__main__":
    
    cap = cv.VideoCapture(0)

    cur_mode = 0

    while True:
        ret, frame = cap.read()
        frame = cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

    
        k = cv.waitKey(1)
        if k == ord('q'):
            break

        if k != -1 and k != 255 and k != cur_mode:
            cur_mode = k

        if cur_mode == ord('s'):
            cv.imshow('Cartoonize',cartoonize_image(frame, ksize=5, sketch_mode=True))

        elif cur_mode == ord('c'):
            cv.imshow('Cartoonize',cartoonize_image(frame, ksize=5, sketch_mode=False))
        
        else:
            cv.imshow('Cartoonize', frame)

    cap.release()
    cv.destroyAllWindows()