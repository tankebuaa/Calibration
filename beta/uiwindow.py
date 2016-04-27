# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from mplcanvas import MplCanvas

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CalibWindow(QtGui.QWidget):
    def setupUi(self, CalibWindow):
        CalibWindow.setObjectName(_fromUtf8("CalibWindow"))
        CalibWindow.resize(800, 600)
        self.setButton = QtGui.QPushButton(CalibWindow)
        self.setButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.setButton.setObjectName(_fromUtf8("setButton"))
        self.playButton = QtGui.QPushButton(CalibWindow)
        self.playButton.setGeometry(QtCore.QRect(130, 20, 75, 23))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.mplCanvas = MplCanvas(CalibWindow)
        self.mplCanvas.setGeometry(QtCore.QRect(20, 60, 800, 600))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
        self.mplCanvas.setSizePolicy(sizePolicy)
        self.mplCanvas.setMinimumSize(QtCore.QSize(800, 600))
        self.mplCanvas.setMaximumSize(QtCore.QSize(4000, 3000))
        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))

        self.retranslateUi(CalibWindow)
        QtCore.QMetaObject.connectSlotsByName(CalibWindow)

    def retranslateUi(self, CalibWindow):
        CalibWindow.setWindowTitle(_translate("CalibWindow", "Python标定程序", None))
        self.setButton.setText(_translate("CalibWindow", "Set", None))
        self.playButton.setText(_translate("CalibWindow", "Play", None))


