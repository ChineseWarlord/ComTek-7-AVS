import cv2 as cv
import numpy as np
import glob

bg =cv.imread('../Data/Test016/001.tif')
bg = cv.cvtColor(bg, cv.COLOR_BGR2GRAY).astype(np.float32)
for images in glob.iglob('../Data/Test016/*.tif'):
    img = cv.imread(images)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY).astype(np.float32)
    diff = np.abs(gray - bg)
    img[diff > 2] = [0, 0, 255]
    print(img)
    cv.imshow('2', img)
    cv.waitKey(0)

# diff = np.abs(bg - img)

# cv.imshow('1', bg)
# cv.waitKey(0)