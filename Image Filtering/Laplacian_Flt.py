import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("image.jpg",0)
#cv2.imshow('fig_og',img)

data=np.asarray(img)
plt.figure()
plt.imshow(data)
plt.show()

high = [[  0  , 1 ,    0 ],
        [1 ,   -4  , 1 ],
        [  0  , 1 ,    0 ]]

new2=[]
for j in range(300-len(high)+1):
    temp=[]
    for k in range(340-len(high)+1):
        temp1=0
        for l in range(len(high)):
            for m in range(len(high)):
                temp1+=high[l][m]*data[k+l][j+m]
        temp.append(temp1)
    new2.append(temp)
new2=np.transpose(new)        

cv2.imshow('Laplacian',new)

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
new=np.asarray(new)

cv2.imshow('GausinFilterd',new)

new1=[]
for j in range(296-len(high)+1):
    temp=[]
    for k in range(336-len(high)+1):
        temp1=0
        for l in range(len(high)):
            for m in range(len(high)):
                temp1+=high[l][m]*new[k+l][j+m]
        temp.append(temp1)
    new1.append(temp)
new1=np.transpose(new1)

cv2.imshow('Lapl_Of_Gaussian',new1)