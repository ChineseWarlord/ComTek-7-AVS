import cv2 as cv
import numpy as np

# How can Morphology be used to find the outline (edge) of an object in a binary image? ​
# Answer: Use the difference between dilation and erosion
# gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

img = cv.imread('dots.jpg', cv.IMREAD_GRAYSCALE)

kernel = np.ones((3,3),np.uint8)
closed = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
opening = cv.morphologyEx(closed, cv.MORPH_OPEN, kernel)


cv.imshow("OG img", img)
cv.imshow("Morphology closing operation", opening)

cv.waitKey(0)
cv.destroyAllWindows()
