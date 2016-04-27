# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uidlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_SetDialog(QtGui.QDialog):
    def setupUi(self, SetDialog):
        SetDialog.setObjectName(_fromUtf8("SetDialog"))
        SetDialog.resize(634, 426)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetDialog.sizePolicy().hasHeightForWidth())
        SetDialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(SetDialog)
        self.buttonBox.setGeometry(QtCore.QRect(260, 360, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.numberLabel = QtGui.QLabel(SetDialog)
        self.numberLabel.setGeometry(QtCore.QRect(90, 60, 54, 12))
        self.numberLabel.setObjectName(_fromUtf8("numberLabel"))
        self.numberEdit = QtGui.QLineEdit(SetDialog)
        self.numberEdit.setGeometry(QtCore.QRect(140, 50, 121, 31))
        self.numberEdit.setObjectName(_fromUtf8("numberEdit"))

        self.retranslateUi(SetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SetDialog)

    def retranslateUi(self, SetDialog):
        SetDialog.setWindowTitle(_translate("SetDialog", "Dialog", None))
        self.numberLabel.setText(_translate("SetDialog", "经线数", None))

