"""
Exercise 2
1. Use OpenCV to load and display lion.jpg​
    Implement a mean filter with configurable kernel size​
    Extra: Implement a Gaussian blur filter with configurable kernel size​
2. Use OpenCV to load and display neon-text.png​. Use template matching to make an image which shows the positions of the three hearts, similar to the one below (the white dots showing the positions are very small, but there are three of them). Show the correlation image as an intermediate step.

- Simon
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import time

img_dir = "../images/lion.jpg"

def mean_filter(img, radius):
    # Copy original img to output img
    img_copy = np.copy(img)
    h, w = img.shape
    #print(f"Original: Width {w}, Height {h}")
    
    # Iterate through each pixel, add neighbors, calculate mean, copy onto output img
    for y in range(radius, h - radius):
        for x in range(radius, w - radius):
            neighbors = img[y - radius:y + radius + 1, x - radius:x + radius + 1]
            mean = np.mean(neighbors)
            img_copy[y,x] = mean
             
    return img_copy

def median_filter(img, radius):
    # Copy original img to output img
    img_copy = np.copy(img)
    h, w = img.shape
    #print(f"Original: Width {w}, Height {h}")
    
    # Iterate through each pixel, add neighbors, calculate median, copy onto output img
    for y in range(radius, h - radius):
        for x in range(radius, w - radius):
            neighbors = img[y - radius:y + radius + 1, x - radius:x + radius + 1]
            median = np.median(neighbors)
            img_copy[y,x] = median
            
    return img_copy


    
if __name__ == "__main__":
    #test = np.array([[1, 2, 3],
    #                 [4, 5, 6],
    #                 [7, 8, 9]])
    #y,x = 2,2
    #print(test[y-1:y+1+1])
    #print(test[x-1:x+1+1])
    #print(test[y-1:y+1+1,x-1:x+1+1])
    #exit()
    
    # Read the img
    img = cv.imread(img_dir, cv.IMREAD_GRAYSCALE)
    
    # Apply mean filter
    filtered_img1 = mean_filter(img, 1)
    filtered_img2 = mean_filter(img, 2)
    filtered_img3 = mean_filter(img, 3)
    
    # Apply opencv function
    opencv_blur1 = cv.blur(img, (3,3))
    opencv_blur2 = cv.blur(img, (5,5))
    opencv_blur3 = cv.blur(img, (7,7))
    
    # Apply median filter
    filtered_img4 = median_filter(img, 1)
    filtered_img5 = median_filter(img, 2)
    filtered_img6 = median_filter(img, 3)
    
    # Add up all images in each row
    row1 = np.concatenate((filtered_img1,filtered_img2,filtered_img3), axis=1)
    row2 = np.concatenate((opencv_blur1,opencv_blur2,opencv_blur3), axis=1)
    row3 = np.concatenate((filtered_img4,filtered_img5,filtered_img6), axis=1)
    disp_img = np.concatenate((row1,row2,row3), axis=0)
    
    # Display filtered images
    cv.imshow("Window", disp_img)
    
    k = cv.waitKey(0)
    if k == ord("q"):
        cv.destroyAllWindows()
        exit()

    