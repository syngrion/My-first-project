from cv2 import cv2 as cv

# Reading images
img = cv.imread('Photos/_111434467_gettyimages-1143489763.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


def changeRes(width,height):
    # live video
    capture.set(3,width)
    capture.set(4,height)
    
    
# Reading Videos
capture = cv.VideoCapture('Videos/Dog.mp4')

while True:
    isture, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resize', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
        
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)