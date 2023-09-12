import cv2 as cv

img = cv.imread('../images/neon-text.png', cv.IMREAD_GRAYSCALE)
cv.imshow('img', img)
cv.waitKey()