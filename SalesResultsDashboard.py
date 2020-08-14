# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SalesResultsDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
import sqlite3
import os

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("Databases\\sales.db")
db.open()


class Ui_SalesResultsVis(object):
    def setupUi(self, SalesResultsVis, month):
        SalesResultsVis.setObjectName("SalesResultsVis")
        SalesResultsVis.resize(1876, 955)
        SalesResultsVis.setStyleSheet("background-color: rgba(0, 35, 72, 255);")
        self.centralwidget = QtWidgets.QWidget(SalesResultsVis)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ytd_frame = QtWidgets.QFrame(self.tab_2)
        self.ytd_frame.setGeometry(QtCore.QRect(0, 0, 1861, 905))
        self.ytd_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.ytd_frame.setObjectName("ytd_frame")
        self.ytd_le_frame2 = QtWidgets.QFrame(self.ytd_frame)
        self.ytd_le_frame2.setGeometry(QtCore.QRect(610, 600, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.ytd_le_frame2.setFont(font)
        self.ytd_le_frame2.setStyleSheet("color: rgb(255, 255, 255);")
        self.ytd_le_frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ytd_le_frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ytd_le_frame2.setLineWidth(10)
        self.ytd_le_frame2.setMidLineWidth(10)
        self.ytd_le_frame2.setObjectName("ytd_le_frame2")
        self.ytd_le_chart2 = QtWidgets.QGridLayout(self.ytd_le_frame2)
        self.ytd_le_chart2.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.ytd_le_chart2.setObjectName("ytd_le_chart2")
        self.ytd_le_frame1 = QtWidgets.QFrame(self.ytd_frame)
        self.ytd_le_frame1.setGeometry(QtCore.QRect(10, 600, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.ytd_le_frame1.setFont(font)
        self.ytd_le_frame1.setStyleSheet("color: rgb(255, 255, 255);")
        self.ytd_le_frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ytd_le_frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ytd_le_frame1.setLineWidth(10)
        self.ytd_le_frame1.setMidLineWidth(10)
        self.ytd_le_frame1.setObjectName("ytd_le_frame1")
        self.ytd_le_chart1 = QtWidgets.QGridLayout(self.ytd_le_frame1)
        self.ytd_le_chart1.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.ytd_le_chart1.setObjectName("ytd_le_chart1")
        self.ytd_b2b2_frame1 = QtWidgets.QFrame(self.ytd_frame)
        self.ytd_b2b2_frame1.setGeometry(QtCore.QRect(10, 320, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.ytd_b2b2_frame1.setFont(font)
        self.ytd_b2b2_frame1.setStyleSheet("color: rgb(255, 255, 255);")
        self.ytd_b2b2_frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ytd_b2b2_frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ytd_b2b2_frame1.setLineWidth(10)
        self.ytd_b2b2_frame1.setMidLineWidth(10)
        self.ytd_b2b2_frame1.setObjectName("ytd_b2b2_frame1")
        self.ytd_b2b2_chart1 = QtWidgets.QGridLayout(self.ytd_b2b2_frame1)
        self.ytd_b2b2_chart1.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.ytd_b2b2_chart1.setObjectName("ytd_b2b2_chart1")
        self.ytd_b2b2_frame2 = QtWidgets.QFrame(self.ytd_frame)
        self.ytd_b2b2_frame2.setGeometry(QtCore.QRect(610, 320, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.ytd_b2b2_frame2.setFont(font)
        self.ytd_b2b2_frame2.setStyleSheet("color: rgb(255, 255, 255);")
        self.ytd_b2b2_frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ytd_b2b2_frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ytd_b2b2_frame2.setLineWidth(10)
        self.ytd_b2b2_frame2.setMidLineWidth(10)
        self.ytd_b2b2_frame2.setObjectName("ytd_b2b2_frame2")
        self.ytd_b2b2_chart2 = QtWidgets.QGridLayout(self.ytd_b2b2_frame2)
        self.ytd_b2b2_chart2.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.ytd_b2b2_chart2.setObjectName("ytd_b2b2_chart2")
        self.ytd_b2b1_frame2 = QtWidgets.QFrame(self.ytd_frame)
        self.ytd_b2b1_frame2.setGeometry(QtCore.QRect(610, 40, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.ytd_b2b1_frame2.setFont(font)
        self.ytd_b2b1_frame2.setStyleSheet("color: rgb(255, 255, 255);")
        self.ytd_b2b1_frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ytd_b2b1_frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ytd_b2b1_frame2.setLineWidth(10)
        self.ytd_b2b1_frame2.setMidLineWidth(10)
        self.ytd_b2b1_frame2.setObjectName("ytd_b2b1_frame2")
        self.ytd_b2b1_chart2 = QtWidgets.QGridLayout(self.ytd_b2b1_frame2)
        self.ytd_b2b1_chart2.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.ytd_b2b1_chart2.setObjectName("ytd_b2b1_chart2")
        self.ytd_b2b1_frame1 = QtWidgets.QFrame(self.ytd_frame)
        self.ytd_b2b1_frame1.setGeometry(QtCore.QRect(10, 40, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.ytd_b2b1_frame1.setFont(font)
        self.ytd_b2b1_frame1.setStyleSheet("color: rgb(255, 255, 255);")
        self.ytd_b2b1_frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ytd_b2b1_frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ytd_b2b1_frame1.setLineWidth(10)
        self.ytd_b2b1_frame1.setMidLineWidth(10)
        self.ytd_b2b1_frame1.setObjectName("ytd_b2b1_frame1")
        self.ytd_b2b1_chart1 = QtWidgets.QGridLayout(self.ytd_b2b1_frame1)
        self.ytd_b2b1_chart1.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.ytd_b2b1_chart1.setObjectName("ytd_b2b1_chart1")
        self.ytd_b2b1_table = QtWidgets.QTableView(self.ytd_frame)
        self.ytd_b2b1_table.setGeometry(QtCore.QRect(1230, 90, 591, 221))
        self.ytd_b2b1_table.setObjectName("ytd_b2b1_table")
        self.ytd_b2b2_table = QtWidgets.QTableView(self.ytd_frame)
        self.ytd_b2b2_table.setGeometry(QtCore.QRect(1230, 370, 591, 221))
        self.ytd_b2b2_table.setObjectName("ytd_b2b2_table")
        self.ytd_le_table = QtWidgets.QTableView(self.ytd_frame)
        self.ytd_le_table.setGeometry(QtCore.QRect(1230, 650, 591, 221))
        self.ytd_le_table.setObjectName("ytd_le_table")
        self.ytd_b2b_label1 = QtWidgets.QLabel(self.ytd_frame)
        self.ytd_b2b_label1.setGeometry(QtCore.QRect(1230, 40, 590, 51))
        self.ytd_b2b_label1.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_b2b_label1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_b2b_label1.setFont(font)
        self.ytd_b2b_label1.setObjectName("ytd_b2b_label1")
        self.ytd_b2b_label2 = QtWidgets.QLabel(self.ytd_frame)
        self.ytd_b2b_label2.setGeometry(QtCore.QRect(1230, 320, 590, 51))
        self.ytd_b2b_label2.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_b2b_label2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_b2b_label2.setFont(font)
        self.ytd_b2b_label2.setObjectName("ytd_b2b_label2")
        self.ytd_le_label = QtWidgets.QLabel(self.ytd_frame)
        self.ytd_le_label.setGeometry(QtCore.QRect(1230, 600, 590, 51))
        self.ytd_le_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_le_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_le_label.setFont(font)
        self.ytd_le_label.setObjectName("ytd_le_label")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.ytd_top_frame = QtWidgets.QFrame(self.tab_5)
        self.ytd_top_frame.setGeometry(QtCore.QRect(0, 0, 1861, 905))
        self.ytd_top_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.ytd_top_frame.setObjectName("ytd_top_frame")
        self.ytd_top_bu2_label = QtWidgets.QLabel(self.ytd_top_frame)
        self.ytd_top_bu2_label.setGeometry(QtCore.QRect(1260, 40, 590, 41))
        self.ytd_top_bu2_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_top_bu2_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_top_bu2_label.setFont(font)
        self.ytd_top_bu2_label.setObjectName("ytd_top_bu2_label")
        self.ytd_top_bu1_label = QtWidgets.QLabel(self.ytd_top_frame)
        self.ytd_top_bu1_label.setGeometry(QtCore.QRect(660, 40, 590, 41))
        self.ytd_top_bu1_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_top_bu1_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_top_bu1_label.setFont(font)
        self.ytd_top_bu1_label.setObjectName("ytd_top_bu1_label")
        self.ytd_top_label = QtWidgets.QLabel(self.ytd_top_frame)
        self.ytd_top_label.setGeometry(QtCore.QRect(20, 10, 590, 41))
        self.ytd_top_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_top_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_top_label.setFont(font)
        self.ytd_top_label.setObjectName("ytd_top_label")
        self.ytd_top_bu2_table = QtWidgets.QTableView(self.ytd_top_frame)
        self.ytd_top_bu2_table.setGeometry(QtCore.QRect(1260, 80, 591, 341))
        self.ytd_top_bu2_table.setObjectName("ytd_top_bu2_table")
        self.ytd_top_bu1_table = QtWidgets.QTableView(self.ytd_top_frame)
        self.ytd_top_bu1_table.setGeometry(QtCore.QRect(660, 80, 591, 341))
        self.ytd_top_bu1_table.setObjectName("ytd_top_bu1_table")
        self.ytd_top_table = QtWidgets.QTableView(self.ytd_top_frame)
        self.ytd_top_table.setGeometry(QtCore.QRect(20, 50, 591, 821))
        self.ytd_top_table.setObjectName("ytd_top_table")
        self.ytd_top_bu4_label = QtWidgets.QLabel(self.ytd_top_frame)
        self.ytd_top_bu4_label.setGeometry(QtCore.QRect(1260, 490, 590, 41))
        self.ytd_top_bu4_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_top_bu4_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_top_bu4_label.setFont(font)
        self.ytd_top_bu4_label.setObjectName("ytd_top_bu4_label")
        self.ytd_top_bu3_table = QtWidgets.QTableView(self.ytd_top_frame)
        self.ytd_top_bu3_table.setGeometry(QtCore.QRect(660, 530, 591, 341))
        self.ytd_top_bu3_table.setObjectName("ytd_top_bu3_table")
        self.ytd_top_bu3_label = QtWidgets.QLabel(self.ytd_top_frame)
        self.ytd_top_bu3_label.setGeometry(QtCore.QRect(660, 490, 590, 41))
        self.ytd_top_bu3_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_top_bu3_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.ytd_top_bu3_label.setFont(font)
        self.ytd_top_bu3_label.setObjectName("ytd_top_bu3_label")
        self.ytd_top_bu4_table = QtWidgets.QTableView(self.ytd_top_frame)
        self.ytd_top_bu4_table.setGeometry(QtCore.QRect(1260, 530, 591, 341))
        self.ytd_top_bu4_table.setObjectName("ytd_top_bu4_table")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.mtd_frame = QtWidgets.QFrame(self.tab_3)
        self.mtd_frame.setGeometry(QtCore.QRect(0, 0, 1861, 905))
        self.mtd_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.mtd_frame.setObjectName("mtd_frame")
        self.mtd_le_frame2 = QtWidgets.QFrame(self.mtd_frame)
        self.mtd_le_frame2.setGeometry(QtCore.QRect(610, 600, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.mtd_le_frame2.setFont(font)
        self.mtd_le_frame2.setStyleSheet("color: rgb(255, 255, 255);")
        self.mtd_le_frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mtd_le_frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mtd_le_frame2.setLineWidth(10)
        self.mtd_le_frame2.setMidLineWidth(10)
        self.mtd_le_frame2.setObjectName("mtd_le_frame2")
        self.mtd_le_chart2 = QtWidgets.QGridLayout(self.mtd_le_frame2)
        self.mtd_le_chart2.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.mtd_le_chart2.setObjectName("mtd_le_chart2")
        self.mtd_le_frame1 = QtWidgets.QFrame(self.mtd_frame)
        self.mtd_le_frame1.setGeometry(QtCore.QRect(10, 600, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.mtd_le_frame1.setFont(font)
        self.mtd_le_frame1.setStyleSheet("color: rgb(255, 255, 255);")
        self.mtd_le_frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mtd_le_frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mtd_le_frame1.setLineWidth(10)
        self.mtd_le_frame1.setMidLineWidth(10)
        self.mtd_le_frame1.setObjectName("mtd_le_frame1")
        self.mtd_le_chart1 = QtWidgets.QGridLayout(self.mtd_le_frame1)
        self.mtd_le_chart1.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.mtd_le_chart1.setObjectName("mtd_le_chart1")
        self.mtd_b2b2_frame1 = QtWidgets.QFrame(self.mtd_frame)
        self.mtd_b2b2_frame1.setGeometry(QtCore.QRect(10, 320, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.mtd_b2b2_frame1.setFont(font)
        self.mtd_b2b2_frame1.setStyleSheet("color: rgb(255, 255, 255);")
        self.mtd_b2b2_frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mtd_b2b2_frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mtd_b2b2_frame1.setLineWidth(10)
        self.mtd_b2b2_frame1.setMidLineWidth(10)
        self.mtd_b2b2_frame1.setObjectName("mtd_b2b2_frame1")
        self.mtd_b2b2_chart1 = QtWidgets.QGridLayout(self.mtd_b2b2_frame1)
        self.mtd_b2b2_chart1.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.mtd_b2b2_chart1.setObjectName("mtd_b2b2_chart1")
        self.mtd_b2b2_frame2 = QtWidgets.QFrame(self.mtd_frame)
        self.mtd_b2b2_frame2.setGeometry(QtCore.QRect(610, 320, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.mtd_b2b2_frame2.setFont(font)
        self.mtd_b2b2_frame2.setStyleSheet("color: rgb(255, 255, 255);")
        self.mtd_b2b2_frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mtd_b2b2_frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mtd_b2b2_frame2.setLineWidth(10)
        self.mtd_b2b2_frame2.setMidLineWidth(10)
        self.mtd_b2b2_frame2.setObjectName("mtd_b2b2_frame2")
        self.mtd_b2b2_chart2 = QtWidgets.QGridLayout(self.mtd_b2b2_frame2)
        self.mtd_b2b2_chart2.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.mtd_b2b2_chart2.setObjectName("mtd_b2b2_chart2")
        self.mtd_b2b1_frame2 = QtWidgets.QFrame(self.mtd_frame)
        self.mtd_b2b1_frame2.setGeometry(QtCore.QRect(610, 40, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.mtd_b2b1_frame2.setFont(font)
        self.mtd_b2b1_frame2.setStyleSheet("color: rgb(255, 255, 255);")
        self.mtd_b2b1_frame2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mtd_b2b1_frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mtd_b2b1_frame2.setLineWidth(10)
        self.mtd_b2b1_frame2.setMidLineWidth(10)
        self.mtd_b2b1_frame2.setObjectName("mtd_b2b1_frame2")
        self.mtd_b2b1_chart2 = QtWidgets.QGridLayout(self.mtd_b2b1_frame2)
        self.mtd_b2b1_chart2.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.mtd_b2b1_chart2.setObjectName("mtd_b2b1_chart2")
        self.mtd_b2b1_frame1 = QtWidgets.QFrame(self.mtd_frame)
        self.mtd_b2b1_frame1.setGeometry(QtCore.QRect(10, 40, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.mtd_b2b1_frame1.setFont(font)
        self.mtd_b2b1_frame1.setStyleSheet("color: rgb(255, 255, 255);")
        self.mtd_b2b1_frame1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mtd_b2b1_frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mtd_b2b1_frame1.setLineWidth(10)
        self.mtd_b2b1_frame1.setMidLineWidth(10)
        self.mtd_b2b1_frame1.setObjectName("mtd_b2b1_frame1")
        self.mtd_b2b1_chart1 = QtWidgets.QGridLayout(self.mtd_b2b1_frame1)
        self.mtd_b2b1_chart1.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.mtd_b2b1_chart1.setObjectName("mtd_b2b1_chart1")
        self.mtd_le_label = QtWidgets.QLabel(self.mtd_frame)
        self.mtd_le_label.setGeometry(QtCore.QRect(1230, 600, 590, 51))
        self.mtd_le_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_le_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_le_label.setFont(font)
        self.mtd_le_label.setObjectName("mtd_le_label")
        self.mtd_b2b_label2 = QtWidgets.QLabel(self.mtd_frame)
        self.mtd_b2b_label2.setGeometry(QtCore.QRect(1230, 320, 590, 51))
        self.mtd_b2b_label2.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_b2b_label2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_b2b_label2.setFont(font)
        self.mtd_b2b_label2.setObjectName("mtd_b2b_label2")
        self.mtd_b2b_label1 = QtWidgets.QLabel(self.mtd_frame)
        self.mtd_b2b_label1.setGeometry(QtCore.QRect(1230, 40, 590, 51))
        self.mtd_b2b_label1.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_b2b_label1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_b2b_label1.setFont(font)
        self.mtd_b2b_label1.setObjectName("mtd_b2b_label1")
        self.mtd_le_table = QtWidgets.QTableView(self.mtd_frame)
        self.mtd_le_table.setGeometry(QtCore.QRect(1230, 650, 591, 221))
        self.mtd_le_table.setObjectName("mtd_le_table")
        self.mtd_b2b_table2 = QtWidgets.QTableView(self.mtd_frame)
        self.mtd_b2b_table2.setGeometry(QtCore.QRect(1230, 370, 591, 221))
        self.mtd_b2b_table2.setObjectName("mtd_b2b_table2")
        self.mtd_b2b_table1 = QtWidgets.QTableView(self.mtd_frame)
        self.mtd_b2b_table1.setGeometry(QtCore.QRect(1230, 90, 591, 221))
        self.mtd_b2b_table1.setObjectName("mtd_b2b_table1")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.mtd_top_frame = QtWidgets.QFrame(self.tab_4)
        self.mtd_top_frame.setGeometry(QtCore.QRect(0, 0, 1861, 905))
        self.mtd_top_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.mtd_top_frame.setObjectName("mtd_top_frame")
        self.mtd_top_bu2_label = QtWidgets.QLabel(self.mtd_top_frame)
        self.mtd_top_bu2_label.setGeometry(QtCore.QRect(1260, 40, 590, 41))
        self.mtd_top_bu2_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_top_bu2_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_top_bu2_label.setFont(font)
        self.mtd_top_bu2_label.setObjectName("mtd_top_bu2_label")
        self.mtd_top_bu1_label = QtWidgets.QLabel(self.mtd_top_frame)
        self.mtd_top_bu1_label.setGeometry(QtCore.QRect(660, 40, 590, 41))
        self.mtd_top_bu1_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_top_bu1_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_top_bu1_label.setFont(font)
        self.mtd_top_bu1_label.setObjectName("mtd_top_bu1_label")
        self.mtd_top_label = QtWidgets.QLabel(self.mtd_top_frame)
        self.mtd_top_label.setGeometry(QtCore.QRect(20, 10, 590, 41))
        self.mtd_top_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_top_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_top_label.setFont(font)
        self.mtd_top_label.setObjectName("mtd_top_label")
        self.mtd_top_bu2_table = QtWidgets.QTableView(self.mtd_top_frame)
        self.mtd_top_bu2_table.setGeometry(QtCore.QRect(1260, 80, 591, 341))
        self.mtd_top_bu2_table.setObjectName("mtd_top_bu2_table")
        self.mtd_top_bu1_table = QtWidgets.QTableView(self.mtd_top_frame)
        self.mtd_top_bu1_table.setGeometry(QtCore.QRect(660, 80, 591, 341))
        self.mtd_top_bu1_table.setObjectName("mtd_top_bu1_table")
        self.mtd_top_table = QtWidgets.QTableView(self.mtd_top_frame)
        self.mtd_top_table.setGeometry(QtCore.QRect(20, 50, 591, 821))
        self.mtd_top_table.setObjectName("mtd_top_table")
        self.mtd_top_bu4_label = QtWidgets.QLabel(self.mtd_top_frame)
        self.mtd_top_bu4_label.setGeometry(QtCore.QRect(1260, 490, 590, 41))
        self.mtd_top_bu4_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_top_bu4_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_top_bu4_label.setFont(font)
        self.mtd_top_bu4_label.setObjectName("mtd_top_bu4_label")
        self.mtd_top_bu3_table = QtWidgets.QTableView(self.mtd_top_frame)
        self.mtd_top_bu3_table.setGeometry(QtCore.QRect(660, 530, 591, 341))
        self.mtd_top_bu3_table.setObjectName("mtd_top_bu3_table")
        self.mtd_top_bu3_label = QtWidgets.QLabel(self.mtd_top_frame)
        self.mtd_top_bu3_label.setGeometry(QtCore.QRect(660, 490, 590, 41))
        self.mtd_top_bu3_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_top_bu3_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.mtd_top_bu3_label.setFont(font)
        self.mtd_top_bu3_label.setObjectName("mtd_top_bu3_label")
        self.mtd_top_bu4_table = QtWidgets.QTableView(self.mtd_top_frame)
        self.mtd_top_bu4_table.setGeometry(QtCore.QRect(1260, 530, 591, 341))
        self.mtd_top_bu4_table.setObjectName("mtd_top_bu4_table")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        SalesResultsVis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SalesResultsVis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1876, 18))
        self.menubar.setObjectName("menubar")
        SalesResultsVis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SalesResultsVis)
        self.statusbar.setObjectName("statusbar")
        SalesResultsVis.setStatusBar(self.statusbar)

        self.retranslateUi(SalesResultsVis)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SalesResultsVis)

        # Filling the YTD and MTD tables
        self.fill_chart_tables("YTD 1",
                               "SELECT bu1, SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                               "GROUP BY bu1 "
                               "ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables("YTD 2",
                               "SELECT bu2, SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                               "GROUP BY bu2 "
                               "ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables("YTD 3",
                               "SELECT code, company, SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                               "GROUP BY code "
                               "ORDER BY SUM(cm1) DESC")

        self.fill_chart_tables(f"MTD 1",
                               f"SELECT bu1, SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                               f"WHERE month = '{month}'"
                               f"GROUP BY bu1 "
                               f"ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables(f"MTD 2",
                               f"SELECT bu2, SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                               f"WHERE month = '{month}'"
                               f"GROUP BY bu2 "
                               f"ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables(f"MTD 3",
                               f"SELECT code, company, SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                               f"WHERE month = '{month}'"
                               f"GROUP BY code "
                               f"ORDER BY SUM(cm1) DESC")

        # Filling the YTD and MTD Ranking lists
        self.fill_ranking_tables("YTD R1", "SELECT code, bu1, bu2, customer, "
                                           "SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                           "GROUP BY customer, bu1 "
                                           "ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R2", "SELECT code, bu1, bu2, customer, "
                                           "SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                           "WHERE bu1 = 'PBN Plnt Based Nutr.' "
                                           "GROUP BY customer "
                                           "ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R3", "SELECT code, bu1, bu2, customer, "
                                           "SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                           "WHERE bu1 = 'NPI Nat. Perf. Ing.' "
                                           "GROUP BY customer "
                                           "ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R4", "SELECT code, bu1, bu2, customer, "
                                           "SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                           "WHERE bu1 = 'ISS Ing. Syst.&Sol.' "
                                           "GROUP BY customer "
                                           "ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R5", "SELECT code, bu1, bu2, customer, "
                                           "SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                           "WHERE bu1 = 'Others' "
                                           "GROUP BY customer "
                                           "ORDER BY SUM(cm1) DESC")

        self.fill_ranking_tables(f"MTD R1", f"SELECT code, bu1, bu2, customer, "
                                            f"SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                            f"WHERE month = '{month}'"
                                            f"GROUP BY customer, bu1 "
                                            f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R2", f"SELECT code, bu1, bu2, customer, "
                                            f"SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                            f"WHERE bu1 = 'PBN Plnt Based Nutr.' AND month = '{month}' "
                                            f"GROUP BY customer "
                                            f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R3", f"SELECT code, bu1, bu2, customer, "
                                            f"SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                            f"WHERE bu1 = 'NPI Nat. Perf. Ing.' AND month = '{month}' "
                                            f"GROUP BY customer "
                                            f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R4", f"SELECT code, bu1, bu2, customer, "
                                            f"SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                            f"WHERE bu1 = 'ISS Ing. Syst.&Sol.' AND month = '{month}' "
                                            f"GROUP BY customer "
                                            f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R5", f"SELECT code, bu1, bu2, customer, "
                                            f"SUM(vol), SUM(ns), SUM(gs), SUM(gm), SUM(cm1) FROM sales "
                                            f"WHERE bu1 = 'Others' AND month = '{month}' "
                                            f"GROUP BY customer "
                                            f"ORDER BY SUM(cm1) DESC")

    def retranslateUi(self, SalesResultsVis):
        _translate = QtCore.QCoreApplication.translate
        SalesResultsVis.setWindowTitle(_translate("SalesResultsVis", "MainWindow"))
        self.ytd_b2b_label1.setText(_translate("SalesResultsVis", "YTD B2B Level 1"))
        self.ytd_b2b_label2.setText(_translate("SalesResultsVis", "YTD B2B Level 2"))
        self.ytd_le_label.setText(_translate("SalesResultsVis", "YTD Local/Destination comparison"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SalesResultsVis", "YTD"))
        self.ytd_top_bu2_label.setText(_translate("SalesResultsVis", "YTD Top 5 - BU 2"))
        self.ytd_top_bu1_label.setText(_translate("SalesResultsVis", "YTD Top 5 - BU 1"))
        self.ytd_top_label.setText(_translate("SalesResultsVis", "Top ranking all Business Units YTD"))
        self.ytd_top_bu4_label.setText(_translate("SalesResultsVis", "YTD Top 5 - BU 4"))
        self.ytd_top_bu3_label.setText(_translate("SalesResultsVis", "YTD Top 5 - BU 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                  _translate("SalesResultsVis", "YTD - Top Performers"))
        self.mtd_le_label.setText(_translate("SalesResultsVis", "MTD Local/Destination comparison"))
        self.mtd_b2b_label2.setText(_translate("SalesResultsVis", "MTD B2B Level 2"))
        self.mtd_b2b_label1.setText(_translate("SalesResultsVis", "MTD B2B Level 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SalesResultsVis", "MTD"))
        self.mtd_top_bu2_label.setText(_translate("SalesResultsVis", "MTD Top 5 - BU 2"))
        self.mtd_top_bu1_label.setText(_translate("SalesResultsVis", "MTD Top 5 - BU 1"))
        self.mtd_top_label.setText(_translate("SalesResultsVis", "Top ranking all Business Units MTD"))
        self.mtd_top_bu4_label.setText(_translate("SalesResultsVis", "MTD Top 5 - BU 4"))
        self.mtd_top_bu3_label.setText(_translate("SalesResultsVis", "MTD Top 5 - BU 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                  _translate("SalesResultsVis", "MTD - Top Performers"))

    def fill_chart_tables(self, table_push, query_push):
        assign_tables = {"YTD 1": self.ytd_b2b1_table, "YTD 2": self.ytd_b2b2_table, "YTD 3": self.ytd_le_table,
                         "MTD 1": self.mtd_b2b_table1, "MTD 2": self.mtd_b2b_table2, "MTD 3": self.mtd_le_table}

        self.model = QSqlTableModel(db=db)
        self.model.setTable("sales")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.query = QSqlQuery(db=db)
        self.query.prepare(query_push)
        self.query.exec_()
        self.model.setQuery(self.query)

        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Volume")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Net Sales")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Gross Sales")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Gross Margin")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "CM 1")

        if table_push == "YTD 3" or table_push == "MTD 3":
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "LE")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "LE Name")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Volume")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Net Sales")
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Gross Sales")
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Gross Margin")
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, "CM 1")
            assign_tables[table_push].setModel(self.model)
            scale_to_tableframe = assign_tables[table_push].horizontalHeader()
            scale_to_tableframe.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            scale_to_tableframe.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "BU Level 1")
            assign_tables[table_push].setModel(self.model)
            scale_to_tableframe = assign_tables[table_push].horizontalHeader()
            scale_to_tableframe.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            scale_to_tableframe.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        else:
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "BU Level 1")
            assign_tables[table_push].setModel(self.model)
            scale_to_tableframe = assign_tables[table_push].horizontalHeader()
            scale_to_tableframe.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            scale_to_tableframe.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def fill_ranking_tables(self, table_push, query_push):
        assign_tables = {"YTD R1": self.ytd_top_table, "YTD R2": self.ytd_top_bu1_table,
                         "YTD R3": self.ytd_top_bu2_table,
                         "YTD R4": self.ytd_top_bu3_table, "YTD R5": self.ytd_top_bu4_table,

                         "MTD R1": self.mtd_top_table, "MTD R2": self.mtd_top_bu1_table,
                         "MTD R3": self.mtd_top_bu2_table,
                         "MTD R4": self.mtd_top_bu3_table, "MTD R5": self.mtd_top_bu4_table}

        self.model = QSqlTableModel(db=db)
        self.model.setTable("sales")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.query = QSqlQuery(db=db)
        self.query.prepare(query_push)
        self.query.exec_()
        self.model.setQuery(self.query)

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "LE")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "BU1")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "BU2")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Customer")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Vol")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "N. Sales")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "G. Sales")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "G. Marg")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "CM1")

        assign_tables[table_push].setModel(self.model)
        scale_to_tableframe = assign_tables[table_push].horizontalHeader()
        for column in [0, 5, 6, 7, 8]:
            scale_to_tableframe.setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeToContents)
        scale_to_tableframe.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)


if __name__ == "__main__":
    import sys

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    SalesResultsVis = QtWidgets.QMainWindow()
    ui = Ui_SalesResultsVis()
    ui.setupUi(SalesResultsVis, '03')
    SalesResultsVis.show()
    sys.exit(app.exec_())