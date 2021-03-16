from cv2 import cv2 as cv

img = cv.imread('Photos/KittenFluffs4.jpg')
cv.imshow('Cats', img)

# Averaging blur
Average =cv.blur(img, (7,7))
cv.imshow('Average blur', Average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian blur', gauss)

# Median blur
median = cv.medianBlur(img, 7)
cv.imshow('Median blur', median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral blur', bilateral)


cv.waitKey()