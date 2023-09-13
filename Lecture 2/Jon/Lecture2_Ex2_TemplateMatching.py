import cv2 as cv
import numpy as np

img = cv.imread('neon-text.png')

#Get size of image and create new blank grayscale image
height, width = img.shape[:2]
gray_image = np.full((height, width), 256, dtype=np.uint8)


templateImg = cv.imread("hearttemplate.jpg")

#Template matching
result = cv.matchTemplate(img, templateImg, cv.TM_CCOEFF_NORMED)

#Find min and max value in result template image
(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(result)

(startX, startY) = maxLoc
endX = startX + templateImg.shape[1]
endY = startY + templateImg.shape[0]

cv.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 3)


cv.imshow("Neon template", img)

cv.waitKey(0)
cv.destroyAllWindows()

# NOTE: as only the highest probable value for the template match making
# is found, only one heart is found. To find all three hearts, just find
# the top 3 highest values in the result image