'''
Exercise 3
-Use OpenCV to load and display a color image
-Convert it to grayscale
    Using nested loops
    Using matrix multiplication
    Using the built-in OpenCV function

Vasiliki
'''
import cv2 as cv
import sys
import numpy as np

if __name__=='__main__':
    img = cv.imread("../images/bente.png")

    cv.imshow('Test', img)
    cv.waitKey(0)
    
# Using nested loops
# Same code we wrote in the group room but used enumerate to avoid the manual counter mistakes
    grayscale = img.copy()
    for counteri, i in enumerate(img):
        for counterj, j in enumerate(i):
            pixel = img[counteri, counterj]
            x = (1/3) * pixel[0] + (1/3) * pixel[1] + (1/3) * pixel[2]
            grayscale[counteri, counterj] = x
    cv.imshow('Grayscale', grayscale)
    cv.waitKey(0)

# Using matrix multiplication
    grayscale = img.copy()
    weights = [0.299, 0.587, 0.114]
    mulmatrix =np.transpose(np.full((3,3), weights))
    for counteri, i in enumerate(img):
        grayscale[counteri] = np.matmul(img[counteri], mulmatrix)

    cv.imshow('Grayscale', grayscale)
    cv.waitKey(0)

# Using the built-in OpenCV function
    grayscale = img.copy()
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('Grayscale', grayscale)
    cv.waitKey(0)









