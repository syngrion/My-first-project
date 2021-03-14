from cv2 import cv2 as cv

img = cv.imread('Photos/_111434467_gettyimages-1143489763.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)


# Reading Videos
#capture = cv.VideoCapture('Videos/Dog.mp4')

#while True:
#    isture, frame = capture.read()
#    cv.imshow('Video', frame)
    
#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break
        
#capture.release()
#cv.destroyAllWindows()