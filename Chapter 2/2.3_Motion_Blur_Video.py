import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

size = 100
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur/size

while True :
    _, frame = cap.read()
    motion_blur = cv.filter2D(frame, -1, kernel_motion_blur)
    cv.imshow('video frame', motion_blur)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()