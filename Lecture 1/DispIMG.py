import cv2 as cv
import sys

img_dir = "images/"

if __name__ == "__main__":
    img = cv.imread(img_dir)
    
    if img is None:
        print('Image not found')
        
    cv.imshow("Window",img)
    k = cv.waitKey(0)
    if k == ord("q"):
        exit(0)