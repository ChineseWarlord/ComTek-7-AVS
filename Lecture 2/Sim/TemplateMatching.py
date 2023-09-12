"""
Exercise 2
1. Use OpenCV to load and display neon-text.png​. Use template matching to make an image which shows the positions of the three hearts, similar to the one below (the white dots showing the positions are very small, but there are three of them). Show the correlation image as an intermediate step.
 
Hint: Use a combination of the functions matchTemplate, normalize, and threshold

- Simon
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import time

img_dir = "../images/neon-text.png"
img_template = "../images/template_color.png"

if __name__ == "__main__":
    # Read the img
    img = cv.imread(img_dir, cv.IMREAD_GRAYSCALE)
    img2 = img.copy()
    
    template = cv.imread(img_template, cv.IMREAD_GRAYSCALE)
    w, h = template.shape
    
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
    'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        
    
    # Apply template Matching
    res = cv.matchTemplate(img,template,cv.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img,top_left, bottom_right, 255, 2)
    
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()