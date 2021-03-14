from cv2 import cv2 as cv

img = cv.imread('Photos/City.jpg')
cv.imshow('City', img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=4)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Erode', eroded)

cv.waitKey(0)