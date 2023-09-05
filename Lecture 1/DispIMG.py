"""
Exercise 2
1. Install OpenCV if you haven't already done it
2. Make a program which loads and displays an image using OpenCV
3. Make a program which loops over each pixel and prints its value, row by row.

- Simon
"""

import cv2 as cv
import sys

img_dir = "images/Bente.jfif"

if __name__ == "__main__":
    img = cv.imread(img_dir)
    print(img)

    if img is None:
        print("Image not found")

    cv.imshow("Window", img)
    k = cv.waitKey(0)
    if k == ord("q"):
        exit()
