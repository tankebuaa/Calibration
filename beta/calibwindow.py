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
        self.exitButton.clicked.connect(self.exit)
        self.saveButton.clicked.connect(self.save)
        
    def set_para(self):
        self.dlg = Ui_SetDialog()
        self.dlg.setupUi(self.dlg)
        if self.dlg.exec_():
            para = (int(self.dlg.numberEdit.text()), int(self.dlg.wndrEdit.text()),\
            int(self.dlg.delrEdit.text()), float(self.dlg.hgEdit.text()), int(self.dlg.crEdit.text()),\
            float(self.dlg.gthEdit.text()), float(self.dlg.ethEdit.text()))
            self.mplCanvas.set_para(para)
        
    def play(self):
        self.mplCanvas.play()
        
    def save(self):
        pass
        
    def exit(self):
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