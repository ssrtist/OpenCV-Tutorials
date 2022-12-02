import cv2

img = cv2.imread('assets/2hands.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, [0,0], fx=.5, fy=.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('assets/new_img.jpg', img)

cv2.imshow('2hands', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(img))
print(img)