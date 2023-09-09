"""
Exercise 3
Use OpenCV to load and display a color image
Convert it to grayscale

1. Using nested loops
2. Using matrix multiplication
3. Using the built-in OpenCV function

- Simon
"""

import numpy as np
import cv2 as cv
import sys

img_dir = "images/Bente.png"


if __name__ == "__main__":
    img = cv.imread(img_dir)
    # print(img)

    # print(img[0,1,0])

    if img is None:
        print("Image not found")

    # Convert to grayscale nested loop
    img_copy = np.copy(img)
    counti = 0
    for i in img:
        countj = 0
        for j in i:
            x = 0.33 * j[0] + 0.33 * j[1] + 0.33 * j[2]
            img_copy[counti, countj] = [x, x, x]
            countj += 1
        counti += 1
    # print("new line: ",img_copy)

    cv.imshow("Window", img_copy)
    k = cv.waitKey(0)
    if k == ord("q"):
        exit()
