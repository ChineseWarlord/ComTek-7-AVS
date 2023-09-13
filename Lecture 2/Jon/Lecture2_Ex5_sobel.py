import cv2 as cv
import numpy as np

# for grayscale read "cv.IMREAD_GRAYSCALE"
img = cv.imread('ironmanhelmet.jpg')

scale_percent = 40 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

sobelx = cv.Sobel(resized,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(resized,cv.CV_64F,0,1,ksize=5)

cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)


cv.waitKey(0)
cv.destroyAllWindows()
