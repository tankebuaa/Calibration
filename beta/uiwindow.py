# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
# 相当于建立的UI函数，只不过包含的实例没有功能
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
        CalibWindow.resize(1115, 795)
        self.widget = QtGui.QWidget(CalibWindow)
        self.widget.setGeometry(QtCore.QRect(30, 30, 177, 43))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.setButton = QtGui.QPushButton(self.widget)
        self.setButton.setObjectName(_fromUtf8("setButton"))
        self.horizontalLayout.addWidget(self.setButton)
        self.playButton = QtGui.QPushButton(self.widget)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.mplCanvas = MplCanvas()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
        self.mplCanvas.setSizePolicy(sizePolicy)
        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))
        self.gridLayout.addWidget(self.mplCanvas, 1, 0, 1, 1)

        self.retranslateUi(CalibWindow)
        QtCore.QMetaObject.connectSlotsByName(CalibWindow)

    def retranslateUi(self, CalibWindow):
        CalibWindow.setWindowTitle(_translate("CalibWindow", "Python标定程序", None))
        self.setButton.setText(_translate("CalibWindow", "Set", None))
        self.playButton.setText(_translate("CalibWindow", "Play", None))


