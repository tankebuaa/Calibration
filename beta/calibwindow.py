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
        self.calibButton.clicked.connect(self.calibrate)
        self.saveButton.clicked.connect(self.save)
        
    def set_para(self):
        self.dlg = Ui_SetDialog()
        self.dlg.setupUi(self.dlg)
        if self.dlg.exec_():
            para = (int(self.dlg.numberEdit.text()), int(self.dlg.wndrEdit.text()),\
            int(self.dlg.delrEdit.text()), float(self.dlg.gsEdit.text()),\
            float(self.dlg.hgEdit.text()), float(self.dlg.gthEdit.text()),\
            float(self.dlg.ethEdit.text()), int(self.dlg.crEdit.text()))
            self.mplCanvas.set_para(para)
        
    def play(self):
        self.mplCanvas.play()
        
    def calibrate(self):
        self.mplCanvas.calibrate()
        
    def save(self):
        self.mplCanvas.save()
        
    def closeEvent(self, event):
        msg = QtGui.QMessageBox.question(self, "Warning", "Are you sure to quit?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
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