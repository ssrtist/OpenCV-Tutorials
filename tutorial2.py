import cv2
import random as rd

img = cv2.imread('assets/2hands.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, [0,0], fx=.5, fy=.5)
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [rd.randrange(255),rd.randrange(255),rd.randrange(255)]

copy = img[50:150, 300:400]
img[200:300, 200:300] = copy

cv2.imshow('2hands', img)
cv2.waitKey(0)
cv2.destroyAllWindows()