'''
Exercise 4
Write your own thresholding algorithm that takes a grayscale images as input. Show input and the binary output image
Load and threshold the two images 'thermal1' and 'thermal2' (from moodle). Then, combine the two binary images using the logic operations AND and OR (one at a time).

Vasiliki
'''

import cv2 as cv
import numpy as np
import threshold_vas as thr

if __name__=='__main__':
    thermal1 = cv.imread('images/thermal1.png')
    thermal1 = thr.man_threshold(thermal1, 120)
    thermal2 = cv.imread('images/thermal2.png')
    thermal2 = thr.man_threshold(thermal2, 120)

    cv.imshow('thermal1', thermal1)
    cv.waitKey(0)

    cv.imshow('thermal2', thermal2)
    cv.waitKey(0)

    if np.shape(thermal1) == np.shape(thermal2):
        img_and = thermal1.copy()
        img_or  = thermal1.copy()

        for counteri, i in enumerate(thermal1):
            for counterj, _ in enumerate(i):
                img_and[counteri, counterj] = thermal1[counteri, counterj] & thermal2[counteri, counterj]
                img_or[counteri, counterj] = thermal1[counteri, counterj] | thermal2[counteri, counterj]

        cv.imshow('img_and', img_and)
        cv.waitKey(0)

        cv.imshow('img_or', img_or)
        cv.waitKey(0)
    else:
        print('ERROR: Image dimensions need to be common')


