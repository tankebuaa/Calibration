# -*- coding : utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolBar
import datacalib as dc

class MplData(object):
    '''
    存放标定数据的类
    '''
    def __init__(self):
        picName = []#存放文件名的list
        
    def set_picName(self):
        picNmae = dc.data_calib()
class MplCanvas(QtGui.QWidget):
    '''
    mpl的数据和交互类
    '''
    def __init__(self, parent = None):
        super(MplCanvas, self).__init__()
        self.data = None
        self.add_file()
        self.create_canvas(parent)
        
    def create_canvas(self, parent = None):
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolBar(self.canvas, parent)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.toolbar)
        
        self.setLayout(self.layout)
        
    def add_file(self):
        self.data = MplData()
        self.data.set_picName()
        
    def set_para(self):
        pass
        
    def play(self):
        pass