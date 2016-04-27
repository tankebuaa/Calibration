# -*- coding : utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from uiwindow import Ui_CalibWindow# @python.exe -c"import PyQt4.uic.pyuic" name.ui -o name.py
from uidlg import Ui_SetDialog

class CalibWnd(Ui_CalibWindow):
    '''
    UI顶层交互代码，分离纯界面，并包裹wrap数据进行封装
    '''
    def __init__(self):
        super(CalibWnd, self).__init__()
        self.setupUi(self)
        self.setButton.clicked.connect(self.set_para)
        self.playButton.clicked.connect(self.play)
        
    def set_para(self):
        self.dlg = Ui_SetDialog()
        self.dlg.setupUi(self.dlg)
        if self.dlg.exec_():
            print(int(self.dlg.numberEdit.text()))
            self.mplCanvas.set_para(int(self.dlg.numberEdit.text()))
        
    def play(self):
        self.mplCanvas.play()
        
        
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