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
    # Initialize the threshold value and method index
    threshold = 0.5
    method_index = 1
    min_norm = 0
    max_norm = 1

    # Read the image and template
    img = cv.imread(img_dir, cv.IMREAD_GRAYSCALE)
    template = cv.imread(img_template, cv.IMREAD_GRAYSCALE)

    # All the 6 methods for comparison in a list
    methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

    # Create a dictionary to map method integers to string representations
    method_names = {
        cv.TM_CCOEFF: 'TM_CCOEFF',
        cv.TM_CCOEFF_NORMED: 'TM_CCOEFF_NORMED',
        cv.TM_CCORR: 'TM_CCORR',
        cv.TM_CCORR_NORMED: 'TM_CCORR_NORMED',
        cv.TM_SQDIFF: 'TM_SQDIFF',
        cv.TM_SQDIFF_NORMED: 'TM_SQDIFF_NORMED'
    }

    # Function to update the template matching method
def update_method(val):
    global method_index
    method_index = val

# Function to update the normalization range
def update_norm_range(val):
    global min_norm, max_norm
    min_norm = val / 100.0
    max_norm = (val + 100) / 100.0

# Create a window for the Threshold, Method, and Normalization selection
cv.namedWindow('Controls')
cv.createTrackbar('Threshold', 'Controls', int(threshold * 100), 100, lambda x: None)
cv.createTrackbar('Method', 'Controls', method_index, len(methods) - 1, update_method)
cv.createTrackbar('Normal', 'Controls', int(min_norm * 100), 100, update_norm_range)


# Threshold value 48, Method 1, Normalization 37
while True:
    # Get the current threshold value, method, and normalization range
    threshold = cv.getTrackbarPos('Threshold', 'Controls') / 100.0
    method = methods[method_index]
    method_string = method_names.get(method, 'Unknown Method')

    # Apply template matching with the updated threshold and method
    norm_img = cv.normalize(img, None, min_norm, max_norm, cv.NORM_MINMAX)
    res = cv.matchTemplate(norm_img, template, method)
    ret, thresh = cv.threshold(res, threshold, 255, cv.THRESH_BINARY)

    # Display the images and control window
    cv.imshow('Original Image', img)
    cv.imshow('Matching Result + Threshold', thresh)

    # Exit the loop when the user presses 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cv.destroyAllWindows()