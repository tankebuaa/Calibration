#!/usr/bin/env python3
# coding=utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import timeit


print(timeit.timeit('a@b', setup = 'import numpy as np;a = np.ones((2,2));b = np.ones((2,1))'))    
print(timeit.timeit('np.dot(a,b)', setup = 'import numpy as np;a = np.ones((2,2));b = np.ones((2,1))'))

plt.plot([1.6, 2.7])
plt.show()
print("测试中文")
a = 2
b = 3
