'''
Exercise 4
Write your own thresholding algorithm that takes a grayscale images as input. Show input and the binary output image
Load and threshold the two images 'thermal1' and 'thermal2' (from moodle). Then, combine the two binary images using the logic operations AND and OR (one at a time).

Vasiliki
'''

import cv2 as cv
import numpy as np
import sys


def man_threshold(img, th):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    for counteri, i in enumerate(img):
        for counterj, _ in enumerate(i):
            if img[counteri, counterj] < th:
                img[counteri, counterj] = 0
            else:
                img[counteri, counterj] = 255

    return img


    
    

