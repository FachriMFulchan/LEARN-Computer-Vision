import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True :
    ret, frame = cap.read()

    rows, cols = frame.shape[:2]

    src_points = np.float32([ [0,0], [cols, 0], [0, rows] ])
    dst_points = np.float32([ [cols, 0], [0,0], [cols, rows]])

    affine_matrix = cv.getAffineTransform(src_points, dst_points)
    img_affine = cv.warpAffine(frame, affine_matrix, (cols, rows))




    cv.imshow('Frame', frame)
    cv.imshow('Mirror', img_affine)
    
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()