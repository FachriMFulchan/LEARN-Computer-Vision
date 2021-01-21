import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #Ngeresize
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    #Ngeconvert jadi gray
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Ngilangin noise
    output = cv2.medianBlur(output, 7)

    #Detect Edges
    output = cv2.Laplacian(output, cv2.CV_8U, ksize=5)

    #Memperjelas si hitam dengan si putih
    ret, output = cv2.threshold(output, 100, 255, cv2.THRESH_BINARY_INV)

    output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

    cv2.imshow('Frame', frame)
    cv2.imshow('Output', output)


    k = cv2.waitKey(1)
    
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()