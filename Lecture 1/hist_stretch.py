'''
Write a function that increases the contrast of the image 'Einstein'.

Vasiliki
'''

import numpy as np
import cv2 as cv

#ONLY FOR GRAYSCALE
def stretch(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    min = np.min(img)
    max = np.max(img)

    for counteri, i in enumerate(img):
        for counterj, _ in enumerate(i):
            img[counteri, counterj] = (img[counteri, counterj] - min) * 255 / (max - min)
    
    return img