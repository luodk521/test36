# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestForm(object):
    def setupUi(self, TestForm):
        TestForm.setObjectName("TestForm")
        TestForm.resize(778, 590)
        self.label = QtWidgets.QLabel(TestForm)
        self.label.setGeometry(QtCore.QRect(110, 60, 281, 141))
        self.label.setObjectName("label")

        self.retranslateUi(TestForm)
        QtCore.QMetaObject.connectSlotsByName(TestForm)

    def retranslateUi(self, TestForm):
        _translate = QtCore.QCoreApplication.translate
        TestForm.setWindowTitle(_translate("TestForm", "Form"))
        self.label.setText(_translate("TestForm", "哈哈哈……"))

