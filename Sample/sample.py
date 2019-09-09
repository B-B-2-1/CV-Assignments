import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('naturesample.jpg',1)

width,height = img.shape[:2]

imgarr = img.ravel()

red = []
green = []
blue = []
xaxis = []

redvalues = []
bluevalues = []
greenvalues = []


for x in range(260):
    red.append(0)
    green.append(0)
    blue.append(0)
    xaxis.append(x)
    
for x in range(width*height):
    loc = imgarr[x*3]
    blue[loc]+=1 
    bluevalues.append(loc)
    loc = imgarr[x*3 +1]
    green[loc]+=1 
    greenvalues.append(loc)
    loc = imgarr[x*3 +2]
    red[loc]+=1 
    redvalues.append(loc)



print("Vatience of red in pixels")
print(np.var(redvalues))
print('and mean is')
print(np.mean(redvalues)) 

print("Vatience of green in pixels")
print(np.var(greenvalues))
print('and mean is')
print(np.mean(greenvalues)) 

print("Vatience of blue in pixels")
print(np.var(bluevalues)) 
print('and mean is')
print(np.mean(bluevalues))

plt.plot(xaxis,red,'r',label = 'Red pixels')
plt.plot(xaxis,green,'g',label = 'green pixels')
plt.plot(xaxis,blue,'b',label = 'blue pixels') 
plt.show() 
