import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #print(frame.shape)
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[0:frame.shape[0]//2, 0:frame.shape[1]//2] = smaller_frame
    image[0:frame.shape[0]//2, frame.shape[1]//2:frame.shape[1]] = smaller_frame
    image[frame.shape[0]//2:frame.shape[0], 0:frame.shape[1]//2] = smaller_frame
    image[frame.shape[0]//2:frame.shape[0], frame.shape[1]//2:frame.shape[1]] = smaller_frame
    cv2.imshow('image', image)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()