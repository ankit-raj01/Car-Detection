# Finding optimum threshold for Canny edge detector

import cv2 as cv

img = cv.imread('rgb_imgs/0087.png') 
cv.imshow('Image', img)

def empty(a):
    pass
cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars', 640, 240)
cv.createTrackbar('Threshold 1', 'TrackBars', 150, 255, empty)
cv.createTrackbar('Threshold 2', 'TrackBars', 255, 255, empty)

while True:    
    bilateral = cv.bilateralFilter(img, 5, 80, 200, borderType = cv.BORDER_CONSTANT)     
    gray = cv.cvtColor(bilateral, cv.COLOR_BGR2GRAY)
    Threshold1 = cv.getTrackbarPos('Threshold 1', 'TrackBars')
    Threshold2 = cv.getTrackbarPos('Threshold 2', 'TrackBars')
    canny = cv.Canny(gray, Threshold1, Threshold2)
    cv.imshow('Canny', canny)
    if cv.waitKey(300) & 0xFF == ord('q'):                                             
        break