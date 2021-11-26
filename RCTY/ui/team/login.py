# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 489)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test/用户.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAccessibleName("")
        Form.setStyleSheet("*{\n"
"\n"
"font-size:15px;\n"
"font-style:MingLiU-ExtB;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background:white;\n"
"    padding-left:10px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    \n"
"    font: 10pt \"宋体\";\n"
"    border-bottom-right-radius:10px;\n"
"   border: 2px solid rgb(159, 162, 162);\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    padding-top:0px ;\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox{\n"
"    background:rgba(85,170,255,0);\n"
"    color: rgb(0, 0, 0);\n"
"    font-style:MingLiU-ExtB;\n"
"}\n"
"QLabel{\n"
"font-style:MingLiU-ExtB;\n"
"font-size:14px;\n"
"}\n"
"QComboBox\n"
"{\n"
"    \n"
"    font: 10pt \"宋体\";\n"
"    background:white;\n"
"    padding-left:10px ;\n"
"    border-top-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"    border: 2px solid rgb(159, 162, 162);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-image:url(:/test/下箭头 (2).png);\n"
"    width:25px;\n"
"    height:25px;\n"
"}\n"
"QComboBox::down-arrow:hover\n"
"{\n"
"    border-image:url(:/test/下箭头 (2).png);\n"
"    width:30px;\n"
"    height:30px;\n"
"}\n"
"QComboBox::down-arrow:on\n"
"{\n"
"    border-image:url(:/test/下箭头 (2).png);\n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"    width:20px;\n"
"    background:transparent;\n"
"    padding-right:5px;\n"
"}\n"
"\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 521, 491))
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"background:transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 210, 320, 40))
        self.lineEdit_2.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(100, 270, 91, 19))
        self.checkBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"宋体\";\n"
"background:transparent;")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 330, 221, 50))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius:10px;\n"
"    background-color: rgb(42,166,244);\n"
"    font: 24pt \"黑体\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    border-radius:10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"    font: 24pt \"黑体\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    \n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 0, 0);\n"
"    font: 24pt \"黑体\";\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(470, 0, 30, 30))
        self.toolButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.toolButton_2.setStyleSheet("background:transparent;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/test/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 200, 80))
        self.label_2.setStyleSheet("background:transparent;\n"
"font: 30pt \"黑体\";\n"
"color: rgb(136, 136, 136);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(114, 400, 160, 30))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"宋体\";\n"
"background:transparent;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(309, 400, 101, 30))
        self.label_5.setAcceptDrops(False)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"宋体\";\n"
"background:transparent;")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(90, 160, 320, 40))
        self.comboBox.setAccessibleName("")
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxCount(2147483646)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(263, 399, 50, 30))
        self.pushButton_3.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background:transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    font: 10pt \"黑体\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color: rgb(52, 52, 52);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 290, 93, 28))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background:transparent;\n"
"    color: rgb(0, 0, 255);\n"
"    font: 9pt \"黑体\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color: rgb(52, 52, 52);\n"
"    font: 9pt \"黑体\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    \n"
"    color: rgb(170, 0, 0);\n"
"    font: 9pt \"黑体\";\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.toolButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 521, 491))
        self.frame_2.setStyleSheet("image: url(:/test/榕创科技21302.png);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        self.toolButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "密码"))
        self.checkBox.setText(_translate("Form", "自动登录"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.toolButton_2.setText(_translate("Form", "close"))
        self.label_2.setText(_translate("Form", "欢迎登录"))
        self.label_3.setText(_translate("Form", "你还没有账号？那就"))
        self.label_5.setText(_translate("Form", "一个吧~"))
        self.comboBox.setPlaceholderText(_translate("Form", "账号"))
        self.comboBox.setItemText(0, _translate("Form", "qweqe"))
        self.comboBox.setItemText(1, _translate("Form", "qweqeqwe"))
        self.pushButton_3.setText(_translate("Form", "注册"))
        self.pushButton_2.setText(_translate("Form", "忘记密码？"))

import resource_rc
