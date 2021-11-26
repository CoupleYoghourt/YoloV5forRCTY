# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRusers.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import resource_rc
import Login_sort as LS
import sys
from PyQt5.QtWidgets import QApplication,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMargins, Qt

class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 720)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 520, 720))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"        background-color: rgb(255, 255, 255);\n"  
"        border:1px solid;\n"
"        border-radius:10px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"    border-radius:10px;\n"
"    font: 10pt \"新宋体\";\n"
"    border-color: rgb(48, 48, 48);\n"
"    border:1px solid;\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 14pt \"新宋体\";\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border-color: rgb(109, 96, 255);\n"
"}\n"
"QLabel\n"
"{\n"
"    border:0px solid;\n"
"    font: 9pt \"黑体\";\n"
"    font: 11pt \"新宋体\";\n"
"\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: rgb(0, 0, 255);\n"
"    background:transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    color: rgb(165, 165, 165);\n"
"    background:transparent;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 40, 120, 40))
        self.label.setStyleSheet("color: rgb(163,163,164);\n"
"font: 16pt \"黑体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(12, 505, 80, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(12, 185, 60, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(12, 425, 60, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(12, 265, 80, 30))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(12, 105, 60, 30))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(12, 345, 60, 30))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 100, 390, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 180, 390, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 260, 390, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 340, 390, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 420, 390, 40))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 500, 390, 40))
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(90, 560, 91, 30))
        self.checkBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(180, 560, 161, 30))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 560, 161, 30))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 620, 175, 40))
        self.pushButton_3.setStyleSheet("*{\n"
"    background-color: rgb(70, 70, 255);\n"
"    font: 16pt \"黑体\";\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid;\n"
"    border-radius:10px;\n"
"}\n"
"*:hover\n"
"{\n"
"    background-color: rgb(140, 133, 144);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 630, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(480, 10, 30, 30))
        self.toolButton.setStyleSheet("background:transparent;")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        self.toolButton.clicked.connect(Form.close) # type: ignore
        self.pushButton_3.clicked.connect(lambda: self.Crusers())
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)

        self.label.setText(_translate("Form", "用户注册"))
        self.label_2.setText(_translate("Form", "确认密码"))
        self.label_3.setText(_translate("Form", "账号ID"))
        self.label_4.setText(_translate("Form", "密码"))
        self.label_5.setText(_translate("Form", "手机号码"))
        self.label_6.setText(_translate("Form", "用户名"))
        self.label_7.setText(_translate("Form", "邮箱"))
        self.checkBox.setText(_translate("Form", "我同意"))
        self.pushButton.setText(_translate("Form", "《榕创天眼服务协议》"))
        self.pushButton_2.setText(_translate("Form", "《榕创天眼隐私政策》"))
        self.pushButton_3.setText(_translate("Form", "确认注册"))
        self.pushButton_4.setText(_translate("Form", "返回登录"))

    def Crusers(self):
        self.name = self.lineEdit.text();
        self.id = self.lineEdit_2.text();
        self.phone = self.lineEdit_3.text();
        self.email = self.lineEdit_4.text();
        self.pwd = self.lineEdit_5.text();
        self.comfirm_pwd = self.lineEdit_6.text();
        if self.pwd==self.comfirm_pwd:
            LS.CUsers(self.email,self.id,self.pwd,self.phone,self.name)
        else:
            print("密码不一致！请重新输入密码！")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Ui_Form()
    ex.show()
    sys.exit(app.exec_())