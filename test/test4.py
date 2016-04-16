#!/usr/bin/env python3
# coding: utf-8

from ctypes import *

from PIL import Image

#import cv2

import numpy as np
import matplotlib.pyplot as plt

dll = CDLL("d:/Code/eclipse/PyDll/Debug/libPyDll.dll")
dll.showImage.argtypes = [c_char_p]
print("OK")

a = None
while a == None:
    try:
        a = int(input("enter file Name:"))
        if a < 0 or a > 1:
            a = None
    except ValueError as err:
        print(err)
print(a)
#path = b"d:/Code/eclipse/MyPy/src/test/left01.png"
path = "d:/Code/eclipse/MyPy/src/test/left0{0}.png".format(a)
print(path)
dll.showImage(path.encode("utf-8"))

im = Image.open(path)
imL = list(im.getdata())
print(len(imL))
cols, rows = im.size
print("width(cols) = {0}, heigth(rows) = {1}, len = {2}".format(cols, rows, cols * rows))
box = (100, 100, 110, 110)
region = im.crop(box)
for x in range(100,110):
    for y in range(100,110):
        rgb = (int(im.getpixel((x,y))[0]/10),int(im.getpixel((x,y))[1]),int(im.getpixel((x,y))[2]/1))
        im.putpixel((x,y), rgb)
        #print(im.getpixel((x, y)))
im.show()

'''
img = cv2.imread("d:/Code/eclipse/MyPy/src/test/left01.png")
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)
'''

imgn = np.zeros((200,200), np.uint8)
fig = plt.figure()
ax = fig.add_subplot(222)
ax.imshow(imgn)
plt.show()
print("Debug")