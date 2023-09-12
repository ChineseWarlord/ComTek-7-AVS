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
    # Get the shape (dimensions) of the original img
    # Create a new empty array with same shape
    h, w = img.shape
    img_copy = np.zeros((h, w), dtype="uint8")
    # print(f"Original: Width {w}, Height {h}")

    # Iterate through each pixel, add neighbors, calculate mean, copy onto output img
    for y in range(radius, h - radius):
        for x in range(radius, w - radius):
            neighbors = img[y - radius : y + radius + 1, x - radius : x + radius + 1]
            mean = np.mean(neighbors)
            img_copy[y, x] = mean

    return img_copy


def median_filter(img, radius):
    # Get the shape (dimensions) of the original img
    # Create a new empty array with same shape
    h, w = img.shape
    img_copy = np.zeros((h, w), dtype="uint8")
    # print(f"Original: Width {w}, Height {h}")

    # Iterate through each pixel, add neighbors, calculate median, copy onto output img
    for y in range(radius, h - radius):
        for x in range(radius, w - radius):
            neighbors = img[y - radius : y + radius + 1, x - radius : x + radius + 1]
            median = np.median(neighbors)
            img_copy[y, x] = median

    return img_copy


if __name__ == "__main__":
    # test = np.array([[1, 2, 3],
    #                 [4, 5, 6],
    #                 [7, 8, 9]])
    # y,x = 2,2
    # print(test[y-1:y+1+1])
    # print(test[x-1:x+1+1])
    # print(test[y-1:y+1+1,x-1:x+1+1])
    # exit()

    # Read the img
    img = cv.imread(img_dir, cv.IMREAD_GRAYSCALE)

    # Apply mean filter
    filtered_img1 = mean_filter(img, 1)
    filtered_img2 = mean_filter(img, 2)
    filtered_img3 = mean_filter(img, 3)

    # Apply mean opencv function
    opencv_blur1 = cv.blur(img, (3, 3))
    opencv_blur2 = cv.blur(img, (5, 5))
    opencv_blur3 = cv.blur(img, (7, 7))

    # Apply median filter
    filtered_img4 = median_filter(img, 1)
    filtered_img5 = median_filter(img, 2)
    filtered_img6 = median_filter(img, 3)
    
    # Apply median opencv function
    opencv_blur4 = cv.medianBlur(img, 3)
    opencv_blur5 = cv.medianBlur(img, 5)
    opencv_blur6 = cv.medianBlur(img, 7)

    # Apply gaussian opencv function
    opencv_blur7 = cv.GaussianBlur(img, (3, 3), 0)
    opencv_blur8 = cv.GaussianBlur(img, (5, 5), 0)
    opencv_blur9 = cv.GaussianBlur(img, (7, 7), 0)

    # Add up all images in each row
    row1 = np.concatenate((filtered_img1, filtered_img2, filtered_img3), axis=1)
    row2 = np.concatenate((opencv_blur1, opencv_blur2, opencv_blur3), axis=1)
    row3 = np.concatenate((filtered_img4, filtered_img5, filtered_img6), axis=1)
    row4 = np.concatenate((opencv_blur4, opencv_blur5, opencv_blur6), axis=1)
    row5 = np.concatenate((opencv_blur7, opencv_blur8, opencv_blur9), axis=1)
    disp_img1 = np.concatenate((row1, row2), axis=0)
    disp_img2 = np.concatenate((row3, row4), axis=0)

    # Display filtered images
    cv.imshow("Mean Filter", disp_img1)
    cv.imshow("Median Filter", disp_img2)

    k = cv.waitKey(0)
    if k == ord("q"):
        cv.destroyAllWindows()
        exit()
