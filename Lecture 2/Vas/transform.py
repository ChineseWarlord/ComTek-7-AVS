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

# Calculate the affine transforms
M = cv.getAffineTransform(src=pts2,dst=pts1)
print(M)

# Apply to affine transform to img2 and save the results
cols,rows,_ = img2.shape
img2_t = cv.warpAffine(img2,M,(cols,rows))
cv.imwrite('rotzoom_transformed.png', img2_t)

#Specify the same 4 points for the projective transform
pts1 = np.float32([[2121,415], # upper left corner of the first black square
                   [1272,770], # the dot over the 'i' in 'Multiple'
                   [810,1948], # the dot over the 'i' in 'Richard'
                   [3144,2124]])# the bottom right corner of the last black square
pts2 = np.float32([[2469,2219], # upper left corner of the first black square
                   [2357,1336], # the dot over the 'i' in 'Multiple'
                   [1335,501], # the dot over the 'i' in 'Richard'
                   [875,3647]])# the bottom right corner of the last black square
#Calculate the projective transform
M_pro = cv.getPerspectiveTransform(src=pts2, dst=pts1)

# Apply the projective transform
cols,rows,_ = img3.shape
img3_t = cv.warpPerspective(img3,M_pro,(cols,rows))
cv.imwrite('persp1_transformed.png', img3_t)