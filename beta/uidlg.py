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
        SetDialog.resize(679, 346)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetDialog.sizePolicy().hasHeightForWidth())
        SetDialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(SetDialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 290, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.numberLabel = QtGui.QLabel(SetDialog)
        self.numberLabel.setGeometry(QtCore.QRect(50, 50, 54, 12))
        self.numberLabel.setObjectName(_fromUtf8("numberLabel"))
        self.numberEdit = QtGui.QLineEdit(SetDialog)
        self.numberEdit.setGeometry(QtCore.QRect(170, 40, 121, 31))
        self.numberEdit.setObjectName(_fromUtf8("numberEdit"))
        self.wndrLabel = QtGui.QLabel(SetDialog)
        self.wndrLabel.setGeometry(QtCore.QRect(50, 100, 54, 12))
        self.wndrLabel.setObjectName(_fromUtf8("wndrLabel"))
        self.wndrEdit = QtGui.QLineEdit(SetDialog)
        self.wndrEdit.setGeometry(QtCore.QRect(170, 90, 121, 31))
        self.wndrEdit.setObjectName(_fromUtf8("wndrEdit"))
        self.delrLabel = QtGui.QLabel(SetDialog)
        self.delrLabel.setGeometry(QtCore.QRect(50, 150, 54, 12))
        self.delrLabel.setObjectName(_fromUtf8("delrLabel"))
        self.delrEdit = QtGui.QLineEdit(SetDialog)
        self.delrEdit.setGeometry(QtCore.QRect(170, 140, 121, 31))
        self.delrEdit.setObjectName(_fromUtf8("delrEdit"))
        self.crLabel = QtGui.QLabel(SetDialog)
        self.crLabel.setGeometry(QtCore.QRect(380, 200, 54, 12))
        self.crLabel.setObjectName(_fromUtf8("crLabel"))
        self.crEdit = QtGui.QLineEdit(SetDialog)
        self.crEdit.setGeometry(QtCore.QRect(510, 190, 121, 31))
        self.crEdit.setObjectName(_fromUtf8("crEdit"))
        self.gthLabel = QtGui.QLabel(SetDialog)
        self.gthLabel.setGeometry(QtCore.QRect(380, 100, 54, 12))
        self.gthLabel.setObjectName(_fromUtf8("gthLabel"))
        self.gthEdit = QtGui.QLineEdit(SetDialog)
        self.gthEdit.setGeometry(QtCore.QRect(510, 90, 121, 31))
        self.gthEdit.setObjectName(_fromUtf8("gthEdit"))
        self.ethLabel = QtGui.QLabel(SetDialog)
        self.ethLabel.setGeometry(QtCore.QRect(380, 150, 54, 12))
        self.ethLabel.setObjectName(_fromUtf8("ethLabel"))
        self.ethEdit = QtGui.QLineEdit(SetDialog)
        self.ethEdit.setGeometry(QtCore.QRect(510, 140, 121, 31))
        self.ethEdit.setObjectName(_fromUtf8("ethEdit"))
        self.hgLabel = QtGui.QLabel(SetDialog)
        self.hgLabel.setGeometry(QtCore.QRect(380, 50, 91, 16))
        self.hgLabel.setObjectName(_fromUtf8("hgLabel"))
        self.hgEdit = QtGui.QLineEdit(SetDialog)
        self.hgEdit.setGeometry(QtCore.QRect(510, 40, 121, 31))
        self.hgEdit.setObjectName(_fromUtf8("hgEdit"))
        self.gslabel = QtGui.QLabel(SetDialog)
        self.gslabel.setGeometry(QtCore.QRect(50, 200, 81, 16))
        self.gslabel.setObjectName(_fromUtf8("gslabel"))
        self.gsEdit = QtGui.QLineEdit(SetDialog)
        self.gsEdit.setGeometry(QtCore.QRect(170, 190, 121, 31))
        self.gsEdit.setObjectName(_fromUtf8("gsEdit"))

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
        self.hgLabel.setText(_translate("SetDialog", "高斯求导因子", None))
        self.hgEdit.setText(_translate("SetDialog", "3.0", None))
        self.gslabel.setText(_translate("SetDialog", "高斯平滑因子", None))
        self.gsEdit.setText(_translate("SetDialog", "0.5", None))

