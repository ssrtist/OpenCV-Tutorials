import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))

font = cv2.FONT_HERSHEY_COMPLEX
framecount = 0
while True:
    framecount+=1
    ret, frame = cap.read()
    # width2 = int(frame.shape[1])
    # height2 = int(frame.shape[0])
    # print ('width: ' + str(width) + ' and height: ' + str(height))

    img = cv2.line(frame, (0, 0), (width, height), (0,255,0), 10)
    img = cv2.line(img, (0, height), (width, 0), (255,255,0), 10)
    img = cv2.rectangle(img, (100,100),(200,200), (128,255,255))
    img = cv2.circle(img, (200,200), 50, (128,128,128))
    img = cv2.putText(img, 'FPS: ' + str(framecount), (50,100), cv2.FONT_HERSHEY_COMPLEX, 1, 5, 5, cv2.LINE_AA)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'): break

#print ('width2: ' + str(width2) + ' and height2: ' + str(height2))

cap.release()
cv2.destroyAllWindows()