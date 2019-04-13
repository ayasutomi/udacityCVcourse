import cv2
import numpy as np

img = cv2.imread('imgs/watch.jpg',cv2.IMREAD_GRAYSCALE )
cv2.imshow('watch',img)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)
canny = cv2.Canny(img, 100,200)

cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()