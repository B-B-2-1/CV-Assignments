import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('naturesample.jpg',0)
cv2.imshow('og-image',img)
cv2.waitKey(0)

height, width = img.shape
N = 5
smoothing_arr = [[[ 0.00730688 , 0.03274718 , 0.05399097 , 0.03274718 , 0.00730688],
 [ 0.03274718 , 0.14676266 , 0.24197072 , 0.14676266 , 0.03274718],
 [ 0.05399097 , 0.24197072 , 0.39894228 , 0.24197072  ,0.05399097],
 [ 0.03274718  ,0.14676266 , 0.24197072  ,0.14676266 , 0.03274718],
 [ 0.00730688,  0.03274718,  0.05399097 , 0.03274718,  0.00730688]]]

print('starting filtering')
for y in range(height):
    for x in range(width):
        sum1 = 0
        for m in range(N):
            for n in range(N):
                sum1 += smoothing_arr[m][n]*img[(y+m)%height][(x+n)%width]
        img[(y+int(N/2))%height][(x+int(N/2))%width] = sum1
cv2.imshow('Image_smoothed.png',img)
cv2.waitKey(0)
