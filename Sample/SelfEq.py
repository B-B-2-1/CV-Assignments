import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('pikachu.jpg',0)
equ = cv2.equalizeHist(img)
cv2.imshow('equalized func',img)
width,height = img.shape[:2]

imgarr = img.ravel()
imgarrequ = equ.ravel()

greyscale = []
greyscalequ = []
CDF_arr = []

for x in range(260):
    greyscale.append(0)
    greyscalequ.append(0)
    CDF_arr.append(0)
    
for x in range(width*height):
    loc = imgarr[x]
    greyscale[loc]+=1
    loc = imgarrequ[x]
    greyscalequ[loc]+=1
    
for x in range(1,260):
    CDF_arr[x] = CDF_arr[x-1] + greyscale[x]/(width*height)


for x in range(height):
    for y in range(width):
        loc = img[y][x]
        img[y][x] = 255*CDF_arr[loc]

imgarr = img.ravel()

for x in range(260):
    greyscale.append(0)
    greyscalequ.append(0)
    CDF_arr.append(0)
    
for x in range(width*height):
    loc = imgarr[x]
    greyscale[loc]+=1
        




newx = []
newimg = []
xaxis = []

for x in range(260):
    newx.append(int(255*CDF_arr[x]))
    newimg.append(0)
    xaxis.append(x)
print(newx)    

for x in range(260):
    newimg[(newx[x])] += greyscale[x]
 
plt.bar(xaxis,newimg)

cv2.imshow('equImg',img)
plt.show()
'''    

cv2.imshow('imagegrey',img)
cv2.imshow('equImg',equ)
plt.subplot(1,2,1)
plt.bar(xaxis,greyscale)
plt.subplot(1,2,2)
plt.bar(xaxis,greyscalequ)
plt.show()
'''
