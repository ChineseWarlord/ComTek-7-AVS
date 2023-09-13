import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../images/neon-text.png', cv.IMREAD_GRAYSCALE)
template = cv.imread('../images/template.png', cv.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

img = cv.normalize(img, None, 0, 255, norm_type=cv.NORM_MINMAX)




ret, img = cv.threshold(img, 80, 255, cv.THRESH_BINARY)
# ret, template = cv.threshold(template, 80, 255, cv.THRESH_BINARY)
res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
ret, res = cv.threshold(res, 0.38, 1, cv.THRESH_BINARY)


cv.imshow('img2', img)
cv.imshow('img3', res)
cv.waitKey(0)






