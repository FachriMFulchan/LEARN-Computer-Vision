import cv2
import numpy as np

def update_pts(params, x, y):
    global x_init, y_init
    params["top_left_pt"] = (min(x_init, x), min(y_init,y))         #pilih yang paling kecil
    params["bottom_right_pt"] = (max(x_init, x), max(y_init, y))    #pilih yang paling besar
    img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]


    # print(params["top_left_pt"])
    # print(params["bottom_right_pt"])
    print((min(x_init, x), min(y_init,y)))
    


def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing

    #First click initialize the init rectangle point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y
    
    #Meanwhile mouse button is pressed, update diagonal rectangle point
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        update_pts(params, x, y)

    #Once mouse button is release
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        update_pts(params, x, y)


if __name__ == "__main__":
    drawing = False
    event_params = {"top_left_pt": (-1, -1), "bottom_right_pt": (-1, -1)}

    cap = cv2.VideoCapture(0)

    #Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    cv2.namedWindow('Webcam')

    #Bind draw_rectangle function to every mouse event
    cv2.setMouseCallback('Webcam', draw_rectangle, event_params)


    while True:
        ret, frame = cap.read()
        img = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        (x0, y0), (x1, y1) = event_params["top_left_pt"], event_params["bottom_right_pt"]
        img[y0:y1, x0:x1] = 255 - img[y0:y1, x0:x1]
        # print(event_params)
        cv2.imshow('Webcam', img)

        c = cv2.waitKey(1)
        if c ==  27:
            break
cap.release()
cv2.destroyAllWindows()