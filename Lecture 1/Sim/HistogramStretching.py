"""
Exercise 1
1. Design an algorithm which can do histogram stretching.

- Simon
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import time

img_dir = "../images/Einstein.tif"

def stretch(img):
    min = np.min(img)
    max = np.max(img)
    
    img = np.uint8((img - min) * 255.0 / (max - min))
    
    return img

if __name__ == "__main__":
    # Read the img
    img_color = cv.imread(img_dir)
    h, w, c = img_color.shape
    print(f"Width: {w}\nHeight: {h}\nChannel: {c}")
    
    # Convert to grayscale
    img_gray = np.copy(img_color)
    for i, row in enumerate(img_color):
        for j, col in enumerate(row):
            x = 1/3 * col[0] + 1/3 * col[1] + 1/3 * col[2]
            img_gray[i,j] = [x,x,x]
    
    ##############################################
    # Test [counting 0-255] then plot histogram
    img_gray2 = cv.imread(img_dir, cv.IMREAD_GRAYSCALE)
    pixel_count =  np.zeros(256, dtype="uint8")     
    for pixel_value in img_gray2.ravel():
        pixel_count[pixel_value] += 1
    
    print(pixel_count)
    
    # Plot the histogram
    plt.bar(range(256), pixel_count)
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.title('Grayscale2 Image Histogram')
    plt.show()
    ##############################################
            
    # Stretch histogram
    img_stretch = stretch(img_gray)
    
    # Split the image into its color channels
    b, g, r = cv.split(img_color)

    # Create a figure with three subplots
    fig, axs = plt.subplots(1, 5, figsize=(15, 5))

    # Plot the histograms for grayscale, stretched grayscale and each color channel
    axs[0].hist(img_gray.ravel(), 256, [0, 256], color='gray')
    axs[0].set_xlabel('Intensity')
    axs[0].set_ylabel('Frequency')
    axs[0].set_title('Histogram for Grayscale image')
    
    axs[1].hist(img_stretch.ravel(), 256, [0, 256], color='gray')
    axs[1].set_xlabel('Intensity')
    axs[1].set_ylabel('Frequency')
    axs[1].set_title('Histogram for Stretched Grayscale image')
    
    axs[2].hist(b.ravel(), 256, [0, 256], color='blue')
    axs[2].set_xlabel('Intensity')
    axs[2].set_ylabel('Frequency')
    axs[2].set_title('Histogram for Blue Channel')

    axs[3].hist(g.ravel(), 256, [0, 256], color='green')
    axs[3].set_xlabel('Intensity')
    axs[3].set_ylabel('Frequency')
    axs[3].set_title('Histogram for Green Channel')

    axs[4].hist(r.ravel(), 256, [0, 256], color='red')
    axs[4].set_xlabel('Intensity')
    axs[4].set_ylabel('Frequency')
    axs[4].set_title('Histogram for Red Channel')
    
    # Show images
    imgs = np.concatenate((img_gray,img_stretch,img_color),axis=1)
    cv.namedWindow("Window",cv.WINDOW_NORMAL)
    cv.imshow("Window", imgs)
    
    # Adjust spacing between subplots
    plt.tight_layout()
    plt.show()
    
    k = cv.waitKey(0)
    if k == ord("q"):
        #cv.destroyAllWindows()
        exit()




