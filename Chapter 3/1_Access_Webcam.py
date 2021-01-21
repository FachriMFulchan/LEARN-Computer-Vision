import cv2 as cv

cap = cv.VideoCapture(0) 
#Webcam index 1 + reader implementatin Quicktime

#Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True :
    ret, frame = cap.read()
    frame = cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
    cv.imshow('Input', frame)

    c = cv.waitKey(1)
    if c == ord('q'):
        break

cap.release()
cv.destroyAllWindows()