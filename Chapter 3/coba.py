import cv2
import numpy as np

def update_pts(params, x, y):
    global x_init, y_init
    params["top_left_pt"] = (min(x_init, x), min(y_init, y))
    params["bottom_right_pt"] = (max(x_init, x), max(y_init, y))
    img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]

def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        update_pts(params, x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        update_pts(params, x, y)

    



if __name__ == "__main__":
    drawing = False
    event_params = {"top_left_pt":(-1, -1), "bottom_right_pt": (-1, -1)}

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError('Cannot Open Webcam')

    cv2.namedWindow('Webcam')

    while True:
        ret, frame = cap.read()
        img = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        cv2.setMouseCallback('Webcam', draw_rectangle, event_params)

        (x0, y0), (x1, y1) = event_params["top_left_pt"], event_params['bottom_right_pt']
        img[y0:y1, x0:x1] = 255 - img[y0:y1, x0:x1]
        
        print(event_params["top_left_pt"])
        print(event_params["bottom_right_pt"])


        cv2.imshow('Webcam', img)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()