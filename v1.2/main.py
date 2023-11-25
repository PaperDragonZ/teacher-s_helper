# -*- coding: utf-8 -*-
# Created by: Paper_Dragon

import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QColor
import sys
import configparser as c
import os
import time
import main_rc
import random
import subprocess
cc = c.ConfigParser()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 645)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1001, 611))
        self.frame.setStyleSheet("background-color: rgb(208, 208, 208);\n"
"border-radius:30px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.menu = QtWidgets.QFrame(self.frame)
        self.menu.setGeometry(QtCore.QRect(0, 200, 211, 291))
        self.menu.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.pushButton_5 = QtWidgets.QPushButton(self.menu)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 0, 191, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"    background-color: rgb(208, 208, 208);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_5:hover{\n"
"    border:4px solid rgb(170, 170, 170);\n"
"    color: rgb(0,0,0);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/image/buttom/筛选_filter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.menu)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 60, 191, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"    background-color: rgb(208, 208, 208);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_6:hover{\n"
"    border:4px solid rgb(170, 170, 170);\n"
"    color: rgb(0,0,0);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/image/buttom/奖杯_trophy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.menu)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 120, 191, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"    background-color: rgb(208, 208, 208);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_7:hover{\n"
"    border:4px solid rgb(170, 170, 170);\n"
"    color: rgb(0,0,0);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/image/buttom/铅笔_pencil.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.menu)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
"    background-color: rgb(208, 208, 208);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_8:hover{\n"
"    border:4px solid rgb(170, 170, 170);\n"
"    color: rgb(0,0,0);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/button/image/buttom/设置_setting.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.menu)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("#pushButton_9{\n"
"    background-color: rgb(208, 208, 208);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_9:hover{\n"
"    border:4px solid rgb(170, 170, 170);\n"
"    color: rgb(0,0,0);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/image/buttom/计时器_timer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(450, 180, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.function_5 = QtWidgets.QFrame(self.frame)
        self.function_5.setGeometry(QtCore.QRect(210, 0, 791, 611))
        self.function_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px\n"
"")
        self.function_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_5.setObjectName("function_5")
        self.label_7 = QtWidgets.QLabel(self.function_5)
        self.label_7.setGeometry(QtCore.QRect(60, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(self.function_5)
        self.frame_3.setGeometry(QtCore.QRect(60, 100, 701, 151))
        self.frame_3.setStyleSheet("background-color: rgb(208, 208, 208);\n"
"border-radius:30px\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(280, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(20, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 40, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 40, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(170, 50, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("#pushButton_11{\n"
"    background-color: rgb(193, 193, 193);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_11:hover{\n"
"    border:4px solid rgb(184, 184, 184);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(620, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("#pushButton_12{\n"
"    background-color: rgb(193, 193, 193);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_12:hover{\n"
"    border:4px solid rgb(184, 184, 184);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(270, 50, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(520, 40, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(950, 20, 31, 31))
        self.pushButton_3.setStyleSheet("border-radius:15px\n"
"")
        self.pushButton_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/image/button_me/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 50, 101, 101))
        self.pushButton_4.setStyleSheet("border-radius:30px\n"
"")
        self.pushButton_4.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/image/image/button_me/image.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QtCore.QSize(128, 128))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 520, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("#pushButton_10{\n"
"    background-color: rgb(208, 208, 208);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_10:hover{\n"
"    border:4px solid rgb(170, 170, 170);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.function_4 = QtWidgets.QFrame(self.frame)
        self.function_4.setGeometry(QtCore.QRect(210, 0, 791, 611))
        self.function_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px\n"
"")
        self.function_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_4.setObjectName("function_4")
        self.label_6 = QtWidgets.QLabel(self.function_4)
        self.label_6.setGeometry(QtCore.QRect(120, 250, 581, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.function_3 = QtWidgets.QFrame(self.frame)
        self.function_3.setGeometry(QtCore.QRect(210, 0, 791, 611))
        self.function_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px\n"
"")
        self.function_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_3.setObjectName("function_3")
        self.label_9 = QtWidgets.QLabel(self.function_3)
        self.label_9.setGeometry(QtCore.QRect(120, 260, 581, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.function_2 = QtWidgets.QFrame(self.frame)
        self.function_2.setGeometry(QtCore.QRect(210, 0, 791, 611))
        self.function_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px\n"
"")
        self.function_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_2.setObjectName("function_2")
        self.label_10 = QtWidgets.QLabel(self.function_2)
        self.label_10.setGeometry(QtCore.QRect(120, 250, 581, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.function_1 = QtWidgets.QFrame(self.frame)
        self.function_1.setGeometry(QtCore.QRect(210, 0, 791, 611))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.function_1.setFont(font)
        self.function_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px\n"
"")
        self.function_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_1.setObjectName("function_1")
        self.label = QtWidgets.QLabel(self.function_1)
        self.label.setGeometry(QtCore.QRect(310, 40, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(47)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.function_1)
        self.frame_2.setGeometry(QtCore.QRect(60, 140, 691, 201))
        self.frame_2.setStyleSheet("background-color: rgb(216, 245, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(530, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(430, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(430, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 70, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    background-color: rgb(216, 245, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_2:hover{\n"
"    border:8px solid rgb(211, 239, 249);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(170, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(46)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(430, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 90, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.frame_4 = QtWidgets.QFrame(self.function_1)
        self.frame_4.setGeometry(QtCore.QRect(60, 360, 691, 201))
        self.frame_4.setStyleSheet("background-color: rgb(216, 245, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(530, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(390, 30, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_13.setGeometry(QtCore.QRect(440, 70, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("#pushButton_13{\n"
"    background-color: rgb(216, 245, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    border-radius:10px;\n"
"}\n"
"#pushButton_13:hover{\n"
"    border:8px solid rgb(211, 239, 249);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(500, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(40, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(200, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(270, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(350, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.menu.raise_()
        self.label_8.raise_()
        self.function_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_10.raise_()
        self.function_4.raise_()
        self.function_3.raise_()
        self.function_2.raise_()
        self.function_1.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.function_1.hide()
        self.function_2.hide()
        self.function_3.hide()
        self.function_4.hide()
        self.function_5.hide()

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(self.function_2.hide) # type: ignore
        self.pushButton_5.clicked.connect(self.function_1.show) # type: ignore
        self.pushButton_5.clicked.connect(self.function_3.hide) # type: ignore
        self.pushButton_5.clicked.connect(self.function_4.hide) # type: ignore
        self.pushButton_5.clicked.connect(self.function_5.hide) # type: ignore
        self.pushButton_6.clicked.connect(self.function_1.hide) # type: ignore
        self.pushButton_6.clicked.connect(self.function_2.show) # type: ignore
        self.pushButton_6.clicked.connect(self.function_3.hide) # type: ignore
        self.pushButton_6.clicked.connect(self.function_4.hide) # type: ignore
        self.pushButton_6.clicked.connect(self.function_5.hide) # type: ignore
        self.pushButton_7.clicked.connect(self.function_1.hide) # type: ignore
        self.pushButton_7.clicked.connect(self.function_2.hide) # type: ignore
        self.pushButton_7.clicked.connect(self.function_3.show) # type: ignore
        self.pushButton_7.clicked.connect(self.function_4.hide) # type: ignore
        self.pushButton_7.clicked.connect(self.function_5.hide) # type: ignore
        self.pushButton_9.clicked.connect(self.function_1.hide) # type: ignore
        self.pushButton_9.clicked.connect(self.function_2.hide) # type: ignore
        self.pushButton_9.clicked.connect(self.function_3.hide) # type: ignore
        self.pushButton_9.clicked.connect(self.function_4.show) # type: ignore
        self.pushButton_9.clicked.connect(self.function_5.hide) # type: ignore
        self.pushButton_8.clicked.connect(self.function_1.hide) # type: ignore
        self.pushButton_8.clicked.connect(self.function_2.hide) # type: ignore
        self.pushButton_8.clicked.connect(self.function_3.hide) # type: ignore
        self.pushButton_8.clicked.connect(self.function_4.hide) # type: ignore
        self.pushButton_8.clicked.connect(self.function_5.show) # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_4.clicked.connect(self.function_5.hide) # type: ignore
        self.pushButton_4.clicked.connect(self.function_1.hide) # type: ignore
        self.pushButton_4.clicked.connect(self.function_3.hide) # type: ignore
        self.pushButton_4.clicked.connect(self.function_2.hide) # type: ignore
        self.pushButton_4.clicked.connect(self.function_4.hide) # type: ignore
        self.pushButton_11.clicked.connect(lambda: self.pushButton_11_clicked())
        self.pushButton_2.clicked.connect(lambda: self.pushButton_2_clicked())
        self.pushButton_13.clicked.connect(lambda: self.pushButton_13_clicked())
        self.pushButton_10.clicked.connect(lambda: self.pushButton_10_clicked())
        self.pushButton_12.clicked.connect(lambda: self.pushButton_12_clicked())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pushButton_11_clicked (self):
        me.ini()
        me.ini_detect()
        global min1
        min1 = self.lineEdit_3.text()
        global max1
        max1 = self.lineEdit_4.text()
        global num1
        num1 = self.lineEdit_6.text()

        if min1 >= max1 or int(min1) >= 99 or int(max1) >= 99:
            QMessageBox.information(None, 
                                    "提示", 
                                    "请输入正确的区间！！！", 
                                    QMessageBox.Yes)
        elif num1 >= '6':
            QMessageBox.information(None, 
                                    "提示", 
                                    "一次抽取的人是不是有点多了~~~", 
                                    QMessageBox.Yes)
        else:
            cc.read(config,encoding="utf-8")  
            cc.set('extract','min',min1)
            cc.set('extract','max',max1)
            cc.set('extract','num',num1)
            with open(config, 'w') as f:
                cc.write(f)
            QMessageBox.information(None, 
                                        "提示", 
                                        "保存成功！！！", 
                                        QMessageBox.Yes)
            self.function_1.show()
            self.function_2.hide()
            self.function_3.hide()
            self.function_4.hide()
            self.function_5.hide()
            
            #更新抽学号界面数据
            cc.read(config,encoding="utf-8") 
            extract_min = cc.get("extract","min")
            extract_max = cc.get("extract","max")
            extract_num1 = cc.get("extract","num")
            self.lineEdit_2.setText(_translate("MainWindow", extract_min))
            self.lineEdit.setText(_translate("MainWindow", extract_max))
            self.lineEdit_8.setText(_translate("MainWindow", extract_num1))

    def pushButton_2_clicked (self):
        me.ini_detect()
        cc.read(config,encoding="utf-8") 
        extract_min = cc.get("extract","min")
        extract_max = cc.get("extract","max")
        extract = str(random.randint(int(extract_min),int(extract_max)))
        self.lineEdit_5.setText(_translate("MainWindow", extract))

    def pushButton_13_clicked (self):
        me.ini_detect()
        cc.read(config,encoding="utf-8") 
        extract_min = cc.get("extract","min")
        extract_max = cc.get("extract","max")
        extract_num1 = cc.get("extract","num")
        extract1 = str(random.randint(int(extract_min),int(extract_max)))
        extract2 = str(random.randint(int(extract_min),int(extract_max)))
        extract3 = str(random.randint(int(extract_min),int(extract_max)))
        extract4 = str(random.randint(int(extract_min),int(extract_max)))
        extract5 = str(random.randint(int(extract_min),int(extract_max)))

        self.lineEdit_9.setText(_translate("MainWindow", extract1))
        self.lineEdit_10.setText(_translate("MainWindow", extract2))
        self.lineEdit_11.setText(_translate("MainWindow", extract3))
        self.lineEdit_12.setText(_translate("MainWindow", extract4))
        self.lineEdit_13.setText(_translate("MainWindow", extract5))

        if extract_num1 == '1':
            self.lineEdit_9.show()
            self.lineEdit_10.hide()
            self.lineEdit_11.hide()
            self.lineEdit_12.hide()
            self.lineEdit_13.hide()
        elif extract_num1 == '2':
            self.lineEdit_9.show()
            self.lineEdit_10.show()
            self.lineEdit_11.hide()
            self.lineEdit_12.hide()
            self.lineEdit_13.hide()
        elif extract_num1 == '3':
            self.lineEdit_9.show()
            self.lineEdit_10.show()
            self.lineEdit_11.show()
            self.lineEdit_12.hide()
            self.lineEdit_13.hide()
        elif extract_num1 == '4':
            self.lineEdit_9.show()
            self.lineEdit_10.show()
            self.lineEdit_11.show()
            self.lineEdit_12.show()
            self.lineEdit_13.hide()
        elif extract_num1 == '5':
            self.lineEdit_9.show()
            self.lineEdit_10.show()
            self.lineEdit_11.show()
            self.lineEdit_12.show()
            self.lineEdit_13.show()
        
    def pushButton_10_clicked (self):
        me.ini()
        os.remove(config)
        me.create()
        cc.read(config,encoding="utf-8") 
        extract_min = cc.get("extract","min")
        extract_max = cc.get("extract","max")
        extract_num1 = cc.get("extract","num")
        self.lineEdit_2.setText(_translate("MainWindow", extract_min))
        self.lineEdit.setText(_translate("MainWindow", extract_max))
        self.lineEdit_8.setText(_translate("MainWindow", extract_num1))

    def pushButton_12_clicked (self):
        me.ini()
        QMessageBox.information(None, 
                                    "提示", 
                                    " 配置文件数值说明:\n 'min'和'max'的值不能大于99\n 'min'的值需要小于'max'的值\n 'num'的值不能大于5\n点击主界面左下角'不要点我'即可重置配置文件", 
                                    QMessageBox.Yes)
        
    def retranslateUi(self, MainWindow):
        me.ini()
        global _translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        cc.read(config,encoding="utf-8") 
        extract_num1 = cc.get("extract","num")
        extract_min = cc.get("extract","min")
        extract_max = cc.get("extract","max")
        self.lineEdit_2.setText(_translate("MainWindow", extract_min))
        self.lineEdit.setText(_translate("MainWindow", extract_max))
        self.lineEdit_8.setText(_translate("MainWindow", extract_num1))
        self.pushButton_5.setText(_translate("MainWindow", "抽学号"))
        self.pushButton_6.setText(_translate("MainWindow", "随机奖惩"))
        self.pushButton_7.setText(_translate("MainWindow", "画笔"))
        self.pushButton_8.setText(_translate("MainWindow", "设置"))
        self.pushButton_9.setText(_translate("MainWindow", "计时器"))
        self.label_8.setText(_translate("MainWindow", "欢迎使用本程序！！！"))
        self.label_7.setText(_translate("MainWindow", "设置"))
        self.label_12.setText(_translate("MainWindow", "抽学号配置"))
        self.label_13.setText(_translate("MainWindow", "抽取范围："))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", 'min'))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", 'max'))
        self.label_14.setText(_translate("MainWindow", "~"))
        self.pushButton_11.setText(_translate("MainWindow", "保存配置"))
        self.pushButton_12.setText(_translate("MainWindow", "关于"))
        self.label_16.setText(_translate("MainWindow", "抽取个数（仅连抽模式）："))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "num"))
        self.pushButton_10.setText(_translate("MainWindow", "不要点我！"))
        self.label_6.setText(_translate("MainWindow", "正在制作中……敬请期待！！！"))
        self.label_9.setText(_translate("MainWindow", "正在制作中……敬请期待！！！"))
        self.label_10.setText(_translate("MainWindow", "正在制作中……敬请期待！！！"))
        self.label.setText(_translate("MainWindow", "抽学号"))
        self.label_2.setText(_translate("MainWindow", "随机抽取"))
        self.label_3.setText(_translate("MainWindow", "最小号："))
        self.label_4.setText(_translate("MainWindow", "最大号："))
        self.pushButton_2.setText(_translate("MainWindow", "抽取"))
        self.label_11.setText(_translate("MainWindow", "号"))
        self.label_15.setText(_translate("MainWindow", "修改请转到设置"))
        self.label_5.setText(_translate("MainWindow", "连抽模式"))
        self.label_17.setText(_translate("MainWindow", "连续抽取数："))
        self.pushButton_13.setText(_translate("MainWindow", "抽取"))
        self.label_20.setText(_translate("MainWindow", "修改请转到设置"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "?"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "?"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "?"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "?"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "?"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", '?'))
        
class me ():
    def ini ():
        global myfile
        myfile = os.path.dirname(os.path.realpath(sys.argv[0]))
        global config
        config = os.path.join(myfile,'config.ini')
        
        if os.path.exists(config) == True:
            #print("存在")
            pass
        else:
            #print("不存在")
            me.create()
            pass
    
    def ini_detect ():
        cc.read(config,encoding="utf-8") 
        extract_min_detect = int(cc.get("extract","min"))
        extract_max_detect = int(cc.get("extract","max"))
        extract_num_detect = int(cc.get("extract","num"))
        if extract_min_detect >= extract_max_detect:
            QMessageBox.information(None, 
                                    "提示", 
                                    "不要乱改配置文件中的抽取范围啊!(主界面左下角点击即可重置配置文件)", 
                                    QMessageBox.Yes)
        elif extract_min_detect >= 99:
            QMessageBox.information(None, 
                                    "提示", 
                                    "配置文件中的抽取最小值不能超过100!(主界面左下角点击即可重置配置文件)", 
                                    QMessageBox.Yes)
        elif extract_max_detect >= 99:
            QMessageBox.information(None, 
                                    "提示", 
                                    "配置文件中的抽取最大值不能超过100!(主界面左下角点击即可重置配置文件)", 
                                    QMessageBox.Yes)
        elif extract_num_detect >= 6:
            QMessageBox.information(None, 
                                    "提示", 
                                    "不要乱改配置文件中连抽的数量啊!(主界面左下角点击即可重置配置文件)", 
                                    QMessageBox.Yes)
        else:
            pass
    def create ():
        with open(config, 'w') as f:
            f.write('[extract]\n')
            f.write('min=1\n')
            f.write('max=45\n')
            f.write('num=5\n')

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#窗口分辨率自动配置
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    me.ini()
    MainWindow.show()
    sys.exit(app.exec_())