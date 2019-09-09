import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('naturesample.jpg',0)
cv2.imshow('fig1',img)

print(np.mean(img))
print(np.std(img))

histogram = [0]*256

width,height = img.shape[:2]

for y in range(height):
    for x in range(width):
        loc = int(img[x,y])
        histogram[loc]+=1

histogram = (histogram - np.mean(histogram))/np.std(histogram)        

cv2.imshow('fig2',img)
        
plt.plot(histogram)
plt.show()
