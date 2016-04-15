'''
Created on 2016年4月1日

@author: tanke
'''

#!/usr/bin/env python3
# coding = utf-8

import sys
import cv2
import numpy as np
import numpy.ctypeslib as npct
from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg, NavigationToolbar2QT
import datacalib as dc
import solvehomo as sh

'''
    @param CalibData 是封装标定数据和提供图像处理计算函数的类
    
'''
class CalibData(object):
    def __init__(self):
        # 读入的文件名list
        self.picName = []# 图片文件名列表
        
        self.images = []# 遍历的图像mat 列表
        self.number = -1# 当前载入、处理的文件序号
        self.imgSize = None # 当前图像的尺寸np.array类型
        
        self.corners = []# 计算当前单应的角点列表[(x,y),...]
        self.nCorner = -1# 计算当前单应的圆上的取点序号，总数为+1
        
        # 经纬球参数
        self.sphereSize = None
        
    def set_picName(self):
        self.picName = dc.data_calib()
    
    def append_image(self):
        self.number += 1
        name = self.picName[self.number]
        img = cv2.GaussianBlur(plt.imread(name), (5,5), 0)
        self.images.append(img)
        self.imgSize = np.array(self.current_image().shape)
        
    def current_image(self):
        #print(self.images[self.number].dtype) #uin8类型
        return self.images[self.number]
       
    def append_corner(self, val):
        self.corners.append(val)
        self.nCorner += 1
    
    def current_corner(self):
        return self.corners[self.nCorner]
    
    def init_corners(self):
        self.nCorner = -1
        self.corners.clear()
    
    def set_sphereSize(self):
        while self.sphereSize is None:
            try:
                nH = int(input("Please input jingxian number: "))
                #nV = int(input("Please input vertical number:"))
                self.sphereSize = nH
            except ValueError:
                print("Error!Please input again!")
                self.sphereSize = None
                pass
    def corner_subpix(self, clickPoint):
        # 方案一：调用python的OpenCV角点提取函数cornerSubPix
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.001)
        subpix = cv2.cornerSubPix(np.float32(self.images[self.number]), np.float32(np.array([clickPoint])),(5,5),(-1,-1),criteria)
        return subpix
        '''
        # 方案二：调用C程序
        array_img = npct.ndpointer(dtype = np.double, ndim = 2, shape = \
                                   (self.imgSize[0], self.imgSize[1]), flags = "CONTIGUOUS")
        array_xy = npct.ndpointer(dtype = np.double, ndim = 1, shape = (2,), flags = "CONTIGUOUS")
        array_size = npct.ndpointer(dtype = np.int, ndim = 1, shape = (2,), flags = "CONTIGUOUS")
        libCorner = npct.load_library("libC2Py.dll", "d:/Code/eclipse/C2Py/Debug/")
        libCorner.corner_sub_pix.argtypes = [array_img, array_xy, array_size]
        libCorner.corner_sub_pix.restypes = None
        
        libCorner.corner_sub_pix(np.double(self.current_image()), np.double(clickPoint), self.imgSize)
        '''
        
    def solve_homography(self):
        sh.compute_homography(self.corners, self.nCorner + 1, self.sphereSize)
        ## 需要补充
        pass
        
'''
    @param CalibWindow 是 封装GUI的pyqt4、matplotlib的类
    mpl_ref:2657
'''        
class CalibWindow(QtGui.QWidget):
    def __init__(self):
        super(CalibWindow, self).__init__()
        
        # 标定数据实例
        self.data = None
        self.add_file()
        self.set_para()
        self.create_window()
        
    def create_window(self):
        # plt中的figure实例，即将要显示的图像
        self.fig = plt.figure()
        
        # Gui 对象
        # matplotlib.backend.backend_qt4agg的画布-》转到QObject
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)#QtCore.Qt.StrongFocus接受Tab和鼠标点击来激活当前焦点
        self.canvas.setFocus()
        # matplotlib.backend.backend_qt4agg的导航工具栏对象->转到QObject
        self.toolBar = NavigationToolbar2QT(self.canvas, self)
        
        # PyQt4.QtGui中的按钮对象
        self.playButton = QtGui.QPushButton("Play images")
        self.playButton.clicked.connect(self.play)# 信号与槽链接 /点击按钮...显示下一幅图像
        
        # matplotlib中的鼠标事件和自定义的槽链接/单击...记录角点
        self.canvas.mpl_connect("button_press_event", self.on_button_press)
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        
        # 自定义Qt事件与槽链接
        self.connect(self, QtCore.SIGNAL("play_next()"), self.play)
        
        # Gui 布局
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.playButton)
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolBar)
        
        self.setLayout(layout)
        self.setWindowTitle("Python标定程序")
        
        
    def add_file(self):
        self.data = CalibData()# 初始化标定数据实例
        self.data.set_picName()# 读取图像文件名序列
        
    def set_para(self):
        self.data.set_sphereSize()
        print("Play Image...")
    
    def play(self):
        ax = plt.gca()
        ax.hold(False)
        try:
            self.data.append_image()
            ax.imshow(self.data.current_image(), cmap = "gray")
            self.data.init_corners()
            self.canvas.draw()
            print(">>> click the cross point on same circle...")
        except IndexError:
            print("没有图片啦!")
            pass

    def on_button_press(self, event):
        if event.inaxes is None:
            return
        if event.button is 1:
            clickPoint = np.array([event.xdata, event.ydata])
            print(clickPoint)
            subpix = self.data.corner_subpix(clickPoint)
            self.data.append_corner(subpix)
            print(self.data.nCorner, self.data.current_corner(), self.data.imgSize)# 改成画点
        
            # 标记出单击点
            ax = plt.gca()
            ax.hold(True)
        
            ax.plot(event.xdata, event.ydata, "bo", markerfacecolor = "red")
            ax.set_xlim(0,self.data.imgSize[1])
            ax.set_ylim(self.data.imgSize[0],0)
            self.canvas.draw()
            
    def on_key_press(self, event):
        '''
                            当按下回车键，计算一个H;按下SHift+n，处理下一副图像
        '''
        key_press_handler(event, self.canvas, self.toolBar)# 绑定mpl按键到画布和工具栏
        if event.key is "enter":
            # 计算H
            if self.data.nCorner > 2:
                print("Compute H...")
                self.data.solve_homography()
                #print(self.data.nCorner + 1, self.data.corners)
            else:
                print("Not enough corners!")
            # 初始化单应的角点列表数据
            self.data.init_corners()
            print(">>> click the cross point on same circle OR play next image.")
        elif event.key is "N":
            print(event.key)
            self.emit(QtCore.SIGNAL("play_next()"))
            
    '''
    #重写Qt键盘事件函数  
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            #print("enter")
            # 计算H
            if self.data.nCorner > 2:
                print("Compute H...")
                self.data.solve_homography()
                #print(self.data.nCorner + 1, self.data.corners)
            else:
                print("Not enough corners!")
            # 初始化单应的角点列表数据
            self.data.init_corners()
            print(">>> click the cross point on same circle OR play next image.")
        
        if event.key == QtCore.Qt.Key_0 and self.nCorner == 0:
            # 发射信号，处理下一幅图片
            self.emit(QtCore.SIGNAL("play_next()"))
        '''
            
def main():
    app = QtGui.QApplication(sys.argv)
    calibUi = CalibWindow()
    calibUi.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
        