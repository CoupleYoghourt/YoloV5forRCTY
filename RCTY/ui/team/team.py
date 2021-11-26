# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 810)
        MainWindow.setMinimumSize(QtCore.QSize(450, 810))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 810))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 810))
        self.centralwidget.setMaximumSize(QtCore.QSize(1338, 863))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 810))
        self.frame.setMinimumSize(QtCore.QSize(1280, 810))
        self.frame.setMaximumSize(QtCore.QSize(1327, 839))
        self.frame.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 49, 210, 729))
        self.tabWidget.setMinimumSize(QtCore.QSize(210, 729))
        self.tabWidget.setMaximumSize(QtCore.QSize(210, 760))
        self.tabWidget.setStyleSheet("*{\n"
"\n"
"    background-color: rgb（250,250,250）;\n"
"}\n"
"\n"
"\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(37, 35))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(170, 1, 40, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton.setStyleSheet("*{\n"
"    background:transparent;\n"
"    background-color: rgb(225,223,223);\n"
"    border:0px;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/test/搜索.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 173, 31))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.lineEdit_3.setStyleSheet("*{\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(0, 30, 208, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(0, 60, 207, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_myVideo = QtWidgets.QComboBox(self.tab)
        self.comboBox_myVideo.setGeometry(QtCore.QRect(0, 90, 207, 31))
        self.comboBox_myVideo.setObjectName("comboBox_myVideo")
        self.comboBox_myVideo.addItem("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/test/用户-角色-用户名-单人_jurassic (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/test/用户-角色-用户名-单人_jurassic.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/test/消息 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/test/消息 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/test/功能管理 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/test/功能管理.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1280, 50))
        self.widget_2.setMinimumSize(QtCore.QSize(1280, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(1280, 50))
        self.widget_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(239,239,239, 255), stop:1 rgba(248,248,248, 255));\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(0, 5, 50, 40))
        self.label_3.setStyleSheet("background:transparent;\n"
"image: url(:/test/榕创科技LOGO-02.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(56, 5, 311, 40))
        self.label_4.setStyleSheet("font: 14pt \"黑体\";\n"
"background:transparent;")
        self.label_4.setObjectName("label_4")
        self.pushButton_logout = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_logout.setGeometry(QtCore.QRect(1213, 19, 41, 28))
        self.pushButton_logout.setStyleSheet("*{\n"
"        background:transparent;\n"
"}\n"
"*:hover{\n"
"    color: rgb(42,166,244);\n"
"}")
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_10.setGeometry(QtCore.QRect(1099, 20, 31, 28))
        self.pushButton_10.setStyleSheet("    background:transparent;")
        self.pushButton_10.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/test/用户.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.username = QtWidgets.QLabel(self.widget_2)
        self.username.setGeometry(QtCore.QRect(1128, 19, 81, 28))
        self.username.setObjectName("username")
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setGeometry(QtCore.QRect(211, 52, 1070, 660))
        self.widget_3.setMinimumSize(QtCore.QSize(1070, 660))
        self.widget_3.setMaximumSize(QtCore.QSize(1070, 660))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setGeometry(QtCore.QRect(791, 75, 275, 275))
        self.textBrowser.setMinimumSize(QtCore.QSize(275, 275))
        self.textBrowser.setMaximumSize(QtCore.QSize(275, 275))
        self.textBrowser.setStyleSheet("background-color: rgb（250,250,250）;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_8.setGeometry(QtCore.QRect(791, 382, 275, 275))
        self.textBrowser_8.setMinimumSize(QtCore.QSize(275, 275))
        self.textBrowser_8.setMaximumSize(QtCore.QSize(275, 275))
        self.textBrowser_8.setStyleSheet("background-color: rgb（250,250,250）;")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(788, 43, 281, 32))
        self.label_7.setStyleSheet("background-color: rgb(225,223,223);\n"
"\n"
"font: 9pt \"宋体\";")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(788, 350, 281, 32))
        self.label_2.setStyleSheet("background-color: rgb(225,223,223);\n"
"font: 9pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.line_5 = QtWidgets.QFrame(self.widget_3)
        self.line_5.setGeometry(QtCore.QRect(0, 42, 1070, 1))
        self.line_5.setStyleSheet("")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(0, 46, 785, 610))
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.line_9 = QtWidgets.QFrame(self.widget_3)
        self.line_9.setGeometry(QtCore.QRect(788, 42, 3, 620))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setGeometry(QtCore.QRect(-2, -1, 1071, 42))
        self.widget_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(239,239,239, 255), stop:1 rgba(248,248,248, 255));\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_6.setGeometry(QtCore.QRect(890, 0, 80, 42))
        self.pushButton_6.setStyleSheet("*{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    font: 9pt \"宋体\";\n"
"    background:transparent;\n"
"}\n"
"*:hover\n"
"{\n"
"    color: rgb(42,166,244);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/test/云上传.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_feedBack = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_feedBack.setGeometry(QtCore.QRect(983, 0, 85, 42))
        self.pushButton_feedBack.setStyleSheet("*{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    font: 9pt \"宋体\";\n"
"    background:transparent;\n"
"}\n"
"*:hover\n"
"{\n"
"    color: rgb(42,166,244);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/test/消息 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_feedBack.setIcon(icon6)
        self.pushButton_feedBack.setObjectName("pushButton_feedBack")
        self.line_10 = QtWidgets.QFrame(self.widget_8)
        self.line_10.setGeometry(QtCore.QRect(974, 7, 3, 29))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 120, 40))
        self.label_6.setStyleSheet("font: 20pt \"黑体\";\n"
"border:0px;")
        self.label_6.setObjectName("label_6")
        self.textBrowser.raise_()
        self.textBrowser_8.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.line_5.raise_()
        self.line_9.raise_()
        self.widget_8.raise_()
        self.label.raise_()
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(208, 750, 1073, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(212, 709, 1070, 2))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(207, 51, 2, 760))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.widget_7 = QtWidgets.QWidget(self.frame)
        self.widget_7.setGeometry(QtCore.QRect(208, 756, 1073, 56))
        self.widget_7.setMinimumSize(QtCore.QSize(1070, 40))
        self.widget_7.setStyleSheet("QWidget\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(239,239,239, 255), stop:1 rgba(248,248,248, 255));\n"
"}\n"
"QPushButton{\n"
"    border:1px solid;\n"
"}    \n"
"QPushButton:hover\n"
"{\n"
"    border-color:  rgb(42,166,244);\n"
"}\n"
"QPushButton:checked\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.pushButton_img = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_img.setGeometry(QtCore.QRect(20, 12, 75, 35))
        self.pushButton_img.setStyleSheet("*{\n"
"\n"
"    border-top-left-radius:5px;\n"
"    border-bottom-left-radius:5px;\n"
"\n"
"}\n"
"")
        self.pushButton_img.setCheckable(True)
        self.pushButton_img.setChecked(True)
        self.pushButton_img.setAutoExclusive(True)
        self.pushButton_img.setObjectName("pushButton_img")
        self.pushButton_video = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_video.setGeometry(QtCore.QRect(90, 12, 75, 35))
        self.pushButton_video.setToolTipDuration(-1)
        self.pushButton_video.setStyleSheet("\n"
"")
        self.pushButton_video.setCheckable(True)
        self.pushButton_video.setAutoExclusive(True)
        self.pushButton_video.setDefault(False)
        self.pushButton_video.setObjectName("pushButton_video")
        self.pushButton_camer = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_camer.setGeometry(QtCore.QRect(160, 12, 85, 35))
        self.pushButton_camer.setStyleSheet("*{\n"
"\n"
"    border-top-right-radius:5px;\n"
"    border-bottom-right-radius:5px;\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton_camer.setCheckable(True)
        self.pushButton_camer.setAutoExclusive(True)
        self.pushButton_camer.setObjectName("pushButton_camer")
        self.pushButton_finish = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_finish.setGeometry(QtCore.QRect(748, 12, 40, 35))
        self.pushButton_finish.setStyleSheet("*{\n"
"    border:1px solid;\n"
"    border-radius:5px;\n"
"    font: 9pt \"仿宋\";\n"
"}\n"
"")
        self.pushButton_finish.setCheckable(True)
        self.pushButton_finish.setAutoExclusive(True)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.pushButton_video.raise_()
        self.pushButton_finish.raise_()
        self.pushButton_img.raise_()
        self.pushButton_camer.raise_()
        self.widget_6 = QtWidgets.QWidget(self.frame)
        self.widget_6.setGeometry(QtCore.QRect(209, 711, 1071, 51))
        self.widget_6.setMinimumSize(QtCore.QSize(1070, 40))
        self.widget_6.setStyleSheet("*{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(239,239,239, 255), stop:1 rgba(248,248,248, 255));\n"
"}\n"
"QPushButton{\n"
"    border:1px solid;\n"
"    border-top-left-radius:5px;\n"
"    border-bottom-left-radius:5px;\n"
"    background-color: rgb(231,231,231);\n"
"}    \n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    border-color:  rgb(42,166,244);\n"
"}\n"
"QPushButton:checked\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton{\n"
"    border:1px solid;\n"
"    border-top-right-radius:5px;\n"
"    border-bottom-right-radius:5px;\n"
"    background-color: rgb(231,231,231);\n"
"}    \n"
"QToolButton:hover\n"
"{\n"
"    \n"
"    border-color:  rgb(42,166,244);\n"
"}\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.toolButton_11 = QtWidgets.QToolButton(self.widget_6)
        self.toolButton_11.setGeometry(QtCore.QRect(60, 5, 40, 40))
        self.toolButton_11.setStyleSheet("*{\n"
"    border:0px;\n"
"background:transparent;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/test/音量.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon7)
        self.toolButton_11.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_11.setObjectName("toolButton_11")
        self.pushButton_29 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_29.setGeometry(QtCore.QRect(930, 10, 80, 25))
        self.pushButton_29.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_29.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_29.setStyleSheet("")
        self.pushButton_29.setCheckable(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.toolButton_12 = QtWidgets.QToolButton(self.widget_6)
        self.toolButton_12.setGeometry(QtCore.QRect(1009, 10, 25, 25))
        self.toolButton_12.setMinimumSize(QtCore.QSize(25, 25))
        self.toolButton_12.setMaximumSize(QtCore.QSize(25, 25))
        self.toolButton_12.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/test/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon8)
        self.toolButton_12.setCheckable(True)
        self.toolButton_12.setObjectName("toolButton_12")
        self.pushButton_stop = QtWidgets.QToolButton(self.widget_6)
        self.pushButton_stop.setGeometry(QtCore.QRect(10, 5, 40, 40))
        self.pushButton_stop.setStyleSheet("*{\n"
"    border:0px;\n"
"    background:transparent;\n"
"    image: url(:/test/已停止.png);\n"
"}\n"
"        \n"
"")
        self.pushButton_stop.setText("")
        self.pushButton_stop.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_start = QtWidgets.QToolButton(self.widget_6)
        self.pushButton_start.setGeometry(QtCore.QRect(10, 5, 40, 40))
        self.pushButton_start.setStyleSheet("*{\n"
"    border:0px;\n"
"    background:transparent;\n"
"    image: url(:/test/播放.png);\n"
"}")
        self.pushButton_start.setText("")
        self.pushButton_start.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_start.setObjectName("pushButton_start")
        self.toolButton_11.raise_()
        self.pushButton_29.raise_()
        self.toolButton_12.raise_()
        self.pushButton_start.raise_()
        self.pushButton_stop.raise_()
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 770, 210, 40))
        self.widget.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(239,239,239, 255), stop:1 rgba(248,248,248, 255));\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(-10, 4, 111, 31))
        self.pushButton_4.setStyleSheet("*{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    font: 9pt \"宋体\";\n"
"    background:transparent;\n"
"}\n"
"*:hover\n"
"{\n"
"    color: rgb(42,166,244);\n"
"}")
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(104, 5, 103, 31))
        self.pushButton_5.setStyleSheet("*{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    font: 9pt \"宋体\";\n"
"    background:transparent;\n"
"}\n"
"*:hover\n"
"{\n"
"    color: rgb(42,166,244);\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/test/_增加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setObjectName("pushButton_5")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(0, 1, 210, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(101, 3, 2, 37))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.widget_7.raise_()
        self.widget_6.raise_()
        self.widget.raise_()
        self.line_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_stop.clicked.connect(self.pushButton_start.show)
        self.pushButton_stop.clicked.connect(self.pushButton_stop.hide)
        self.pushButton_start.clicked.connect(self.pushButton_stop.show)
        self.pushButton_start.clicked.connect(self.pushButton_start.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "搜索：设备名"))
        self.comboBox.setItemText(0, _translate("MainWindow", "我的设备"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "默认分组"))
        self.comboBox_myVideo.setItemText(0, _translate("MainWindow", "我的录像"))
        self.label_4.setText(_translate("MainWindow", "垃圾存放点智能管理平台"))
        self.pushButton_logout.setText(_translate("MainWindow", "退出"))
        self.username.setText(_translate("MainWindow", "用户名"))
        self.label_7.setText(_translate("MainWindow", " 垃圾存放点信息输出"))
        self.label_2.setText(_translate("MainWindow", " 行人行为信息输出"))
        self.pushButton_6.setText(_translate("MainWindow", "云存储"))
        self.pushButton_feedBack.setText(_translate("MainWindow", "意见留言"))
        self.label_6.setText(_translate("MainWindow", "主屏幕"))
        self.pushButton_img.setText(_translate("MainWindow", "图片检测"))
        self.pushButton_video.setText(_translate("MainWindow", "视频检测"))
        self.pushButton_camer.setText(_translate("MainWindow", "摄像头检测"))
        self.pushButton_finish.setText(_translate("MainWindow", "结束"))
        self.toolButton_11.setText(_translate("MainWindow", "..."))
        self.pushButton_29.setText(_translate("MainWindow", "开启轮巡"))
        self.toolButton_12.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "设备管理"))
        self.pushButton_5.setText(_translate("MainWindow", "添加"))

