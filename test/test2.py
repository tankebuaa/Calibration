'''
Created on 2016年3月25日

@author: tanke
'''

import numpy as np
import numpy.ctypeslib as npct
#import ctypes

#对c函数进行输入和返回参数类型设置
array_2d_double = npct.ndpointer(dtype = np.double, ndim = 2, shape = (2,2), flags = "CONTIGUOUS")
libexample = npct.load_library("libC2Py.dll", "d:/Code/eclipse/C2Py/Debug/")
libexample.mul.argtypes = [array_2d_double, array_2d_double, array_2d_double]
libexample.mul.restype = None

#直接使用指针对内存进行操作
x = np.array([[3.0, 3.0], [1.0, 1.0]])
y = np.array([[4.0, 4.0], [1.5, 1.5]])
z = np.empty_like(x)
libexample.mul(x, y, z)
print(x,y,z)
#01365672
'''
import sys
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class Window(QtGui.QDialog):
    def __init__(self):
        #super(Window, self).__init__(parent)
        #QtGui.QDialog.__init__(self)
        super().__init__()
        self.img = plt.imread("I1.jpg")
        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        #self.button.clicked.connect(self.plot)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        # plot some random stuff 
        # random data
        #data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.imshow(self.img)

        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
'''