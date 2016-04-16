#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

def on_press(event):
    if event.inaxes is None: return
    for line in event.inaxes.lines:
        if event.key=='enter':
            visible = line.get_visible()
            line.set_visible(not visible)

    event.inaxes.figure.canvas.draw()
    print("press",event.key,event.xdata)
fig, ax = plt.subplots(1)

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(2, 20))

plt.show()
