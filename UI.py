# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys, json, os, subprocess,re
import configparser
from datetime import datetime 

class Ui_dialog(object):

    

    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(1021, 769)
        self.tabWidget = QTabWidget(dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1024, 768))
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(230, 160, 51, 31))
        self.spinBox_2 = QSpinBox(self.tab)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(300, 160, 51, 31))
        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(230, 240, 71, 31))
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, 200, 111, 41))
        self.label_50 = QLabel(self.tab)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(90, 160, 141, 41))
        self.label_51 = QLabel(self.tab)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(90, 240, 111, 41))
        self.doubleSpinBox = QDoubleSpinBox(self.tab)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(230, 200, 71, 31))
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 120, 111, 31))
        self.label_52 = QLabel(self.tab)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(230, 130, 341, 21))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_52.setFont(font1)
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(580, 70, 351, 271))
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(580, 390, 351, 271))
        self.label_53 = QLabel(self.tab)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(590, 360, 91, 16))
        self.label_54 = QLabel(self.tab)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(590, 40, 91, 16))
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(100, 390, 211, 131))
        font2 = QFont()
        font2.setPointSize(28)
        self.pushButton_4.setFont(font2)
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(90, 280, 111, 31))
        self.label_55 = QLabel(self.tab)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(230, 290, 341, 21))
        self.label_55.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.groupBox_4 = QGroupBox(self.tab_1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 10, 271, 341))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 101, 16))
        font3 = QFont()
        font3.setPointSize(10)
        self.label.setFont(font3)
        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 30, 113, 21))
        self.lineEdit_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 60, 113, 21))
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 101, 16))
        self.label_2.setFont(font3)
        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(150, 90, 113, 21))
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 121, 16))
        self.label_3.setFont(font3)
        self.lineEdit_4 = QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(150, 120, 113, 21))
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 111, 16))
        self.label_4.setFont(font3)
        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(150, 150, 113, 21))
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 150, 121, 16))
        self.label_6.setFont(font3)
        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(150, 180, 113, 21))
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 180, 121, 16))
        self.label_7.setFont(font3)
        self.lineEdit_8 = QLineEdit(self.groupBox_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(150, 210, 113, 21))
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 210, 121, 16))
        self.label_8.setFont(font3)
        self.lineEdit_9 = QLineEdit(self.groupBox_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(150, 240, 113, 21))
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 240, 121, 16))
        self.label_9.setFont(font3)
        self.lineEdit_13 = QLineEdit(self.groupBox_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(150, 270, 113, 21))
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 270, 101, 16))
        self.label_13.setFont(font3)
        self.lineEdit_5 = QLineEdit(self.groupBox_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(150, 300, 113, 21))
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 300, 151, 16))
        self.label_5.setFont(font3)
        self.groupBox_2 = QGroupBox(self.tab_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(320, 370, 271, 161))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.lineEdit_16 = QLineEdit(self.groupBox_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(150, 30, 113, 21))
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 30, 121, 16))
        self.label_16.setFont(font3)
        self.lineEdit_17 = QLineEdit(self.groupBox_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(150, 60, 113, 21))
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 60, 121, 16))
        self.label_17.setFont(font3)
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 90, 121, 16))
        self.label_18.setFont(font3)
        self.lineEdit_18 = QLineEdit(self.groupBox_2)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(150, 90, 113, 21))
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 120, 121, 16))
        self.label_19.setFont(font3)
        self.lineEdit_19 = QLineEdit(self.groupBox_2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(150, 120, 113, 21))
        self.groupBox = QGroupBox(self.tab_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(320, 10, 271, 281))
        self.groupBox.setFont(font)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        # self.lineEdit_10 = QLineEdit(self.groupBox)
        # self.lineEdit_10.setObjectName(u"lineEdit_10")
        # self.lineEdit_10.setGeometry(QRect(150, 90, 113, 21))
        # self.label_10 = QLabel(self.groupBox)
        # self.label_10.setObjectName(u"label_10")
        # self.label_10.setGeometry(QRect(10, 90, 161, 16))
        # self.label_10.setFont(font3)
        # self.lineEdit_12 = QLineEdit(self.groupBox)
        # self.lineEdit_12.setObjectName(u"lineEdit_12")
        # self.lineEdit_12.setGeometry(QRect(150, 120, 113, 21))
        # self.label_12 = QLabel(self.groupBox)
        # self.label_12.setObjectName(u"label_12")
        # self.label_12.setGeometry(QRect(10, 120, 161, 16))
        # self.label_12.setFont(font3)
        self.lineEdit_14 = QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(150, 30, 113, 21))
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 30, 161, 16))
        self.label_14.setFont(font3)
        self.lineEdit_15 = QLineEdit(self.groupBox)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(150, 60, 113, 21))
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 60, 161, 16))
        self.label_15.setFont(font3)
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 90, 161, 16))
        self.label_20.setFont(font3)
        self.lineEdit_20 = QLineEdit(self.groupBox)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(150, 90, 113, 21))
        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 120, 161, 16))
        self.label_21.setFont(font3)
        self.lineEdit_21 = QLineEdit(self.groupBox)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(150, 120, 113, 21))
        self.lineEdit_24 = QLineEdit(self.groupBox)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(150, 150, 113, 21))
        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 150, 161, 16))
        self.label_24.setFont(font3)
        self.lineEdit_25 = QLineEdit(self.groupBox)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(QRect(150, 180, 113, 21))
        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 180, 161, 16))
        self.label_25.setFont(font3)
        self.lineEdit_26 = QLineEdit(self.groupBox)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(150, 210, 113, 21))
        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 210, 161, 16))
        self.label_26.setFont(font3)
        self.lineEdit_27 = QLineEdit(self.groupBox)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(150, 240, 113, 21))
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 240, 161, 16))
        self.label_27.setFont(font3)
        self.pushButton = QPushButton(self.tab_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(630, 660, 75, 24))
        self.pushButton_2 = QPushButton(self.tab_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(800, 660, 75, 24))
        self.groupBox_3 = QGroupBox(self.tab_1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(620, 370, 271, 251))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.label_35 = QLabel(self.groupBox_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 30, 121, 16))
        self.label_35.setFont(font3)
        self.lineEdit_35 = QLineEdit(self.groupBox_3)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setGeometry(QRect(150, 30, 113, 21))
        self.lineEdit_36 = QLineEdit(self.groupBox_3)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setGeometry(QRect(150, 60, 113, 21))
        self.label_36 = QLabel(self.groupBox_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 60, 121, 16))
        self.label_36.setFont(font3)
        self.lineEdit_37 = QLineEdit(self.groupBox_3)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setGeometry(QRect(150, 90, 113, 21))
        self.label_37 = QLabel(self.groupBox_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 90, 121, 16))
        self.label_37.setFont(font3)
        self.lineEdit_38 = QLineEdit(self.groupBox_3)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setGeometry(QRect(150, 120, 113, 21))
        self.label_38 = QLabel(self.groupBox_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 120, 121, 16))
        self.label_38.setFont(font3)
        self.lineEdit_39 = QLineEdit(self.groupBox_3)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setGeometry(QRect(150, 150, 113, 21))
        self.label_39 = QLabel(self.groupBox_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 150, 121, 16))
        self.label_39.setFont(font3)
        self.lineEdit_40 = QLineEdit(self.groupBox_3)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setGeometry(QRect(150, 180, 113, 21))
        self.label_40 = QLabel(self.groupBox_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 180, 121, 16))
        self.label_40.setFont(font3)
        self.lineEdit_41 = QLineEdit(self.groupBox_3)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setGeometry(QRect(150, 210, 113, 21))
        self.label_41 = QLabel(self.groupBox_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 210, 121, 16))
        self.label_41.setFont(font3)
        self.groupBox_6 = QGroupBox(self.tab_1)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 370, 271, 361))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setChecked(False)
        self.lineEdit_22 = QLineEdit(self.groupBox_6)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(150, 30, 113, 21))
        self.label_22 = QLabel(self.groupBox_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 30, 101, 16))
        self.label_22.setFont(font3)
        self.lineEdit_23 = QLineEdit(self.groupBox_6)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(150, 60, 113, 21))
        self.label_23 = QLabel(self.groupBox_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 60, 101, 16))
        self.label_23.setFont(font3)
        self.lineEdit_42 = QLineEdit(self.groupBox_6)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setGeometry(QRect(150, 120, 51, 21))
        self.label_42 = QLabel(self.groupBox_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 120, 151, 16))
        self.label_42.setFont(font3)
        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 150, 141, 16))
        self.label_43.setFont(font3)
        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 180, 141, 16))
        self.label_44.setFont(font3)
        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 210, 141, 16))
        self.label_45.setFont(font3)
        self.label_46 = QLabel(self.groupBox_6)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 240, 141, 16))
        self.label_46.setFont(font3)
        self.lineEdit_47 = QLineEdit(self.groupBox_6)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setGeometry(QRect(210, 120, 51, 21))
        self.lineEdit_48 = QLineEdit(self.groupBox_6)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setGeometry(QRect(210, 150, 51, 21))
        self.lineEdit_43 = QLineEdit(self.groupBox_6)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setGeometry(QRect(150, 150, 51, 21))
        self.lineEdit_44 = QLineEdit(self.groupBox_6)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setGeometry(QRect(150, 180, 51, 21))
        self.lineEdit_49 = QLineEdit(self.groupBox_6)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setGeometry(QRect(210, 180, 51, 21))
        self.lineEdit_45 = QLineEdit(self.groupBox_6)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setGeometry(QRect(150, 210, 51, 21))
        self.lineEdit_50 = QLineEdit(self.groupBox_6)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setGeometry(QRect(210, 210, 51, 21))
        self.lineEdit_46 = QLineEdit(self.groupBox_6)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setGeometry(QRect(150, 240, 51, 21))
        self.lineEdit_51 = QLineEdit(self.groupBox_6)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setGeometry(QRect(210, 240, 51, 21))
        self.lineEdit_52 = QLineEdit(self.groupBox_6)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setGeometry(QRect(150, 270, 51, 21))
        self.lineEdit_53 = QLineEdit(self.groupBox_6)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setGeometry(QRect(210, 270, 51, 21))
        self.lineEdit_54 = QLineEdit(self.groupBox_6)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setGeometry(QRect(150, 300, 51, 21))
        self.lineEdit_55 = QLineEdit(self.groupBox_6)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setGeometry(QRect(210, 300, 51, 21))
        self.lineEdit_56 = QLineEdit(self.groupBox_6)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setGeometry(QRect(210, 330, 51, 21))
        self.lineEdit_57 = QLineEdit(self.groupBox_6)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setGeometry(QRect(150, 330, 51, 21))
        self.label_47 = QLabel(self.groupBox_6)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 300, 141, 16))
        self.label_47.setFont(font3)
        self.label_48 = QLabel(self.groupBox_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 270, 141, 16))
        self.label_48.setFont(font3)
        self.label_49 = QLabel(self.groupBox_6)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 330, 141, 16))
        self.label_49.setFont(font3)
        self.lineEdit_76 = QLineEdit(self.groupBox_6)
        self.lineEdit_76.setObjectName(u"lineEdit_76")
        self.lineEdit_76.setGeometry(QRect(150, 90, 113, 21))
        self.label_67 = QLabel(self.groupBox_6)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(10, 90, 101, 16))
        self.label_67.setFont(font3)
        self.groupBox_7 = QGroupBox(self.tab_1)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(620, 10, 271, 251))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.lineEdit_28 = QLineEdit(self.groupBox_7)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(150, 30, 113, 21))
        self.label_28 = QLabel(self.groupBox_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 30, 121, 16))
        self.label_28.setFont(font3)
        self.label_29 = QLabel(self.groupBox_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 60, 121, 16))
        self.label_29.setFont(font3)
        self.lineEdit_29 = QLineEdit(self.groupBox_7)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(150, 60, 113, 21))
        self.label_30 = QLabel(self.groupBox_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 90, 121, 16))
        self.label_30.setFont(font3)
        self.lineEdit_30 = QLineEdit(self.groupBox_7)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(150, 90, 113, 21))
        self.label_31 = QLabel(self.groupBox_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 120, 121, 16))
        self.label_31.setFont(font3)
        self.lineEdit_31 = QLineEdit(self.groupBox_7)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setGeometry(QRect(150, 120, 113, 21))
        self.label_32 = QLabel(self.groupBox_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 150, 121, 16))
        self.label_32.setFont(font3)
        self.lineEdit_32 = QLineEdit(self.groupBox_7)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setGeometry(QRect(150, 150, 113, 21))
        self.lineEdit_33 = QLineEdit(self.groupBox_7)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setGeometry(QRect(150, 180, 113, 21))
        self.label_33 = QLabel(self.groupBox_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 180, 121, 16))
        self.label_33.setFont(font3)
        self.lineEdit_34 = QLineEdit(self.groupBox_7)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setGeometry(QRect(150, 210, 113, 21))
        self.label_34 = QLabel(self.groupBox_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 210, 121, 16))
        self.label_34.setFont(font3)
        self.label_57 = QLabel(self.tab_1)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(320, 620, 571, 31))
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 240, 881, 451))
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 10, 221, 211))
        self.pushButton_6 = QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(140, 180, 75, 24))
        self.radioButton = QRadioButton(self.groupBox_5)
        self.buttonGroup = QButtonGroup(dialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 30, 171, 20))
        self.radioButton.setFont(font3)
        self.radioButton_2 = QRadioButton(self.groupBox_5)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 60, 191, 20))
        self.radioButton_2.setFont(font3)
        self.radioButton_3 = QRadioButton(self.groupBox_5)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(20, 120, 231, 20))
        self.radioButton_3.setFont(font3)
        self.radioButton_7 = QRadioButton(self.groupBox_5)
        self.buttonGroup.addButton(self.radioButton_7)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(20, 90, 191, 20))
        self.radioButton_7.setFont(font3)
        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(270, 10, 221, 211))
        self.pushButton_7 = QPushButton(self.groupBox_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(140, 180, 75, 24))
        self.radioButton_4 = QRadioButton(self.groupBox_8)
        self.buttonGroup_2 = QButtonGroup(dialog)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(10, 30, 191, 20))
        self.radioButton_4.setFont(font3)
        self.radioButton_5 = QRadioButton(self.groupBox_8)
        self.buttonGroup_2.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 90, 231, 20))
        self.radioButton_5.setFont(font3)
        self.radioButton_6 = QRadioButton(self.groupBox_8)
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 60, 191, 20))
        self.radioButton_6.setFont(font3)
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(520, 20, 75, 24))
        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(520, 60, 75, 24))
        self.pushButton_10 = QPushButton(self.tab_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(820, 190, 75, 24))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.retranslateUi(dialog)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi
        self.FileDialog = QFileDialog()
        self.pushButton_3.clicked.connect(self.FindPath3)
        self.pushButton_5.clicked.connect(self.FindPath5)
        self.pushButton_4.clicked.connect(self.CalibrateCamera)
        self.pushButton_2.clicked.connect(self.writeConfig)
        # self.pushButton_2.clicked.connect(self.CreateSettingJson)
        self.ProjectPath=''
        self.pushButton_6.clicked.connect(self.bgdetection)
        self.pushButton_7.clicked.connect(self.bgdetection)
        self.pushButton_8.clicked.connect(self.tracking)
        self.pushButton_9.clicked.connect(self.reconstruction)
        self.pushButton.clicked.connect(self.ResetAllValue)
    # setupUi
    def ResetAllValue(self):
        self.groupBox_4.setTitle(QCoreApplication.translate("dialog", u"视频信息", None))
        self.label.setText(QCoreApplication.translate("dialog", u"鱼的数量：", None))
        self.lineEdit.setText(QCoreApplication.translate("dialog", u"0", None))
        self.lineEdit_2.setText(QCoreApplication.translate("dialog", u"60", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"视频FPS：", None))
        self.lineEdit_3.setText(QCoreApplication.translate("dialog", u"169", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"俯视同步帧的帧号：", None))
        self.lineEdit_4.setText(QCoreApplication.translate("dialog", u"165", None))
        self.label_4.setText(QCoreApplication.translate("dialog", u"正视同步帧的帧号：", None))
        self.lineEdit_6.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label_6.setText(QCoreApplication.translate("dialog", u"俯视最小的帧号：", None))
        self.lineEdit_7.setText(QCoreApplication.translate("dialog", u"1800", None))
        self.label_7.setText(QCoreApplication.translate("dialog", u"俯视最大的帧号：", None))
        self.lineEdit_8.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label_8.setText(QCoreApplication.translate("dialog", u"正视最小的帧号：", None))
        self.lineEdit_9.setText(QCoreApplication.translate("dialog", u"1800", None))
        self.label_9.setText(QCoreApplication.translate("dialog", u"正视最大的帧号：", None))
        self.lineEdit_13.setText(QCoreApplication.translate("dialog", u"2", None))
        self.label_13.setText(QCoreApplication.translate("dialog", u"下采样率：", None))
        self.lineEdit_5.setText(QCoreApplication.translate("dialog", u"80", None))
        self.label_5.setText(QCoreApplication.translate("dialog", u"制作背景图抽取的帧数：", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("dialog", u"2D目标跟踪的参数：", None))
        self.lineEdit_16.setText(QCoreApplication.translate("dialog", u"15", None))
        self.label_16.setText(QCoreApplication.translate("dialog", u"俯视的鬼影阈值：", None))
        self.lineEdit_17.setText(QCoreApplication.translate("dialog", u"0.5", None))
        self.label_17.setText(QCoreApplication.translate("dialog", u"正视的鬼影阈值：", None))
        self.label_18.setText(QCoreApplication.translate("dialog", u"允许误匹配的掉帧数：", None))
        self.lineEdit_18.setText(QCoreApplication.translate("dialog", u"10", None))
        self.label_19.setText(QCoreApplication.translate("dialog", u"最小置信度：", None))
        self.lineEdit_19.setText(QCoreApplication.translate("dialog", u"0.95", None))
        self.groupBox.setTitle(QCoreApplication.translate("dialog", u"传统目标检测的参数：", None))
        # self.lineEdit_10.setText(QCoreApplication.translate("dialog", u"skeleton", None))
        # self.label_10.setText(QCoreApplication.translate("dialog", u"俯视用的传统检测方法：", None))
        # self.lineEdit_12.setText(QCoreApplication.translate("dialog", u"blob", None))
        # self.label_12.setText(QCoreApplication.translate("dialog", u"正视用的传统检测方法：", None))
        self.lineEdit_14.setText(QCoreApplication.translate("dialog", u"skeleton", None))
        self.label_14.setText(QCoreApplication.translate("dialog", u"俯视用的分割方法：", None))
        self.lineEdit_15.setText(QCoreApplication.translate("dialog", u"blob", None))
        self.label_15.setText(QCoreApplication.translate("dialog", u"正视用的分割方法：", None))
        self.label_20.setText(QCoreApplication.translate("dialog", u"中值滤波核的大小：", None))
        self.lineEdit_20.setText(QCoreApplication.translate("dialog", u"5", None))
        self.label_21.setText(QCoreApplication.translate("dialog", u"连通域的最小面积：", None))
        self.lineEdit_21.setText(QCoreApplication.translate("dialog", u"100", None))
        self.lineEdit_24.setText(QCoreApplication.translate("dialog", u"20", None))
        self.label_24.setText(QCoreApplication.translate("dialog", u"窗口内的最小面积", None))
        self.lineEdit_25.setText(QCoreApplication.translate("dialog", u"30", None))
        self.label_25.setText(QCoreApplication.translate("dialog", u"最佳关键点的最小长度：", None))
        self.lineEdit_26.setText(QCoreApplication.translate("dialog", u"10", None))
        self.label_26.setText(QCoreApplication.translate("dialog", u"窗口的半径：", None))
        self.lineEdit_27.setText(QCoreApplication.translate("dialog", u"0.25", None))
        self.label_27.setText(QCoreApplication.translate("dialog", u"非极大值抑制的阈值：", None))
        self.pushButton.setText(QCoreApplication.translate("dialog", u"恢复默认", None))
        self.pushButton_2.setText(QCoreApplication.translate("dialog", u"全部保存", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("dialog", u"3D目标跟踪的参数：", None))
        self.label_35.setText(QCoreApplication.translate("dialog", u"最大允许时间距离：", None))
        self.lineEdit_35.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.lineEdit_36.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.label_36.setText(QCoreApplication.translate("dialog", u"最大允许空间距离：", None))
        self.lineEdit_37.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.label_37.setText(QCoreApplication.translate("dialog", u"最大允许交叠的帧数：", None))
        self.lineEdit_38.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.label_38.setText(QCoreApplication.translate("dialog", u"最大允许交叠率：", None))
        self.lineEdit_39.setText(QCoreApplication.translate("dialog", u"0.20", None))
        self.label_39.setText(QCoreApplication.translate("dialog", u"最小主轨迹交叠倍数：", None))
        self.lineEdit_40.setText(QCoreApplication.translate("dialog", u"5", None))
        self.label_40.setText(QCoreApplication.translate("dialog", u"主轨迹搜寻倍数：", None))
        self.lineEdit_41.setText(QCoreApplication.translate("dialog", u"0.02", None))
        self.label_41.setText(QCoreApplication.translate("dialog", u"空白度量：", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("dialog", u"鱼缸的参数：", None))
        self.lineEdit_22.setText(QCoreApplication.translate("dialog", u"29", None))
        self.label_22.setText(QCoreApplication.translate("dialog", u"鱼缸的长：", None))
        self.lineEdit_23.setText(QCoreApplication.translate("dialog", u"29", None))
        self.label_23.setText(QCoreApplication.translate("dialog", u"鱼缸的宽：", None))
        self.lineEdit_42.setText(QCoreApplication.translate("dialog", u"668", None))
        self.label_42.setText(QCoreApplication.translate("dialog", u"俯视鱼缸左上角的坐标：", None))
        self.label_43.setText(QCoreApplication.translate("dialog", u"俯视鱼缸右上角的坐标：", None))
        self.label_44.setText(QCoreApplication.translate("dialog", u"俯视鱼缸右下角的坐标：", None))
        self.label_45.setText(QCoreApplication.translate("dialog", u"俯视鱼缸左下角的坐标：", None))
        self.label_46.setText(QCoreApplication.translate("dialog", u"正视鱼缸左上角的坐标：", None))
        self.lineEdit_47.setText(QCoreApplication.translate("dialog", u"84", None))
        self.lineEdit_48.setText(QCoreApplication.translate("dialog", u"83", None))
        self.lineEdit_43.setText(QCoreApplication.translate("dialog", u"1987", None))
        self.lineEdit_44.setText(QCoreApplication.translate("dialog", u"1973", None))
        self.lineEdit_49.setText(QCoreApplication.translate("dialog", u"1411", None))
        self.lineEdit_45.setText(QCoreApplication.translate("dialog", u"652", None))
        self.lineEdit_50.setText(QCoreApplication.translate("dialog", u"1393", None))
        self.lineEdit_46.setText(QCoreApplication.translate("dialog", u"246", None))
        self.lineEdit_51.setText(QCoreApplication.translate("dialog", u"400", None))
        self.lineEdit_52.setText(QCoreApplication.translate("dialog", u"2445", None))
        self.lineEdit_53.setText(QCoreApplication.translate("dialog", u"433", None))
        self.lineEdit_54.setText(QCoreApplication.translate("dialog", u"2275", None))
        self.lineEdit_55.setText(QCoreApplication.translate("dialog", u"1405", None))
        self.lineEdit_56.setText(QCoreApplication.translate("dialog", u"1376", None))
        self.lineEdit_57.setText(QCoreApplication.translate("dialog", u"392", None))
        self.label_47.setText(QCoreApplication.translate("dialog", u"正视鱼缸右下角的坐标：", None))
        self.label_48.setText(QCoreApplication.translate("dialog", u"正视鱼缸右上角的坐标：", None))
        self.label_49.setText(QCoreApplication.translate("dialog", u"正视鱼缸左下角的坐标：", None))
        self.lineEdit_76.setText(QCoreApplication.translate("dialog", u"15", None))
        self.label_67.setText(QCoreApplication.translate("dialog", u"水深：", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("dialog", u"3D重建的参数：", None))
        self.lineEdit_28.setText(QCoreApplication.translate("dialog", u"8.03", None))
        self.label_28.setText(QCoreApplication.translate("dialog", u"重投影误差的均值：", None))
        self.label_29.setText(QCoreApplication.translate("dialog", u"重投影误差的标准差：", None))
        self.lineEdit_29.setText(QCoreApplication.translate("dialog", u"5.26", None))
        self.label_30.setText(QCoreApplication.translate("dialog", u"移动误差的均值：", None))
        self.lineEdit_30.setText(QCoreApplication.translate("dialog", u"2.13", None))
        self.label_31.setText(QCoreApplication.translate("dialog", u"移动影误差的标准差：", None))
        self.lineEdit_31.setText(QCoreApplication.translate("dialog", u"2.32", None))
        self.label_32.setText(QCoreApplication.translate("dialog", u"同视角最大交叠：", None))
        self.lineEdit_32.setText(QCoreApplication.translate("dialog", u"0", None))
        self.lineEdit_33.setText(QCoreApplication.translate("dialog", u"10", None))
        self.label_33.setText(QCoreApplication.translate("dialog", u"轨迹的最小长度：", None))
        self.lineEdit_34.setText(QCoreApplication.translate("dialog", u"25", None))
        self.label_34.setText(QCoreApplication.translate("dialog", u"时间惩罚：", None))

    def CalibrateCamera(self):
        temp=[0,0,0,0,0,0]
        temp[0]=self.spinBox.text()
        temp[1]=self.spinBox_2.text()
        temp[2]=self.doubleSpinBox.text()
        temp[3]=self.comboBox.currentIndex()
        temp[4]=self.label_52.text()
        temp[5]=self.label_55.text()
        if ((temp[4][-1])!='\\' and (temp[4][-1])!="/"):
            temp[4]=self.label_52.text()+'/'
        if ((temp[5][-1])!='\\' and (temp[5][-1])!="/"):
            temp[5]=self.label_55.text()+'/'  
        if temp[3]==0:
            temp[3]=".jpg"
        else:
            temp[3]=".png" 
        print(temp[4])
        print(temp[0]+"  "+temp[1])
        print(temp[2])
        print(temp[3])
        print(temp[5])
        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\reconstruction\\CameraCalibration.py','-cs',temp[0],temp[1],'-ss',temp[2],'-if',temp[4],'-of',temp[5],'-it',temp[3]],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                print(Text.rstrip())
            else:
                break
        path=os.path.join(temp[5],"cam_intrinsic.json")        
        with open(path) as f:
            data = f.read()
        # Remove comments
        pattern = re.compile('/\*.*?\*/', re.DOTALL | re.MULTILINE)
        data = re.sub(pattern, ' ', data)
        # Parse json
        data = json.loads(data)
        # Load camera matrix K and distortion coefficients
        # data["K"]
        # data["Distortion"]
        self.textBrowser.setText(QCoreApplication.translate("dialog", str(data["Distortion"][0]), None))    
        self.textBrowser_2.setText(QCoreApplication.translate("dialog", str(data["K"][0]), None))   

    def FindPath3(self,label):
        Window = QMainWindow()
        path = self.FileDialog.getExistingDirectory(Window, "浏览路径")
        self.label_52.setText(QCoreApplication.translate("dialog", str(path), None))    

    def FindPath5(self,label):
        Window = QMainWindow()
        path = self.FileDialog.getExistingDirectory(Window, "浏览路径")
        self.ProjectPath=str(path)
        print(self.ProjectPath)
        self.label_55.setText(QCoreApplication.translate("dialog", str(path), None))  
        self.label_57.setText(QCoreApplication.translate("dialog", "项目路径为："+str(path), None))    

    def writeConfig(self):

        config = configparser.ConfigParser(allow_no_value=True)
        configFile = os.path.join(self.ProjectPath,'settings.ini')
        if(not os.path.isfile(configFile)):
            with open(configFile, 'w') as f:
                print("create setting.ini")
        config.read(configFile)

        config.set("DEFAULT", "n_fish",self.lineEdit.text())
        config.set("DEFAULT", "seed","1234567890" )
        config.set("DEFAULT", "fps",self.lineEdit_2.text() )
        config.set("DEFAULT", "cam2_head_detector", "false")
        
        config.add_section("BackgroundExtractor")
        config.set("BackgroundExtractor", "n_median",self.lineEdit_5.text())

        config.add_section("Detector")
        config.set("Detector", "cam1_type", self.lineEdit_14.text())
        config.set("Detector", "cam2_type", self.lineEdit_15.text())
        config.set("Detector", "cam1_maxframe", self.lineEdit_7.text())
        config.set("Detector", "cam2_maxframe", self.lineEdit_9.text())
        config.set("Detector", "cam1_minframe", self.lineEdit_6.text())
        config.set("Detector", "cam2_minframe", self.lineEdit_8.text())
        config.set("Detector", "downsample_factor", self.lineEdit_13.text())
        config.set("Detector", "blur_size", self.lineEdit_20.text())
        config.set("Detector", "min_blob_size", self.lineEdit_21.text())
        config.set("Detector", "min_patch_area", self.lineEdit_24.text())
        config.set("Detector", "min_skeleton_length", self.lineEdit_25.text())
        config.set("Detector", "window_size ", self.lineEdit_26.text())
        config.set("Detector", "nms_threshold", self.lineEdit_27.text())

        config.add_section("Tracker")
        config.set("Tracker", "cam1_ghost_threshold", self.lineEdit_16.text())
        config.set("Tracker", "cam2_ghost_threshold", self.lineEdit_17.text())
        config.set("Tracker", "max_kill_count", self.lineEdit_18.text())
        config.set("Tracker", "min_confidence", self.lineEdit_19.text())

        config.add_section("TrackletMatcher")
        config.set("TrackletMatcher", "reprojection_err_mean", self.lineEdit_28.text())
        config.set("TrackletMatcher", "reprojection_err_std", self.lineEdit_29.text())
        config.set("TrackletMatcher", "movement_err_mean", self.lineEdit_30.text())
        config.set("TrackletMatcher", "movement_err_std", self.lineEdit_31.text())
        config.set("TrackletMatcher", "same_view_max_overlap", self.lineEdit_32.text())
        config.set("TrackletMatcher", "tracklet_min_length", self.lineEdit_33.text())
        config.set("TrackletMatcher", "temporal_penalty", self.lineEdit_34.text())

        config.add_section("CameraSynchronization")
        config.set("CameraSynchronization", "cam1_sync_frame", self.lineEdit_3.text())
        config.set("CameraSynchronization", "cam2_sync_frame", self.lineEdit_4.text())

        config.add_section("Aquarium")
        config.set("Aquarium", "aquarium_width", self.lineEdit_22.text())
        config.set("Aquarium", "aquarium_depth", self.lineEdit_23.text())

        config.add_section("TrackletLinker")
        config.set("TrackletLinker", "max_frame_difference", self.lineEdit_35.text())
        config.set("TrackletLinker", "max_spatial_difference", self.lineEdit_36.text())
        config.set("TrackletLinker", "max_intersecting_frames", self.lineEdit_37.text())
        config.set("TrackletLinker", "max_intersection_ratio", self.lineEdit_38.text())
        config.set("TrackletLinker", "min_main_track_overlap_multiplier", self.lineEdit_39.text())
        config.set("TrackletLinker", "main_track_search_multiplier", self.lineEdit_40.text())
        config.set("TrackletLinker", "metric_margin", self.lineEdit_41.text())
            
        with open(configFile, 'w') as configfile:
            config.write(configfile)
            print("Updated configuration file: {}".format(configFile))


    def CreateSettingJson(self):
        result=[]
        result1=[]
        temp={}
        tempcamera={}
        tempworld={}

        temp1={}
        tempcamera1={}
        tempworld1={}

        temp2={}
        tempcamera2={}
        tempworld2={}

        temp3={}
        tempcamera3={}
        tempworld3={}

        temp4={}
        tempcamera4={}
        tempworld4={}

        temp5={}
        tempcamera5={}
        tempworld5={}

        temp6={}
        tempcamera6={}
        tempworld6={}

        temp7={}
        tempcamera7={}
        tempworld7={}

        tempcamera["x"]=int(self.lineEdit_42.text())+0.0
        tempcamera["y"]=int(self.lineEdit_47.text())+0.0
        tempworld["x"]=0.0
        tempworld["y"]=0.0
        tempworld["z"]=0.0
        temp["camera"]=tempcamera
        temp["world"]=tempworld
        result.append(temp)

        tempcamera1["x"]=int(self.lineEdit_43.text())+0.0
        tempcamera1["y"]=int(self.lineEdit_48.text())+0.0
        tempworld1["x"]=int(self.lineEdit_22.text())+0.0
        tempworld1["y"]=0.0
        tempworld1["z"]=0.0
        temp1["camera"]=tempcamera1
        temp1["world"]=tempworld1
        result.append(temp1)

        tempcamera2["x"]=int(self.lineEdit_44.text())+0.0
        tempcamera2["y"]=int(self.lineEdit_49.text())+0.0
        tempworld2["x"]=int(self.lineEdit_22.text())+0.0
        tempworld2["y"]=int(self.lineEdit_23.text())+0.0
        tempworld2["z"]=0.0
        temp2["camera"]=tempcamera2
        temp2["world"]=tempworld2
        result.append(temp2)

        tempcamera3["x"]=int(self.lineEdit_45.text())+0.0
        tempcamera3["y"]=int(self.lineEdit_50.text())+0.0
        tempworld3["x"]=0.0
        tempworld3["y"]=int(self.lineEdit_23.text())+0.0
        tempworld3["z"]=0.0
        temp3["camera"]=tempcamera3
        temp3["world"]=tempworld3
        result.append(temp3)
####################################################################
        tempcamera4["x"]=int(self.lineEdit_46.text())+0.0
        tempcamera4["y"]=int(self.lineEdit_51.text())+0.0
        tempworld4["x"]=0.0
        tempworld4["y"]=int(self.lineEdit_23.text())+0.0
        tempworld4["z"]=0.0
        temp4["camera"]=tempcamera4
        temp4["world"]=tempworld4
        result1.append(temp4)

        tempcamera5["x"]=int(self.lineEdit_52.text())+0.0
        tempcamera5["y"]=int(self.lineEdit_53.text())+0.0
        tempworld5["x"]=int(self.lineEdit_22.text())+0.0
        tempworld5["y"]=int(self.lineEdit_23.text())+0.0
        tempworld5["z"]=0.0
        temp5["camera"]=tempcamera5
        temp5["world"]=tempworld5
        result1.append(temp5)

        tempcamera6["x"]=int(self.lineEdit_54.text())+0.0
        tempcamera6["y"]=int(self.lineEdit_55.text())+0.0
        tempworld6["x"]=int(self.lineEdit_22.text())+0.0
        tempworld6["y"]=int(self.lineEdit_23.text())+0.0
        tempworld6["z"]=int(self.lineEdit_76.text())+0.0
        temp6["camera"]=tempcamera6
        temp6["world"]=tempworld6
        result1.append(temp6)

        tempcamera7["x"]=int(self.lineEdit_57.text())+0.0
        tempcamera7["y"]=int(self.lineEdit_56.text())+0.0
        tempworld7["x"]=0.0
        tempworld7["y"]=int(self.lineEdit_23.text())+0.0
        tempworld7["z"]=int(self.lineEdit_76.text())+0.0
        temp7["camera"]=tempcamera7
        temp7["world"]=tempworld7
        result1.append(temp7)

        outputName1 = os.path.join(self.ProjectPath, 'cam1_references.json')
        with open(outputName1, 'w') as f1:
            json.dump(result, f1,indent=4)
        print('Done! cam1_references.json')
        outputName2 = os.path.join(self.ProjectPath, 'cam2_references.json')
        with open(outputName2, 'w') as f2:
            json.dump(result1, f2,indent=4)  
        print('Done! cam2_references.json')

    def evalueImage(self,cam,head):
        
        if(int(cam)==1):
            if(head):
                weight ="D:\\bishe\\FasterRCNN\\top_head_faster_RCNN_resnet50_30epochs.tar"
            else:
                weight ="D:\\bishe\\FasterRCNN\\top_full_faster_RCNN_resnet50_30epochs.tar"
        else:
            if(head):
                weight ="D:\\bishe\\FasterRCNN\\front_head_faster_RCNN_resnet50_30epochs.tar"
            else:
                weight ="D:\\bishe\\FasterRCNN\\front_full_faster_RCNN_resnet50_30epochs.tar"            


        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\fasterrcnn\\evaluateImages.py','-f',self.ProjectPath,'-c',str(cam),'-w',weight],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != 'Done': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    

    def bgdetection(self):
        self.textEdit.insertPlainText("Starting Detecting\n")
        if(self.radioButton.isChecked()):
            print("传统方法检测")  
        if(self.radioButton_2.isChecked()):
            print("YOLOV3 Full")
        if(self.radioButton_7.isChecked()):    
            print("YOLOV4 Full")
        if(self.radioButton_3.isChecked()):
            print("FAST Full")
        if(self.radioButton_4.isChecked()):
            print("YOLOV3 Head")
        if(self.radioButton_6.isChecked()):
            print("YOLOV4 Head")
        if(self.radioButton_5.isChecked()):    
            print("FAST Head")
        _start = datetime.now() 
        print("开始检测俯拍视角")
        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\detection\\BgDetector.py','-f',self.ProjectPath,'-c','1','-i'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    
        _end = datetime.now() 
        timerup = (_end-_start).seconds
        print("俯拍检测用了"+str(timerup)+"秒")
        self.textEdit.insertPlainText("Cam1 Detection： "+str(timerup)+" second\n")

        print("开始检测侧拍视角")
        _start = datetime.now() 
        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\detection\\BgDetector.py','-f',self.ProjectPath,'-c','2','-i'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    
        _end = datetime.now() 
        timerup = (_end-_start).seconds
        print("侧拍检测用了"+str(timerup)+"秒")
        self.textEdit.insertPlainText("Cam2 Detection： "+str(timerup)+" second\n")



    def tracking(self):  
        # python TrackerVisual.py -f D:\bishe\3DZeF20\3DZeF20\train\ZebraFish-04 -c 2 -i -pd
        _start = datetime.now() 
        print("开始俯拍视角跟踪")
        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\tracking\\TrackerVisual.py','-f',self.ProjectPath,'-c','1','-i','-pd'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    
        _end = datetime.now() 
        timerup = (_end-_start).seconds
        print("俯拍跟踪用了"+str(timerup)+"秒")

        _start = datetime.now() 
        print("开始侧拍视角跟踪")
        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\tracking\\TrackerVisual.py','-f',self.ProjectPath,'-c','2','-i','-pd'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    
        _end = datetime.now() 
        timerup = (_end-_start).seconds
        print("侧拍跟踪用了"+str(timerup)+"秒")



    def reconstruction(self):

        print("开始三维重建")

        #python JsonToCamera.py -f D:\bishe\3DZeF20\3DZeF20\train\ZebraFish-03 -c 1

        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\reconstruction\\JsonToCamera.py','-f',self.ProjectPath,'-c','1'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    

        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\reconstruction\\JsonToCamera.py','-f',self.ProjectPath,'-c','2'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    
        #python TrackletMatching.py -f D:\bishe\3DZeF20\3DZeF20\train\ZebraFish-03

        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\reconstruction\\TrackletMatching.py','-f',self.ProjectPath],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    

        p = subprocess.Popen(['python','D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\modules\\reconstruction\\FinalizeTracks.py','-f',self.ProjectPath],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            response = p.stdout.readline()
            Text = response.decode()
            if Text != '': 
                self.textEdit.insertPlainText(str(Text)+'\n')
            else:
                break    

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"基于深度学习的斑马鱼目标检测跟踪系统", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("dialog", u".jpg", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("dialog", u".png", None))
        self.label_11.setText(QCoreApplication.translate("dialog", u"方块大小(厘米)：", None))
        self.label_50.setText(QCoreApplication.translate("dialog", u"角点长和宽的个数：", None))
        self.label_51.setText(QCoreApplication.translate("dialog", u"图片格式：", None))
        self.pushButton_3.setText(QCoreApplication.translate("dialog", u"浏览图片路径", None))
        self.label_52.setText(QCoreApplication.translate("dialog", u"请选择图片的路径", None))
        self.label_53.setText(QCoreApplication.translate("dialog", u"相机矩阵：", None))
        self.label_54.setText(QCoreApplication.translate("dialog", u"畸变系数：", None))
        self.pushButton_4.setText(QCoreApplication.translate("dialog", u"开始标定", None))
        self.pushButton_5.setText(QCoreApplication.translate("dialog", u"项目根目录", None))
        self.label_55.setText(QCoreApplication.translate("dialog", u"请选择项目根目录", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("dialog", u"相机标定", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("dialog", u"视频信息", None))
        self.label.setText(QCoreApplication.translate("dialog", u"鱼的数量：", None))
        self.lineEdit.setText(QCoreApplication.translate("dialog", u"0", None))
        self.lineEdit_2.setText(QCoreApplication.translate("dialog", u"60", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"视频FPS：", None))
        self.lineEdit_3.setText(QCoreApplication.translate("dialog", u"169", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"俯视同步帧的帧号：", None))
        self.lineEdit_4.setText(QCoreApplication.translate("dialog", u"165", None))
        self.label_4.setText(QCoreApplication.translate("dialog", u"正视同步帧的帧号：", None))
        self.lineEdit_6.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label_6.setText(QCoreApplication.translate("dialog", u"俯视最小的帧号：", None))
        self.lineEdit_7.setText(QCoreApplication.translate("dialog", u"1800", None))
        self.label_7.setText(QCoreApplication.translate("dialog", u"俯视最大的帧号：", None))
        self.lineEdit_8.setText(QCoreApplication.translate("dialog", u"1", None))
        self.label_8.setText(QCoreApplication.translate("dialog", u"正视最小的帧号：", None))
        self.lineEdit_9.setText(QCoreApplication.translate("dialog", u"1800", None))
        self.label_9.setText(QCoreApplication.translate("dialog", u"正视最大的帧号：", None))
        self.lineEdit_13.setText(QCoreApplication.translate("dialog", u"2", None))
        self.label_13.setText(QCoreApplication.translate("dialog", u"下采样率：", None))
        self.lineEdit_5.setText(QCoreApplication.translate("dialog", u"80", None))
        self.label_5.setText(QCoreApplication.translate("dialog", u"制作背景图抽取的帧数：", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("dialog", u"2D目标跟踪的参数：", None))
        self.lineEdit_16.setText(QCoreApplication.translate("dialog", u"15", None))
        self.label_16.setText(QCoreApplication.translate("dialog", u"俯视的鬼影阈值：", None))
        self.lineEdit_17.setText(QCoreApplication.translate("dialog", u"0.5", None))
        self.label_17.setText(QCoreApplication.translate("dialog", u"正视的鬼影阈值：", None))
        self.label_18.setText(QCoreApplication.translate("dialog", u"允许误匹配的掉帧数：", None))
        self.lineEdit_18.setText(QCoreApplication.translate("dialog", u"10", None))
        self.label_19.setText(QCoreApplication.translate("dialog", u"最小置信度：", None))
        self.lineEdit_19.setText(QCoreApplication.translate("dialog", u"0.95", None))
        self.groupBox.setTitle(QCoreApplication.translate("dialog", u"传统目标检测的参数：", None))
        # self.lineEdit_10.setText(QCoreApplication.translate("dialog", u"skeleton", None))
        # self.label_10.setText(QCoreApplication.translate("dialog", u"俯视用的传统检测方法：", None))
        # self.lineEdit_12.setText(QCoreApplication.translate("dialog", u"blob", None))
        # self.label_12.setText(QCoreApplication.translate("dialog", u"正视用的传统检测方法：", None))
        self.lineEdit_14.setText(QCoreApplication.translate("dialog", u"skeleton", None))
        self.label_14.setText(QCoreApplication.translate("dialog", u"俯视用的分割方法：", None))
        self.lineEdit_15.setText(QCoreApplication.translate("dialog", u"blob", None))
        self.label_15.setText(QCoreApplication.translate("dialog", u"正视用的分割方法：", None))
        self.label_20.setText(QCoreApplication.translate("dialog", u"中值滤波核的大小：", None))
        self.lineEdit_20.setText(QCoreApplication.translate("dialog", u"5", None))
        self.label_21.setText(QCoreApplication.translate("dialog", u"连通域的最小面积：", None))
        self.lineEdit_21.setText(QCoreApplication.translate("dialog", u"100", None))
        self.lineEdit_24.setText(QCoreApplication.translate("dialog", u"20", None))
        self.label_24.setText(QCoreApplication.translate("dialog", u"窗口内的最小面积", None))
        self.lineEdit_25.setText(QCoreApplication.translate("dialog", u"30", None))
        self.label_25.setText(QCoreApplication.translate("dialog", u"最佳关键点的最小长度：", None))
        self.lineEdit_26.setText(QCoreApplication.translate("dialog", u"10", None))
        self.label_26.setText(QCoreApplication.translate("dialog", u"窗口的半径：", None))
        self.lineEdit_27.setText(QCoreApplication.translate("dialog", u"0.25", None))
        self.label_27.setText(QCoreApplication.translate("dialog", u"非极大值抑制的阈值：", None))
        self.pushButton.setText(QCoreApplication.translate("dialog", u"恢复默认", None))
        self.pushButton_2.setText(QCoreApplication.translate("dialog", u"全部保存", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("dialog", u"3D目标跟踪的参数：", None))
        self.label_35.setText(QCoreApplication.translate("dialog", u"最大允许时间距离：", None))
        self.lineEdit_35.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.lineEdit_36.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.label_36.setText(QCoreApplication.translate("dialog", u"最大允许空间距离：", None))
        self.lineEdit_37.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.label_37.setText(QCoreApplication.translate("dialog", u"最大允许交叠的帧数：", None))
        self.lineEdit_38.setText(QCoreApplication.translate("dialog", u"-1", None))
        self.label_38.setText(QCoreApplication.translate("dialog", u"最大允许交叠率：", None))
        self.lineEdit_39.setText(QCoreApplication.translate("dialog", u"0.20", None))
        self.label_39.setText(QCoreApplication.translate("dialog", u"最小主轨迹交叠倍数：", None))
        self.lineEdit_40.setText(QCoreApplication.translate("dialog", u"5", None))
        self.label_40.setText(QCoreApplication.translate("dialog", u"主轨迹搜寻倍数：", None))
        self.lineEdit_41.setText(QCoreApplication.translate("dialog", u"0.02", None))
        self.label_41.setText(QCoreApplication.translate("dialog", u"空白度量：", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("dialog", u"鱼缸的参数：", None))
        self.lineEdit_22.setText(QCoreApplication.translate("dialog", u"29", None))
        self.label_22.setText(QCoreApplication.translate("dialog", u"鱼缸的长：", None))
        self.lineEdit_23.setText(QCoreApplication.translate("dialog", u"29", None))
        self.label_23.setText(QCoreApplication.translate("dialog", u"鱼缸的宽：", None))
        self.lineEdit_42.setText(QCoreApplication.translate("dialog", u"668", None))
        self.label_42.setText(QCoreApplication.translate("dialog", u"俯视鱼缸左上角的坐标：", None))
        self.label_43.setText(QCoreApplication.translate("dialog", u"俯视鱼缸右上角的坐标：", None))
        self.label_44.setText(QCoreApplication.translate("dialog", u"俯视鱼缸右下角的坐标：", None))
        self.label_45.setText(QCoreApplication.translate("dialog", u"俯视鱼缸左下角的坐标：", None))
        self.label_46.setText(QCoreApplication.translate("dialog", u"正视鱼缸左上角的坐标：", None))
        self.lineEdit_47.setText(QCoreApplication.translate("dialog", u"84", None))
        self.lineEdit_48.setText(QCoreApplication.translate("dialog", u"83", None))
        self.lineEdit_43.setText(QCoreApplication.translate("dialog", u"1987", None))
        self.lineEdit_44.setText(QCoreApplication.translate("dialog", u"1973", None))
        self.lineEdit_49.setText(QCoreApplication.translate("dialog", u"1411", None))
        self.lineEdit_45.setText(QCoreApplication.translate("dialog", u"652", None))
        self.lineEdit_50.setText(QCoreApplication.translate("dialog", u"1393", None))
        self.lineEdit_46.setText(QCoreApplication.translate("dialog", u"246", None))
        self.lineEdit_51.setText(QCoreApplication.translate("dialog", u"400", None))
        self.lineEdit_52.setText(QCoreApplication.translate("dialog", u"2445", None))
        self.lineEdit_53.setText(QCoreApplication.translate("dialog", u"433", None))
        self.lineEdit_54.setText(QCoreApplication.translate("dialog", u"2275", None))
        self.lineEdit_55.setText(QCoreApplication.translate("dialog", u"1405", None))
        self.lineEdit_56.setText(QCoreApplication.translate("dialog", u"1376", None))
        self.lineEdit_57.setText(QCoreApplication.translate("dialog", u"392", None))
        self.label_47.setText(QCoreApplication.translate("dialog", u"正视鱼缸右下角的坐标：", None))
        self.label_48.setText(QCoreApplication.translate("dialog", u"正视鱼缸右上角的坐标：", None))
        self.label_49.setText(QCoreApplication.translate("dialog", u"正视鱼缸左下角的坐标：", None))
        self.lineEdit_76.setText(QCoreApplication.translate("dialog", u"15", None))
        self.label_67.setText(QCoreApplication.translate("dialog", u"水深：", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("dialog", u"3D重建的参数：", None))
        self.lineEdit_28.setText(QCoreApplication.translate("dialog", u"8.03", None))
        self.label_28.setText(QCoreApplication.translate("dialog", u"重投影误差的均值：", None))
        self.label_29.setText(QCoreApplication.translate("dialog", u"重投影误差的标准差：", None))
        self.lineEdit_29.setText(QCoreApplication.translate("dialog", u"5.26", None))
        self.label_30.setText(QCoreApplication.translate("dialog", u"移动误差的均值：", None))
        self.lineEdit_30.setText(QCoreApplication.translate("dialog", u"2.13", None))
        self.label_31.setText(QCoreApplication.translate("dialog", u"移动影误差的标准差：", None))
        self.lineEdit_31.setText(QCoreApplication.translate("dialog", u"2.32", None))
        self.label_32.setText(QCoreApplication.translate("dialog", u"同视角最大交叠：", None))
        self.lineEdit_32.setText(QCoreApplication.translate("dialog", u"0", None))
        self.lineEdit_33.setText(QCoreApplication.translate("dialog", u"10", None))
        self.label_33.setText(QCoreApplication.translate("dialog", u"轨迹的最小长度：", None))
        self.lineEdit_34.setText(QCoreApplication.translate("dialog", u"25", None))
        self.label_34.setText(QCoreApplication.translate("dialog", u"时间惩罚：", None))
        self.label_57.setText(QCoreApplication.translate("dialog", u"保存设置参数的路径：", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("dialog", u"设置参数", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("dialog", u"基于鱼的全身的检测方法", None))
        self.pushButton_6.setText(QCoreApplication.translate("dialog", u"检测", None))
        self.radioButton.setText(QCoreApplication.translate("dialog", u"传统", None))
        self.radioButton_2.setText(QCoreApplication.translate("dialog", u"YOLOv3", None))
        self.radioButton_3.setText(QCoreApplication.translate("dialog", u"Faster R-CNN", None))
        self.radioButton_7.setText(QCoreApplication.translate("dialog", u"YOLOv4", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("dialog", u"基于鱼的头部的检测方法", None))
        self.pushButton_7.setText(QCoreApplication.translate("dialog", u"检测", None))
        self.radioButton_4.setText(QCoreApplication.translate("dialog", u"YOLOv3", None))
        self.radioButton_5.setText(QCoreApplication.translate("dialog", u"Faster R-CNN", None))
        self.radioButton_6.setText(QCoreApplication.translate("dialog", u"YOLOv4", None))
        self.pushButton_8.setText(QCoreApplication.translate("dialog", u"2D跟踪", None))
        self.pushButton_9.setText(QCoreApplication.translate("dialog", u"3D重建", None))
        self.pushButton_10.setText(QCoreApplication.translate("dialog", u"清空", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("dialog", u"执行过程", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("dialog", u"显示结果", None))
    # retranslateUi

if __name__ == "__main__":

    app = QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()