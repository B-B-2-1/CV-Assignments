import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('pikachu.jpg',0)

width,height = img.shape[:2]

imgarr = img.ravel()

greyscale = []
red = []
green = []
blue = []
xaxis = []

redvalues = []
bluevalues = []
greenvalues = []


for x in range(260):
    greyscale.append(0)
    red.append(0)
    green.append(0)
    blue.append(0)
    xaxis.append(x)
'''    
for x in range(width*height):
    loc = imgarr[x]
    if loc <156:
        loc = 0
    else:
        loc -=156
        loc *=2.56
    greyscale[int(loc)]+=1
'''
plt.bar(xaxis,label = 'greyscale')
plt.show()

cv2.imshow('oGimage',img)
for x in range(width-1):
    for y in range(height-1):
            if img[y][x] <156:
                img[y][x] = 0
            else:
                img[y][x] -=156
                img[y][x] *=2.56
                
cv2.imshow('image',img)

'''
plt.plot(xaxis,red,'r',label = 'Red pixels')
plt.plot(xaxis,green,'g',label = 'green pixels')
plt.plot(xaxis,blue,'b',label = 'blue pixels')
'''
plt.bar(xaxis,greyscale,label = 'greyscale')
plt.show() 
