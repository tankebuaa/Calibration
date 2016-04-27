# -*- coding : utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from uiwindow import Ui_CalibWindow# @python.exe -c"import PyQt4.uic.pyuic" name.ui -o name.py
import datacalib as dc

class CalibWnd(Ui_CalibWindow):
    '''
    UI顶层交互界面，包裹wrap数据进行封装
    '''
    def __init__(self):
        super(CalibWnd, self).__init__()
        self.setupUi(self)
        self.setButton.clicked.connect(self.setPara)
        self.playButton.clicked.connect(self.play)
        
    def set_para(self):
        self.mplCanvas.set_para()
        pass
        
    def play():
        self.mplCanvas.play()
        pass
        
def main():
    '''
    主函数
    '''
    app = QtGui.QApplication(sys.argv)
    calib = CalibWnd()
    calib.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()