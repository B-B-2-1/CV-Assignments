import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

imgref=cv2.imread("CV_img1.jpg",0)
plt.subplot(2,2,1)
plt.imshow(imgref)

resultimg1 = imgref

height, width = imgref.shape

img=cv2.imread("CV_img2.jpg",0)
plt.subplot(2,2,2)
plt.imshow(img)

resultimg2 = img

for i in range(256):
    sum=0
    l=0
    for j in range(height):
        for k in range(width):
            if imgref[j][k]==i:
                sum+=img[j][k]
                l+=1
    if(l!=0):            
        val=np.ceil(sum/l)
    else:
        val = 0    
    for j in range(height):
        for k in range(width):
            if imgref[j][k]==i:
                img[j][k]=val

plt.subplot(2,2,3)
plt.imshow(img)

imgref=cv2.imread("CV_img2.jpg",0)
img=cv2.imread("CV_img1.jpg",0)

for i in range(256):
    sum=0
    l=0
    for j in range(height):
        for k in range(width):
            if imgref[j][k]==i:
                sum+=img[j][k]
                l+=1
    if(l!=0):            
        val=np.ceil(sum/l)
    else:
        val = 0    
    for j in range(height):
        for k in range(width):
            if imgref[j][k]==i:
                img[j][k]=val

plt.subplot(2,2,4)
plt.imshow(img)
plt.show()
