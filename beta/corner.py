#!/usr/bin/env python3
# coding=utf-8

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

'''
    选取初值点，对范围内的点提取亚像素点，遍历半径（在阈值内）内剔除，得到两条曲线,用八联通搜寻分组，计算斜率分类两条曲线，分别拟合，计算交点
    选点应该对称，靠近摄像机，多幅图像，计算单应
'''
img = cv2.imread("d:/Code/matlabspace/calibration/circle_sphere/201602/20160407/Image12.bmp",0)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.imshow(img,cmap = "gray")
ax2 = fig.add_subplot(122)
blur = cv2.GaussianBlur(img, (7,7), 1.0)
ax2.imshow(blur, cmap = "gray")

# Fast
fast = cv2.FastFeatureDetector_create()
kp = fast.detect(blur, None)
img2 = np.empty_like(img)
img2 = cv2.drawKeypoints(blur, kp, img2, color = (255,0,0))
plt.figure()
plt.subplot(1,2,1), plt.imshow(img2, cmap = "gray"), plt.title("NonMaxSuppresion")

# unuse nonmaxsuppersion
#te = fast.getNonmaxSuppression() 是False
fast.setNonmaxSuppression(False)
kp = fast.detect(blur, None)
img3 = np.empty_like(img)
img3 = cv2.drawKeypoints(blur, kp, img3, color = (0,255,0))
plt.subplot(1,2,2), plt.imshow(img3, cmap="gray"), plt.title("Set NonMaxSuppresion")

# fft变换
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
result = 20 * np.log(np.abs(fshift))
plt.figure()
plt.imshow(result, cmap = "gray")

plt.show()
os.system("pause")

