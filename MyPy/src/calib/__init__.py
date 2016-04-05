'''
Created on 2016年3月26日

@author: tanke
'''

#!/usr/bin/env python3
# coding = utf-8

import sys
#import cv2
import numpy as np
import numpy.ctypeslib as npct
from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT, FigureCanvasQTAgg
import datacalib

# 异常申明

class CalibWindow(QtGui.QWidget):
    def __init__(self):
        super(CalibWindow, self).__init__()
        
        # 读入的文件名list
        self.picName = []# 图片文件名列表
        self.images = []# 遍历的图像mat 列表
        
        self.number = -1# 当前载入、处理的文件序号
        self.imgSize = None # 当前图像的尺寸np.array类型
        self.points = []# 当前图像的角点[(x,y),...]
        self.nCorner = -1# 当前图像的取点数目
        
        # 经线数目
        self.sphereSize = None
        
        # plt中的figure实例，即将要显示的图像
        self.fig = plt.figure()
        
        # Gui 对象
        # matplotlib.backend.backend_qt4agg的画布-》转到QObject
        self.canvas = FigureCanvasQTAgg(self.fig)
        # matplotlib.backend.backend_qt4agg的导航工具栏对象->转到QObject
        self.toolBar = NavigationToolbar2QT(self.canvas, self)
        # PyQt4.QtGui中的按钮对象
        self.addFileButton = QtGui.QPushButton("Add File")
        self.addFileButton.clicked.connect(self.add_file) # 信号与槽链接/点击按钮...读取文件名
        # PyQt4.QtGui中的按钮对象
        self.playButton = QtGui.QPushButton("Play images")
        self.playButton.clicked.connect(self.play)# 信号与槽链接 /点击按钮...显示下一幅图像
        
        self.setParaButton = QtGui.QPushButton("Set Parameters")
        self.setParaButton.clicked.connect(self.set_para)
        
        # matplotlib中的鼠标事件和自定义的槽链接/单击...记录角点
        self.canvas.mpl_connect("button_press_event", self.on_button_press)
        
        # matplotlib 中的键盘事件和自定义的槽链/按下...计算一个H
        #self.canvas.mpl_connect("key_press_event", self.on_key_press)
        
        # 自定义信号和槽（每幅图像所有角点，满足条件发射信号，执行显示下一幅图像等操作）
        #self.connect(self, QtCore.SIGNAL("play_next()"), self.play)
        
        # Gui 布局
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolBar)
        layout.addWidget(self.addFileButton)
        layout.addWidget(self.setParaButton)
        layout.addWidget(self.playButton)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.setWindowTitle("Python标定程序")
        
        
    def add_file(self):
        self.picName = datacalib.data_calib()
        self.images = []
        self.number = -1
        
    def set_para(self):
        # 方案一：弹出一个对话框
        
        # 方案二：直接在console中输入
        while self.sphereSize is None:
            try:
                nH = int(input("Please input jingxian number: "))
                #nV = int(input("Please input vertical number:"))
                self.sphereSize = [nH]
            except ValueError:
                print("Error!Please input again!")
                self.sphereSize = None
                pass
        print("Next...")
    
    def play(self):
        ax = plt.gca()
        ax.hold(False)
        try:
            self.number += 1
            name = self.picName[self.number]
            self.images.append(plt.imread(name))
            ax.imshow(self.images[self.number], cmap = plt.cm.gray)
            self.imgSize = np.array(self.images[self.number].shape)
            
            #print(self.images[self.number].dtype) #uin8类型
            
            self.canvas.draw()
            self.nCorner = -1
            print(">>> click the cross point on same circle...")
        except IndexError:
            print("没有图片啦!")
            pass

    def on_button_press(self, event):
        # test
        if event.inaxes is None:
            return
        self.points.append(np.array([event.xdata, event.ydata]))
        self.nCorner += 1
        print(self.nCorner, event.xdata, event.ydata)# 改成画点
        # 角点提取函数test中改event.xdata/ydata
        #criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.001)
        #corners = cv2.cornerSubPix(np.double(self.images[self.number]), np.double(np.array([event.xdata, event.ydata])),(5,5),(-1,-1),criteria)
        #print(corners)
        self.corner_subpix(np.double(self.points[self.nCorner]))
        print(self.points[self.nCorner],self.imgSize)
        
        # 标记出角点
        ax = plt.gca()
        ax.hold(True)
        
        ax.plot(event.xdata, event.ydata, "bo", markerfacecolor = "red")#需要改
        ax.set_xlim(0,self.imgSize[1])
        ax.set_ylim(self.imgSize[0],0)
        self.canvas.draw()
        
        
    # 当按下回车键，计算一个H
    '''
    # 不知道为什么matplotlib的键盘事件无响应...
    def on_key_press(self, event):
        if event.inaxes is None:
            return
    '''
    #重写Qt键盘事件函数  
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            print("enter")
            # 计算H
        
            print(self.nCorner, self.points)
        
        
            # 初始化角点数据
            self.nCorner = -1
            self.points.clear()
            print(">>> click the cross point on same circle OR play next image.")
        '''
        if event.key == QtCore.Qt.Key_0 and self.nCorner == 0:
            # 发射信号，处理下一幅图片
            self.emit(QtCore.SIGNAL("play_next()"))
        '''
    def corner_subpix(self, clickCorner):
        array_img = npct.ndpointer(dtype = np.double, ndim = 2, shape = \
                                   (self.imgSize[0], self.imgSize[1]), flags = "CONTIGUOUS")
        array_xy = npct.ndpointer(dtype = np.double, ndim = 1, shape = (2,), flags = "CONTIGUOUS")
        array_size = npct.ndpointer(dtype = np.int, ndim = 1, shape = (2,), flags = "CONTIGUOUS")
        libCorner = npct.load_library("libC2Py.dll", "d:/Code/eclipse/C2Py/Debug/")
        libCorner.corner_sub_pix.argtypes = [array_img, array_xy, array_size] 
        libCorner.corner_sub_pix.restypes = None
        libCorner.corner_sub_pix(np.double(self.images[self.number]), clickCorner, self.imgSize)   
        #return clickCorner

    
        
# begin        
app = QtGui.QApplication(sys.argv)
calibUi = CalibWindow()
calibUi.show()

sys.exit(app.exec_())