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
    template = cv.imread(img_template, cv.IMREAD_GRAYSCALE)
    
    # All the 6 methods for comparison in a list
    methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
    cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]
    
    # Choose a method
    method = methods[1]
    
    # Create a dictionary to map method integers to string representations
    method_names = {
        cv.TM_CCOEFF: 'TM_CCOEFF',
        cv.TM_CCOEFF_NORMED: 'TM_CCOEFF_NORMED',
        cv.TM_CCORR: 'TM_CCORR',
        cv.TM_CCORR_NORMED: 'TM_CCORR_NORMED',
        cv.TM_SQDIFF: 'TM_SQDIFF',
        cv.TM_SQDIFF_NORMED: 'TM_SQDIFF_NORMED'
    }
    
    # Use the dictionary to get the string representation of the method
    method_string = method_names.get(method, 'Unknown Method')
    
    # Apply template matching, normalization + threshholding
    threshold = 0.5
    norm_img = cv.normalize(img, None, 0, 1, cv.NORM_MINMAX)
    res = cv.matchTemplate(norm_img,template,method)
    ret, thresh = cv.threshold(res,threshold,255,cv.THRESH_BINARY)
    
    print(f"Matching Result: {res}")
    print(f"Matching + Thresholding Result: {thresh}")
    
    # Plot the result and original img
    plt.subplot(141),plt.imshow(img, cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(142),plt.imshow(norm_img, cmap = 'gray')
    plt.title('Normalized Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(143),plt.imshow(res, cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(144),plt.imshow(thresh, cmap = 'gray')
    plt.title('Matching Result + Threshold'), plt.xticks([]), plt.yticks([])
    plt.suptitle(method_string)
    plt.tight_layout()
    plt.show()