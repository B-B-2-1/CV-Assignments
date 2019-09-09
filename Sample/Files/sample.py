import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('naturesample.jpg',0)
cv2.imshow('Image',img);

width,height = img.shape[:2]

xaxis = []
histarr = []
mean = 0
mode = 0
modeval = 0
median = 0
varience = 0

for x in range(256):
    xaxis.append(x)
    histarr.append(0)
    
for y in range(height):
    for x in range(width):
        loc = img[x][y]
        mean += loc/(width*height)
        histarr[loc] += 1
        
for x in range(256):
    if(histarr[x]>modeval):
        modeval = histarr[x]
        mode = x

median = 255/2

print('Mean = ', mean)
print('mode = ', mode)
print('median = ', median)

for x in range(256):
    varience += (1/(height*width))*(x-mean)*(x-mean)*histarr[x]
print('varience = ',varience)    
        
plt.bar(xaxis,histarr)
plt.show()
