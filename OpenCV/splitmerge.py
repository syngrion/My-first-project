from cv2 import cv2 as cv
import numpy as np

img = cv.imread('Photos/Rizal-Park.jpg')
cv.imshow('Rizal Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape) # Blue
print(g.shape) # Green
print(r.shape) # Red

merged = cv.merge([b,g,r])
cv.imshow('Merged image', img)

cv.waitKey()