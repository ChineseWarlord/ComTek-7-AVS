import numpy as np
import cv2 as cv
import sys

img_dir = "../images/Bente.png"

if __name__ == "__main__":
    """
    Img consists of 3d-array:
    [[[x,x,x], [x,x,x], ... , [x,x,x]]]
    Each index represents RGB(BGR):
    [[[blue, green, red]]]
    """
    # How to read img 3d-array:
    # img[y,x,pixel colors]
    # Bente.png = img[183,273,[BGR]]
    img = cv.imread(img_dir)
    h, w, c = img.shape
    print(f"Width: {w}\nHeight: {h}\nChannel: {c}")

    if img is None:
        print("Image not found")
        exit()

    # Prints row of pixels and their BGR values for each height value
    for i, pixelrow in enumerate(img):
        print(f"Index: {i}, Row of pixels: \n{pixelrow}")

    # Prints column of pixels and their BGR values for each height value
    for i, pixelrow in enumerate(img.transpose(1, 0, 2)):
        print(f"Index: {i}, Column of pixels: \n{pixelrow}")

    # 1. Prints all pixels and their BGR values
    total_pixels = 0
    for row in range(h):
        for col in range(w):
            pixel = img[row, col]
            print(
                f"Row: {row}, Column: {col}, Pixel: {total_pixels}, Pixel BGR: {pixel}")
            total_pixels += 1
            
    # 2. Prints all pixels and their BGR values
    for i, row in enumerate(img):
            for j, col in enumerate(row):
                print(f"[row,col]: [{i},{j}] BGR: {col}")
            
    print(f"Total no. pixels: {total_pixels}")
