import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread("image.jpg",0)
cv2.imshow('ogFig',img)
cv2.waitKey(0)
#################################gaussian
height, width = img.shape
N = 5
smoothing_arr = [[[ 0.00730688 , 0.03274718 , 0.05399097 , 0.03274718 , 0.00730688],
 [ 0.03274718 , 0.14676266 , 0.24197072 , 0.14676266 , 0.03274718],
 [ 0.05399097 , 0.24197072 , 0.39894228 , 0.24197072  ,0.05399097],
 [ 0.03274718  ,0.14676266 , 0.24197072  ,0.14676266 , 0.03274718],
 [ 0.00730688,  0.03274718,  0.05399097 , 0.03274718,  0.00730688]]]

for y in range(height):
    for x in range(width):
        sum1 = 0
        for m in range(N):
            for n in range(N):
                sum1 += smoothing_arr[m][n]*img[(y+m)%height][(x+n)%width]
        img[(y+int(N/2))%height][(x+int(N/2))%width] = sum1
################################Level1
ans=[]
for i in range(0,340,2):
    temp=[]
    for j in range(0,300,2):
            temp.append(img[i][j])
    if len(temp):
        ans.append(temp)
cv2.imshow()
cv2.waitKey(0)
##################################Gaussian 
height, width = ans.shape
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
        ans[(y+int(N/2))%height][(x+int(N/2))%width] = sum1

######################################level 2        
ans1=[]
for i in range(0,340,2):
    temp=[]
    for j in range(0,300,2):
            temp.append(ans[i][j])
    if len(temp):
        ans1.append(temp)
cv2.imshow('level2',ans1)
cv2.waitKey(0)
####################################Gaussian 
height, width = ans1.shape
N = 5
smoothing_arr = [[[ 0.00730688 , 0.03274718 , 0.05399097 , 0.03274718 , 0.00730688],
 [ 0.03274718 , 0.14676266 , 0.24197072 , 0.14676266 , 0.03274718],
 [ 0.05399097 , 0.24197072 , 0.39894228 , 0.24197072  ,0.05399097],
 [ 0.03274718  ,0.14676266 , 0.24197072  ,0.14676266 , 0.03274718],
 [ 0.00730688,  0.03274718,  0.05399097 , 0.03274718,  0.00730688]]]

for y in range(height):
    for x in range(width):
        sum1 = 0
        for m in range(N):
            for n in range(N):
                sum1 += smoothing_arr[m][n]*img[(y+m)%height][(x+n)%width]
        ans1[(y+int(N/2))%height][(x+int(N/2))%width] = sum1
####################################Level 3
ans2=[]
for i in range(0,340,2):
    temp=[]
    for j in range(0,300,2):
            temp.append(ans1[i][j])
    if len(temp):
        ans2.append(temp)
cv2.imshow('level3',ans2)
cv2.waitKey(0)