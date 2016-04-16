'''
Created on 2016年3月25日

@author: tanke
'''
#!/usr/bin/env python

#import numpy as np
import cv2
import matplotlib.pyplot as plt

# 读入为num.array类型:M*N*D
img = cv2.imread("I1.jpg")
b, g, r = cv2.split(img)
img2 = cv2.merge([r,g,b])

## OpenCV 默认读入和输出为BGR
cv2.namedWindow("imgBGR")
cv2.imshow("imgBGR", img)
cv2.waitKey(0)

cv2.namedWindow("imgRGB")
cv2.imshow("imgRGB", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

## MatPlot 默认读入和输出为RGB
fig = plt.figure()
#BGR
ax1 = fig.add_subplot(2,1,1)
ax1.imshow(img)
plt.xticks([]),plt.yticks([])
#RGB
ax2 = fig.add_subplot(2,1,2)
ax2.imshow(img2)
plt.xticks([]),plt.yticks([])
#show in matplot
plt.show()
'''
mat = np.float32(img)
print(mat[100,100,1])

'''
