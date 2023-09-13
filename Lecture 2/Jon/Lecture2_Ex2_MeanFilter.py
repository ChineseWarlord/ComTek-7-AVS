import cv2 as cv
import numpy as np

img = cv.imread('lion.jpg')

#Create a x by x kernel for averaging
#np.ones to create a kernel of 1's
#divide by number of entries in kernel
x = 5
y = 5
kernelSize = [x,y]
KernelTotalEntries = x * y
kernelAveraging = np.ones((kernelSize[0], kernelSize[1]), np.float32)/KernelTotalEntries 

#Create a x by x kernel for gaussian blur
kernelGaussian = cv.getGaussianKernel(5,5)

#Apply the 2d filter with chosen kernel
img = cv.filter2D(src=img, ddepth=-1, kernel=kernelGaussian)


cv.imshow("Lion", img)
#cv.imshow("Blurred Lion", blur)

cv.waitKey(0)
cv.destroyAllWindows()
