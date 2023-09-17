import cv2 as cv
import numpy as np

#Reading the partly overlapping images
img1 = cv.imread('../Data/aau-city-1.jpg') 
img2 = cv.imread('../Data/aau-city-2.jpg')

gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY).astype(np.float32)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY).astype(np.float32)

# Detect corners
dst1 = cv.cornerHarris(gray1, 2, 3, 0.04)
dst1 = cv.dilate(dst1,None)

dst2 = cv.cornerHarris(gray2, 2, 3, 0.04)
dst2 = cv.dilate(dst2,None)

#Find the same corners in both images

for counteri, i in enumerate(dst1>0.2*dst1.max()):
    for counterj, j in enumerate(i):
        if(j):
            for counterk, k in enumerate(dst2>0.2*dst2.max()):
                for counterl, l in enumerate(k):
                    if (l):
                        diff = abs(dst1[counteri, counterj] - dst2 [counterk, counterl])
                        check = diff < 0.01 * dst1[counteri, counterj]
                        if check:
                            img1[counteri, counterj] = [0, 0, 255]
                            img2[counterk, counterl] = [0, 0, 255]

cv.imshow('1', img1)
cv.imshow('2', img2)

cv.waitKey()
