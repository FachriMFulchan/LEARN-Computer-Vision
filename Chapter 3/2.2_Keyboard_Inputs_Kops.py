import cv2

def statement():
    print ('''Choose what format do yo like :
                1. Grayscale -- Press 'g'
                2. YUV -- Press 'Y'
                3. HSV -- Press 'H'
                ''')

if __name__ == "__main__":
    statement()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError('Webcam is Error')
    
    cur_mode = None

    while True:
    
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break

        if k != -1 :
            cur_mode = k
        
        if cur_mode == ord('g'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif cur_mode == ord('y'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        elif cur_mode == ord('h'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        else:
            output = frame

        cv2.imshow('Output', output)
    
    cap.release()
    cv2.destroyAllWindows()
