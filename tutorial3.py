import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(frame.shape[1])
    height = int(frame.shape[0])
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image = np.zeros(frame.shape, np.uint8)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame
    cv2.imshow('image', image)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()