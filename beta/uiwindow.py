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

class Ui_CalibWindow(QtGui.QMainWindow):
    def setupUi(self, CalibWindow):
        CalibWindow.setObjectName(_fromUtf8("CalibWindow"))
        CalibWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalibWindow.sizePolicy().hasHeightForWidth())
        CalibWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(CalibWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.setButton = QtGui.QPushButton(self.centralwidget)
        self.setButton.setObjectName(_fromUtf8("setButton"))
        self.gridLayout_2.addWidget(self.setButton, 0, 0, 1, 1)
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.gridLayout_2.addWidget(self.playButton, 0, 1, 1, 1)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout_2.addWidget(self.saveButton, 0, 2, 1, 1)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.gridLayout_2.addWidget(self.exitButton, 0, 3, 1, 1)
        self.mplCanvas = MplCanvas(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
        self.mplCanvas.setSizePolicy(sizePolicy)
        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))
        self.gridLayout_2.addWidget(self.mplCanvas, 1, 0, 1, 4)
        CalibWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CalibWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        CalibWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CalibWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CalibWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CalibWindow)
        QtCore.QMetaObject.connectSlotsByName(CalibWindow)

    def retranslateUi(self, CalibWindow):
        CalibWindow.setWindowTitle(_translate("CalibWindow", "Python标定程序", None))
        self.setButton.setText(_translate("CalibWindow", "Set", None))
        self.playButton.setText(_translate("CalibWindow", "Play", None))
        self.saveButton.setText(_translate("CalibWindow", "Save", None))
        self.exitButton.setText(_translate("CalibWindow", "Exit", None))


