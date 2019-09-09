import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("image.jpg",0)
data=np.asarray(img)
cv2.imshow('fig1',data)
cv2.waitKey(0)

fill = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
        [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
        [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
        [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
        [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]

new=[]
for j in range(300-len(fill)+1):
    temp=[]
    for k in range(340-len(fill)+1):
        temp1=0
        for l in range(len(fill)):
            for m in range(len(fill)):
                temp1+=fill[l][m]*data[k+l][j+m]
        temp.append(temp1)
    new.append(temp)
new=np.transpose(new)

cv2.imshow('fig2',new)
cv2.waitKey(0)

high = [[  0  , -.5 ,    0 ],
        [-.5 ,   3  , -.5 ],
        [  0  , -.5 ,    0 ]]

new=[]
for j in range(300-len(high)+1):
    temp=[]
    for k in range(340-len(high)+1):
        temp1=0
        for l in range(len(high)):
            for m in range(len(high)):
                temp1+=fill[l][m]*data[k+l][j+m]
        temp.append(temp1)
    new.append(temp)
new=np.transpose(new)

cv2.imshow('fig3',new)
cv2.waitKey(0)