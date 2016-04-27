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
        SetDialog.resize(384, 530)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetDialog.sizePolicy().hasHeightForWidth())
        SetDialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(SetDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 470, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.numberLabel = QtGui.QLabel(SetDialog)
        self.numberLabel.setGeometry(QtCore.QRect(90, 60, 54, 12))
        self.numberLabel.setObjectName(_fromUtf8("numberLabel"))
        self.numberEdit = QtGui.QLineEdit(SetDialog)
        self.numberEdit.setGeometry(QtCore.QRect(160, 50, 121, 31))
        self.numberEdit.setObjectName(_fromUtf8("numberEdit"))
        self.wndrLabel = QtGui.QLabel(SetDialog)
        self.wndrLabel.setGeometry(QtCore.QRect(90, 110, 54, 12))
        self.wndrLabel.setObjectName(_fromUtf8("wndrLabel"))
        self.wndrEdit = QtGui.QLineEdit(SetDialog)
        self.wndrEdit.setGeometry(QtCore.QRect(160, 100, 121, 31))
        self.wndrEdit.setObjectName(_fromUtf8("wndrEdit"))
        self.delrLabel = QtGui.QLabel(SetDialog)
        self.delrLabel.setGeometry(QtCore.QRect(90, 160, 54, 12))
        self.delrLabel.setObjectName(_fromUtf8("delrLabel"))
        self.delrEdit = QtGui.QLineEdit(SetDialog)
        self.delrEdit.setGeometry(QtCore.QRect(160, 150, 121, 31))
        self.delrEdit.setObjectName(_fromUtf8("delrEdit"))
        self.crLabel = QtGui.QLabel(SetDialog)
        self.crLabel.setGeometry(QtCore.QRect(90, 260, 54, 12))
        self.crLabel.setObjectName(_fromUtf8("crLabel"))
        self.crEdit = QtGui.QLineEdit(SetDialog)
        self.crEdit.setGeometry(QtCore.QRect(160, 250, 121, 31))
        self.crEdit.setObjectName(_fromUtf8("crEdit"))
        self.gthLabel = QtGui.QLabel(SetDialog)
        self.gthLabel.setGeometry(QtCore.QRect(90, 310, 54, 12))
        self.gthLabel.setObjectName(_fromUtf8("gthLabel"))
        self.gthEdit = QtGui.QLineEdit(SetDialog)
        self.gthEdit.setGeometry(QtCore.QRect(160, 300, 121, 31))
        self.gthEdit.setObjectName(_fromUtf8("gthEdit"))
        self.ethLabel = QtGui.QLabel(SetDialog)
        self.ethLabel.setGeometry(QtCore.QRect(90, 360, 54, 12))
        self.ethLabel.setObjectName(_fromUtf8("ethLabel"))
        self.ethEdit = QtGui.QLineEdit(SetDialog)
        self.ethEdit.setGeometry(QtCore.QRect(160, 350, 121, 31))
        self.ethEdit.setObjectName(_fromUtf8("ethEdit"))
        self.hgLabel = QtGui.QLabel(SetDialog)
        self.hgLabel.setGeometry(QtCore.QRect(90, 210, 54, 12))
        self.hgLabel.setObjectName(_fromUtf8("hgLabel"))
        self.hgEdit = QtGui.QLineEdit(SetDialog)
        self.hgEdit.setGeometry(QtCore.QRect(160, 200, 121, 31))
        self.hgEdit.setObjectName(_fromUtf8("hgEdit"))

        self.retranslateUi(SetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SetDialog)

    def retranslateUi(self, SetDialog):
        SetDialog.setWindowTitle(_translate("SetDialog", "设置参数", None))
        self.numberLabel.setText(_translate("SetDialog", "经线数", None))
        self.numberEdit.setText(_translate("SetDialog", "36", None))
        self.wndrLabel.setText(_translate("SetDialog", "窗口半宽", None))
        self.wndrEdit.setText(_translate("SetDialog", "25", None))
        self.delrLabel.setText(_translate("SetDialog", "剔除半宽", None))
        self.delrEdit.setText(_translate("SetDialog", "6", None))
        self.crLabel.setText(_translate("SetDialog", "连通半宽", None))
        self.crEdit.setText(_translate("SetDialog", "1", None))
        self.gthLabel.setText(_translate("SetDialog", "灰度阈值", None))
        self.gthEdit.setText(_translate("SetDialog", "0.05", None))
        self.ethLabel.setText(_translate("SetDialog", "特征阈值", None))
        self.ethEdit.setText(_translate("SetDialog", "0.0015", None))
        self.hgLabel.setText(_translate("SetDialog", "高斯因子", None))
        self.hgEdit.setText(_translate("SetDialog", "3.0", None))

