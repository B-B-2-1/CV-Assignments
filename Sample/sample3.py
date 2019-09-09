import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('naturesample.jpg',0)
equ = cv2.equalizeHist(img)
width,height = img.shape[:2]

imgarr = img.ravel()
imgarrequ = equ.ravel()

greyscale = []
greyscalequ = []

xaxis = []

for x in range(260):
    greyscale.append(0)
    greyscalequ.append(0)
    xaxis.append(x)
    
for x in range(width*height):
    loc = imgarr[x]
    greyscale[loc]+=1
    loc = imgarrequ[x]
    greyscalequ[loc]+=1 

cv2.imshow('imagegrey',img)
cv2.imshow('equImg',equ)
plt.subplot(1,2,1)
plt.bar(xaxis,greyscale)
plt.subplot(1,2,2)
plt.bar(xaxis,greyscalequ)
plt.show()
