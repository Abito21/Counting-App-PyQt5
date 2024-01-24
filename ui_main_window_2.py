# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(777, 450)
        self.control_bt_2 = QtWidgets.QPushButton(Form)
        self.control_bt_2.setGeometry(QtCore.QRect(640, 120, 75, 23))
        self.control_bt_2.setObjectName("control_bt_2")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(120, 80, 501, 291))
        self.image_label.setFrameShape(QtWidgets.QFrame.Box)
        self.image_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(640, 90, 75, 23))
        self.control_bt.setObjectName("control_bt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.control_bt_2.setText(_translate("Form", "Pause"))
        self.image_label.setText(_translate("Form", "Webcam atau File Video"))
        self.control_bt.setText(_translate("Form", "Start"))

