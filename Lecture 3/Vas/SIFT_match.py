'''Change your solution from last exercise to extract SIFT keypoints and descriptors instead of Harris Corners and your own descriptors
Match feature descriptors using the DescriptorMatcher class
Visualize the matches using the drawMatches function'''

import cv2 as cv
import numpy as np

#Reading the partly overlapping images
img1 = cv.imread('../Data/aau-city-1.jpg') 
img2 = cv.imread('../Data/aau-city-2.jpg')

gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

#Using SIFT to locate corners and descriptors (needs tuning)
sift = cv.SIFT_create()
kps1, des1 = sift.detectAndCompute(gray1, None)
kps2, des2 = sift.detectAndCompute(gray2, None)

img1 =cv.drawKeypoints(gray1 ,kps1, img1)
img2 =cv.drawKeypoints(gray2 ,kps2, img2)

#Using a matcher to match descriptors from img1 to img2 (needs thresholding)
bf = cv.BFMatcher()
matches = bf.match(des1, des2)


#Using drawMatches function to link the good matches
test1 = cv.drawMatches(img1, kps1, img2, kps2, matches, 0)
cv.imshow('sift_keypoints1.jpg', test1)

cv.waitKey(0)
