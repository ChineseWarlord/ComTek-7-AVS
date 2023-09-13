import cv2 as cv
import numpy as np

# for grayscale read "cv.IMREAD_GRAYSCALE"
img = cv.imread('ironmanhelmet.jpg')

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

edges50 = cv.Canny(resized,50,100)
edges200 = cv.Canny(resized,200,400)

cv.imshow("edges50", edges50)
cv.imshow("edges200", edges200)



cv.waitKey(0)
cv.destroyAllWindows()