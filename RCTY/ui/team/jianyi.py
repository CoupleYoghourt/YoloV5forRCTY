# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jianyi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMargins, Qt
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 440)
        Form.setStyleSheet("QFrame\n"
"{\n"
"    border: 0px solid;\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"    \n"
"    background-color: rgb(238,238,238);\n"
"}\n"
"QLabel\n"
"{\n"
"    border:0px;\n"
"    \n"
"    font: 9pt \"宋体\";\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 440))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 5, 30, 30))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 500, 400))
        self.frame_2.setStyleSheet("*{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 25, 121, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 131, 30))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 70, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 120, 121, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_3.setGeometry(QtCore.QRect(160, 120, 131, 19))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_4.setGeometry(QtCore.QRect(160, 70, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_5.setGeometry(QtCore.QRect(320, 70, 91, 19))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(180, 320, 140, 45))
        self.pushButton.setStyleSheet("*{\n"
"    background-color: rgb(213,213,213);\n"
"    border:0px solid;\n"
"    border-radius:10px;\n"
"}\n"
"*:hover\n"
"{\n"
"\n"
"    border:1px solid;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 190, 460, 100))
        self.textEdit.setStyleSheet("*{\n"
"    border:1px solid;\n"
"    border-radius:10px;\n"
"    border-color: rgb(225,225,225);\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(470, 10, 20, 20))
        self.toolButton.setStyleSheet("*{\n"
"    border:0px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        self.toolButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.label.setText(_translate("Form", "建议"))
        self.label_2.setText(_translate("Form", "请选择建议类型："))
        self.label_3.setText(_translate("Form", "请输入您的建议："))
        self.checkBox.setText(_translate("Form", "视频播放"))
        self.checkBox_2.setText(_translate("Form", "软件界面操作"))
        self.checkBox_3.setText(_translate("Form", "其它方面的建议"))
        self.checkBox_4.setText(_translate("Form", "录像查看"))
        self.checkBox_5.setText(_translate("Form", "告警消息"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.toolButton.setText(_translate("Form", "关闭"))

