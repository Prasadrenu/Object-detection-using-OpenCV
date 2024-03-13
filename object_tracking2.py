import cv2
import numpy as np
cap = cv2.VideoCapture("los_angeles.mp4")
if 0:
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print( length )
    fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV v2.x used "CV_CAP_PROP_FPS"
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps

    print('fps = ' + str(fps))
    print('number of frames = ' + str(frame_count))
    print('duration (S) = ' + str(duration))
    minutes = int(duration/60)
    seconds = duration%60
    print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
while 1:
    _, frame = cap.read()
    if _ is False:
        break
    cv2.imshow("FRAME", frame)
    key = cv2.waitKey(42)
