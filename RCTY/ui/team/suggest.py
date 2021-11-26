# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suggest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMargins, Qt
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(753, 763)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(70, 60, 539, 429))
        self.frame.setStyleSheet("*{\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(239,239,239, 255), stop:1 rgba(248,248,248, 255));\n"
"}\n"
"QPushButton\n"
"{\n"
"    border:0px;\n"
"}\n"
"QLabel\n"
"{\n"
"    border:0px;\n"
"}\n"
"QToolButton\n"
"{\n"
"    border:0px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(15, 12, 64, 17))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(506, 10, 31, 20))
        self.toolButton.setStyleSheet("background:transparent;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(475, 10, 31, 20))
        self.toolButton_2.setStyleSheet("background:transparent;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/test/最小化 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 539, 389))
        self.frame_2.setStyleSheet("*{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-color: rgb(172, 172, 172);\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_jianyi = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_jianyi.setGeometry(QtCore.QRect(20, 240, 240, 125))
        self.pushButton_jianyi.setStyleSheet("*{\n"
"    image: url(:/test/建议.png);\n"
"    background:transparent;\n"
"}\n"
"*:pressed{\n"
"    border:1px solid;\n"
"    border-radius:0px;\n"
"}")
        self.pushButton_jianyi.setText("")
        self.pushButton_jianyi.setObjectName("pushButton_jianyi")
        self.pushButton_kuazan = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_kuazan.setGeometry(QtCore.QRect(20, 70, 240, 125))
        self.pushButton_kuazan.setStyleSheet("*{\n"
"    image: url(:/test/夸赞.png);\n"
"    background:transparent;\n"
"}\n"
"*:pressed{\n"
"    border:1px solid;\n"
"    border-radius:0px;\n"
"}\n"
"")
        self.pushButton_kuazan.setText("")
        self.pushButton_kuazan.setObjectName("pushButton_kuazan")
        self.pushButton_tucao = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_tucao.setGeometry(QtCore.QRect(280, 70, 240, 125))
        self.pushButton_tucao.setStyleSheet("*{\n"
"    image: url(:/test/吐槽.png);\n"
"    background:transparent;\n"
"}\n"
"*:pressed{\n"
"    border:1px solid;\n"
"    border-radius:0px;\n"
"}")
        self.pushButton_tucao.setText("")
        self.pushButton_tucao.setObjectName("pushButton_tucao")
        self.pushButton_qiuzhu = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_qiuzhu.setGeometry(QtCore.QRect(280, 240, 240, 125))
        self.pushButton_qiuzhu.setStyleSheet("*{\n"
"    image: url(:/test/求助.png);\n"
"    background:transparent;\n"
"}\n"
"*:pressed{\n"
"    border:1px solid;\n"
"    border-radius:0px;\n"
"}")
        self.pushButton_qiuzhu.setText("")
        self.pushButton_qiuzhu.setObjectName("pushButton_qiuzhu")

        self.retranslateUi(Form)
        self.toolButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.label.setText(_translate("Form", "意见留言"))
        self.toolButton.setText(_translate("Form", "..."))
        self.toolButton_2.setText(_translate("Form", "..."))

