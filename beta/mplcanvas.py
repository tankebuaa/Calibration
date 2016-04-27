# -*- coding : utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt
from PyQt4 import QtGui, QtCore
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolBar
import datacalib as dc

class MplData(object):
    '''
    存放标定数据的类
    '''
    def __init__(self):
        self.picName = []#存放文件名的list
        self.images = []#保存图像的list，元素为mat
        self.no = -1#当前指向图像的序号
        self.points = []#所有中心点
        
    def set_picName(self):#读入文件名列表
        self.picName = dc.data_calib()
        
    def append_image(self):#读入文件名列表中的图片
        self.no += 1
        name = self.picName[self.no]
        img = cv2.imread(name, 0)
        self.images.append(img)
        
    def set_para(self, *args):
        self.LINE_NUM,self.WND_R,self.DEL_R,self.HESSIAN_SIGMA,self.CONNECT_R,self.GRAY_THR,self.EIGVAL_THR=args[0]
        
    def get_subpixel(self, point):
        return point
        
        
        
class MplCanvas(QtGui.QWidget):
    '''
    mpl的数据和画布交互类
    '''
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.data = None
        self.add_file()
        self.create_canvas()
        
    def create_canvas(self):
        self.fig = plt.figure()
        #self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        
        self.canvas.mpl_connect("button_press_event", self.on_button_press)
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        
        self.connect(self, QtCore.SIGNAL("play_next()"), self.play)
        #self.canvas.updateGeometry()
        self.toolbar = NavigationToolBar(self.canvas, self)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        
        self.setLayout(layout)
        
    def add_file(self):
        self.data = MplData()
        self.data.set_picName()
        
    def set_para(self, *args):
        self.data.set_para(*args)
        
    def play(self):
        ax = plt.gca()
        ax.hold(False)
        try:
            self.data.append_image()
            ax.imshow(self.data.images[self.data.no], cmap = "gray")
            self.canvas.draw()
            print(">>> click the cross point on same circle...")
            self.data.points.append([])
        except IndexError:
            print("There is no image!")
            pass
        
    def on_button_press(self, event):
        if event.inaxes is None:
            return
        if event.button is 1:
            #获得单击点作为估计值
            clickPoint = np.array([event.xdata, event.ydata])
            print(clickPoint)
            #求出精确的中心点
            subpix = self.data.get_subpixel(clickPoint)
            #标记出中心点
            ax = plt.gca()
            ax.hold(True)
            ax.plot(subpix[0], subpix[1], "bo", markerfacecolor = "red")
            y,x = self.data.images[self.data.no].shape
            ax.set_xlim(0, x)
            ax.set_ylim(y, 0)
            self.canvas.draw()
            #存入点列表
            self.data.points[self.data.no].append(subpix)
            
    def on_key_press(self, event):
        #绑定按键事件到画布和工具栏
        key_press_handler(event, self.canvas, self.toolbar)
        if event.key is "enter":
            print(event.key)
        elif event.key is "N":
            self.emit(QtCore.SIGNAL("play_next()"))