import numpy as np
import cv2

img = cv2.imread('assets/2hands.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img2, 100, 0.3, 100)
corners = np.int0(corners)

for corner in corners:
    print(corner)
    x, y = corner[0].ravel()
    print(x, y)
    cv2.circle(img, (x, y), 10, (0, 128, 255), 1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = corners[i]
        x1, y1 = corners[i].ravel() # same as using [0]
        corner2 = corners[j]
        x2, y2 = corners[j][0] # same as using ravel()
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        # color = (np.int(np.random.randint(0, 255)), np.int(np.random.randint(0, 255)), np.int(np.random.randint(0, 255)))
        #cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 2, 1)
        cv2.line(img, (x1, y1), (x2, y2), color, 2, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
