# -*- coding : utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from uiwindow import Ui_CalibWindow
import datacalib as dc

class CalibWnd(Ui_CalibWindow):
    def __init__(self):
        self.data = dc.data_calib()
        super(CalibWnd, self).__init__()
        self.setupUi(self)
        self.setButton.clicked.connect(self.setPara)
        self.playButton.clicked.connect(self.play)
        
    def setPara(self):
        pass
        
    def play(self):
        pass
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    calib = CalibWnd()
    calib.show()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()