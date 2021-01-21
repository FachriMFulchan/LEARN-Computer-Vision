import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\A LEARN\Image Processing\A Panduan Kang Gip\Latihan_Koplo\Chapter 4\haarcascade_eye.xml')


if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')
if eye_cascade.empty():
    raise IOError('Unable to load the eye cascade classifier xml file')

cap = cv2.VideoCapture(0)
sunglasses_img = cv2.imread('D:\A LEARN\Image Processing\A Panduan Kang Gip\image\kacamata.jpg')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)

    centers = []

    for (x,y,w,h) in faces:
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_color)
        
        for(x_eyes, y_eyes, w_eyes, h_eyes) in eyes:
            centers.append ((x + int(x_eyes + 0.5 * w_eyes), y + int(y_eyes + 0.5*h_eyes)))

    #if detect both eyes
    if len(centers) > 1: 
        h, w = sunglasses_img.shape[:2]

        #Extract region of interest from the image
        eye_distance = abs(centers[1][0]- centers[0][0])

        #Overlay sunglasses
        #the factor 2.12 is customizable depending on the size of the image
        sunglasses_width = 2.12 * eye_distance
        scalling_factor = sunglasses_width / w
        print (scalling_factor, eye_distance)
        overlay_sunglasses = cv2.resize(sunglasses_img, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_AREA)

        x = centers[0][0] if centers[0][0] < centers[1][0] else centers[1][0]

        #customizable x and y locations; depends in the size of the face
        x -= int(0.26 * overlay_sunglasses.shape[1])
        y += int(0.26*overlay_sunglasses.shape[0])
        h, w = overlay_sunglasses.shape[:2]
        h, w = int(h), int(w)
        frame_roi = frame[y:y+h, x:x+w]

        #Convert color image to grayscale and threshold it
        gray_overlay_sunglassess = cv2.cvtColor(overlay_sunglasses, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_overlay_sunglassess, 180, 255, cv2.THRESH_BINARY_INV)

        #create an inverse mask
        mask_inv = cv2.bitwise_not(mask)

        try:
            #Use the mask to extract the face mask region of interest
            masked_face = cv2.bitwise_and(overlay_sunglasses, overlay_sunglasses, mask=mask)

            #Use the inverse mask to get remaining part of the image
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)

            frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)
            
        except cv2.error as e :
            print('Ignoring arithmetic exceptions' + str(e))
            #raise e
    else:
        print('Eyes not detected')
        

    cv2.imshow('Eye detector', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
