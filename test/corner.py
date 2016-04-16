'''
Created on 2016年4月14日

@author: tanke
'''
#!/usr/bin/env python3
# coding = utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

'''
import timeit
print(timeit.timeit('a@b', setup = 'import numpy as np;a = np.ones((2,2));b = np.ones((2,1))'))    
print(timeit.timeit('np.dot(a,b)', setup = 'import numpy as np;a = np.ones((2,2));b = np.ones((2,1))'))
'''

img = cv2.imread("d:/Code/matlabspace/calibration/circle_sphere/201602/20160407/Image13.bmp", 0)
plt.ion()
a = 2
fig1 = plt.figure(1)
ax = fig1.add_subplot(1,1,1)
ax.plot(100,100,"bo")

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
ax2.imshow(img, cmap = "gray")

print("It is OK")
