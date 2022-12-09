import numpy as np
import cv2

img = cv2.imread('assets/girl2.png', 0)
tempball = cv2.imread('assets/ball2.png', 0)

h, w = tempball.shape
print(img)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, tempball, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, (200,0,0))
    cv2.imshow('Detected with: ' + str(method), img2)
    cv2.waitKey(0)

cv2.destroyAllWindows()