import cv2 as cv
import numpy as np

# Read images
img1 = cv.imread('../Images/exe_a/ref.jpeg')

img2 = cv.imread('../Images/exe_a/rotzoom.jpeg')
img3 = cv.imread('../Images/exe_a/persp1.jpeg')

# Specify the same 3 points in both images
# use MS paint, GIMP or another program to manually get the pixel positions
# this part is typically automated using image processing
pts1 = np.float32([[2121,415], # upper left corner of the first black square
                   [1272,770], # the dot over the 'i' in 'Multiple'
                   [810,1948]]) # the dot over the 'i' in 'Richard'
pts2 = np.float32([[894,1003], # upper left corner of the first black square
                   [594,2063], # the dot over the 'i' in 'Multiple'
                   [1318,3349]]) # the dot over the 'i' in 'Richard'
pts3 = np.float32([[2469,2219], # upper left corner of the first black square
                   [2357,1336], # the dot over the 'i' in 'Multiple'
                   [1335,501]]) # the dot over the 'i' in 'Richard'

# Calculate the affine transforms
M = cv.getAffineTransform(src=pts2,dst=pts1)
M2 = cv.getAffineTransform(src=pts3, dst=pts1)
print(M)
print(M2)

# Apply to affine transform to img2 and save the results
cols,rows,_ = img2.shape
cols2,rows2,_ = img3.shape
img2_t = cv.warpAffine(img2,M,(cols,rows))
img3_t = cv.warpAffine(img3,M2,(cols2,rows2))
cv.imwrite('rotzoom_transformed.png', img2_t)
cv.imwrite('persp1_transformed.png', img3_t)

#Calculate the projective transform
