# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SalesResultsDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import numpy

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
import sqlite3
import os

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("..\\..\\Databases\\sales.db")
db.open()


class Ui_SalesResultsVis(object):
    def setupUi(self, SalesResultsVis, month, results_type):
        self.month = month  # Making it global for the methods
        self.results_type = results_type


        #self.charts_stylesheet = "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(149, 200, 216, 100), stop:0.926136 rgba(29, 41, 81, 255));"
        self.charts_stylesheet = "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(14, 77, 146, 100), stop:0.926136 rgba(14, 77, 146, 150));"
        self.charts_frame_stylesheet = "background-color: rgb(210, 210, 210); color: rgb(19, 55, 90);"


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
        self.ytd_frame.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.ytd_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.ytd_frame.setObjectName("ytd_frame")
        self.ytd_le_frame2 = QtWidgets.QFrame(self.ytd_frame)
        self.ytd_le_frame2.setGeometry(QtCore.QRect(610, 600, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.ytd_le_frame2.setFont(font)
        self.ytd_le_frame2.setStyleSheet("background-color: rgb(210, 210, 210); color: rgb(19, 55, 90);")
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
        self.ytd_le_frame1.setStyleSheet(self.charts_frame_stylesheet)
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
        self.ytd_b2b2_frame1.setStyleSheet(self.charts_frame_stylesheet)
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
        self.ytd_b2b2_frame2.setStyleSheet(self.charts_frame_stylesheet)
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
        self.ytd_b2b1_frame2.setStyleSheet(self.charts_frame_stylesheet)
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
        self.ytd_b2b1_frame1.setStyleSheet(self.charts_frame_stylesheet)
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
        self.ytd_b2b1_table.setStyleSheet(self.charts_stylesheet)
        self.ytd_b2b1_table.setObjectName("ytd_b2b1_table")
        self.ytd_b2b2_table = QtWidgets.QTableView(self.ytd_frame)
        self.ytd_b2b2_table.setGeometry(QtCore.QRect(1230, 370, 591, 221))
        self.ytd_b2b2_table.setObjectName("ytd_b2b2_table")
        self.ytd_b2b2_table.setStyleSheet(self.charts_stylesheet)
        self.ytd_le_table = QtWidgets.QTableView(self.ytd_frame)
        self.ytd_le_table.setGeometry(QtCore.QRect(1230, 650, 591, 221))
        self.ytd_le_table.setObjectName("ytd_le_table")
        self.ytd_le_table.setStyleSheet(self.charts_stylesheet)
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
        self.ytd_top_frame.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.ytd_top_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.ytd_top_frame.setObjectName("ytd_top_frame")

        self.ytd_top_order_label = QtWidgets.QLabel(self.ytd_top_frame)
        self.ytd_top_order_label.setGeometry(QtCore.QRect(660, 440, 1191, 31))
        self.ytd_top_order_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.ytd_top_order_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(22)
        self.ytd_top_order_label.setFont(font)
        self.ytd_top_order_label.setObjectName("ytd_top_order_label")



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
        self.ytd_top_bu2_table.setStyleSheet(self.charts_stylesheet)
        self.ytd_top_bu2_table.setObjectName("ytd_top_bu2_table")
        self.ytd_top_bu1_table = QtWidgets.QTableView(self.ytd_top_frame)
        self.ytd_top_bu1_table.setGeometry(QtCore.QRect(660, 80, 591, 341))
        self.ytd_top_bu1_table.setStyleSheet(self.charts_stylesheet)
        self.ytd_top_bu1_table.setObjectName("ytd_top_bu1_table")
        self.ytd_top_table = QtWidgets.QTableView(self.ytd_top_frame)
        self.ytd_top_table.setGeometry(QtCore.QRect(20, 50, 591, 821))
        self.ytd_top_table.setStyleSheet(self.charts_stylesheet)
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
        self.ytd_top_bu3_table.setStyleSheet(self.charts_stylesheet)
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
        self.ytd_top_bu4_table.setStyleSheet(self.charts_stylesheet)
        self.ytd_top_bu4_table.setObjectName("ytd_top_bu4_table")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.mtd_frame = QtWidgets.QFrame(self.tab_3)
        self.mtd_frame.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.mtd_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.mtd_frame.setObjectName("mtd_frame")
        self.mtd_le_frame2 = QtWidgets.QFrame(self.mtd_frame)
        self.mtd_le_frame2.setGeometry(QtCore.QRect(610, 600, 591, 271))
        font = QtGui.QFont()
        font.setPixelSize(29)
        self.mtd_le_frame2.setFont(font)
        self.mtd_le_frame2.setStyleSheet(self.charts_frame_stylesheet)
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
        self.mtd_le_frame1.setStyleSheet(self.charts_frame_stylesheet)
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
        self.mtd_b2b2_frame1.setStyleSheet(self.charts_frame_stylesheet)
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
        self.mtd_b2b2_frame2.setStyleSheet(self.charts_frame_stylesheet)
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
        self.mtd_b2b1_frame2.setStyleSheet(self.charts_frame_stylesheet)
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
        self.mtd_b2b1_frame1.setStyleSheet(self.charts_frame_stylesheet)
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
        self.mtd_le_table.setStyleSheet(self.charts_stylesheet)
        self.mtd_le_table.setObjectName("mtd_le_table")
        self.mtd_b2b_table2 = QtWidgets.QTableView(self.mtd_frame)
        self.mtd_b2b_table2.setGeometry(QtCore.QRect(1230, 370, 591, 221))
        self.mtd_b2b_table2.setStyleSheet(self.charts_stylesheet)
        self.mtd_b2b_table2.setObjectName("mtd_b2b_table2")
        self.mtd_b2b_table1 = QtWidgets.QTableView(self.mtd_frame)
        self.mtd_b2b_table1.setGeometry(QtCore.QRect(1230, 90, 591, 221))
        self.mtd_b2b_table1.setStyleSheet(self.charts_stylesheet)
        self.mtd_b2b_table1.setObjectName("mtd_b2b_table1")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.mtd_top_frame = QtWidgets.QFrame(self.tab_4)
        self.mtd_top_frame.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.mtd_top_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.329864, y2:0.704091, stop:0 rgba(255, 255, 255, 100), stop:0.926136 rgba(0, 35, 72, 255));")
        self.mtd_top_frame.setObjectName("mtd_top_frame")

        self.mtd_top_order_label = QtWidgets.QLabel(self.mtd_top_frame)
        self.mtd_top_order_label.setGeometry(QtCore.QRect(660, 440, 1191, 31))
        self.mtd_top_order_label.setStyleSheet("background-color: rgba(230, 230, 230, 30); color: rgb(255, 255, 255);")
        self.mtd_top_order_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPixelSize(22)
        self.mtd_top_order_label.setFont(font)
        self.mtd_top_order_label.setObjectName("mtd_top_order_label")

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
        self.mtd_top_bu2_table.setStyleSheet(self.charts_stylesheet)
        self.mtd_top_bu2_table.setObjectName("mtd_top_bu2_table")
        self.mtd_top_bu1_table = QtWidgets.QTableView(self.mtd_top_frame)
        self.mtd_top_bu1_table.setGeometry(QtCore.QRect(660, 80, 591, 341))
        self.mtd_top_bu1_table.setStyleSheet(self.charts_stylesheet)
        self.mtd_top_bu1_table.setObjectName("mtd_top_bu1_table")
        self.mtd_top_table = QtWidgets.QTableView(self.mtd_top_frame)
        self.mtd_top_table.setGeometry(QtCore.QRect(20, 50, 591, 821))
        self.mtd_top_table.setStyleSheet(self.charts_stylesheet)
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
        self.mtd_top_bu3_table.setStyleSheet(self.charts_stylesheet)
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
        self.mtd_top_bu4_table.setStyleSheet(self.charts_stylesheet)
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

        if self.results_type == "Destination Sales Results":
            # Filling the YTD and MTD tables
            self.fill_chart_tables("YTD 1",
                                   "SELECT bu1, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', "
                                   "(SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   "GROUP BY bu1 "
                                   "ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables("YTD 2",
                                   "SELECT bu2, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', "
                                   "(SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   "GROUP BY bu2 "
                                   "ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables("YTD 3",
                                   "SELECT code, company, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,"
                                   "d', (SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   "GROUP BY code "
                                   "ORDER BY SUM(cm1) DESC")

            self.fill_chart_tables(f"MTD 1",
                                   f"SELECT bu1, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                   f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   f"WHERE month = '{month}'"
                                   f"GROUP BY bu1 "
                                   f"ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables(f"MTD 2",
                                   f"SELECT bu2, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                   f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   f"WHERE month = '{month}'"
                                   f"GROUP BY bu2 "
                                   f"ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables(f"MTD 3",
                                   f"SELECT code, company, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), "
                                   f"printf('%,d', (SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   f"WHERE month = '{month}'"
                                   f"GROUP BY code "
                                   f"ORDER BY SUM(cm1) DESC")

            # Filling the YTD and MTD Ranking lists
            self.fill_ranking_tables("YTD R1", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "GROUP BY customer, bu1 "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R2", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'PBN Plnt Based Nutr.' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R3", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'NPI Nat. Perf. Ing.' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R4", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'ISS Ing. Syst.&Sol.' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R5", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'Others' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")

            self.fill_ranking_tables(f"MTD R1", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE month = '{month}'"
                                                f"GROUP BY customer, bu1 "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R2", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'PBN Plnt Based Nutr.' AND month = '{month}' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R3", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'NPI Nat. Perf. Ing.' AND month = '{month}' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R4", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'ISS Ing. Syst.&Sol.' AND month = '{month}' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R5", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'Others' AND month = '{month}' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")

            self.prepare_chart_data("YTD PIE 1", "SELECT bu1, SUM(ns) FROM sales GROUP BY bu1 ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("YTD PIE 2", "SELECT bu1, SUM(cm1) FROM sales GROUP BY bu1 ORDER BY SUM(cm1) DESC")
            self.prepare_chart_data("YTD PIE 5", "SELECT code, SUM(ns) FROM sales GROUP BY code ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("YTD PIE 6", "SELECT code, SUM(cm1) FROM sales GROUP BY code ORDER BY SUM(cm1) DESC")

            self.prepare_bar_chart_data("YTD PIE 3", "SELECT bu2, SUM(ns) FROM sales GROUP BY bu2 ORDER BY SUM(ns) ASC")
            self.prepare_bar_chart_data("YTD PIE 4", "SELECT bu2, SUM(cm1) FROM sales GROUP BY bu2 ORDER BY SUM(cm1) ASC")

            self.prepare_chart_data("MTD PIE 1", f"SELECT bu1, SUM(ns) FROM sales WHERE month = '{month}' GROUP BY bu1 ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("MTD PIE 2", f"SELECT bu1, SUM(cm1) FROM sales WHERE month = '{month}' GROUP BY bu1 ORDER BY SUM(cm1) DESC")
            self.prepare_chart_data("MTD PIE 5", f"SELECT code, SUM(ns) FROM sales WHERE month = '{month}' GROUP BY code ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("MTD PIE 6", f"SELECT code, SUM(cm1) FROM sales WHERE month = '{month}' GROUP BY code ORDER BY SUM(cm1) DESC")

            self.prepare_bar_chart_data("MTD PIE 3", f"SELECT bu2, SUM(ns) FROM sales WHERE month = '{month}' GROUP BY bu2 ORDER BY SUM(ns) ASC")
            self.prepare_bar_chart_data("MTD PIE 4", f"SELECT bu2, SUM(cm1) FROM sales WHERE month = '{month}' GROUP BY bu2 ORDER BY SUM(cm1) ASC")
        elif self.results_type == "Local Sales Results":
            # Filling the YTD and MTD tables
            self.fill_chart_tables("YTD 1",
                                   "SELECT bu1, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', "
                                   "(SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   "WHERE code = 'JP10' "
                                   "GROUP BY bu1 "
                                   "ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables("YTD 2",
                                   "SELECT bu2, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', "
                                   "(SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   "WHERE code = 'JP10' "
                                   "GROUP BY bu2 "
                                   "ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables("YTD 3",
                                   "SELECT code, company, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,"
                                   "d', (SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   "WHERE code = 'JP10'"
                                   "GROUP BY code "
                                   "ORDER BY SUM(cm1) DESC")

            self.fill_chart_tables(f"MTD 1",
                                   f"SELECT bu1, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                   f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   f"WHERE month = '{month}' AND code = 'JP10' "
                                   f"GROUP BY bu1 "
                                   f"ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables(f"MTD 2",
                                   f"SELECT bu2, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                   f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   f"WHERE month = '{month}' AND code = 'JP10' "
                                   f"GROUP BY bu2 "
                                   f"ORDER BY SUM(cm1) DESC")
            self.fill_chart_tables(f"MTD 3",
                                   f"SELECT code, company, printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), "
                                   f"printf('%,d', (SUM(gs))), printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                   f"WHERE month = '{month}' AND code = 'JP10' "
                                   f"GROUP BY code "
                                   f"ORDER BY SUM(cm1) DESC")

            # Filling the YTD and MTD Ranking lists
            self.fill_ranking_tables("YTD R1", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE code = 'JP10' "
                                               "GROUP BY customer, bu1 "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R2", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'PBN Plnt Based Nutr.' AND code = 'JP10' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R3", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'NPI Nat. Perf. Ing.' AND code = 'JP10' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R4", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'ISS Ing. Syst.&Sol.' AND code = 'JP10' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables("YTD R5", "SELECT code, bu1, bu2, customer, "
                                               "printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                               "printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                               "WHERE bu1 = 'Others' AND code = 'JP10' "
                                               "GROUP BY customer "
                                               "ORDER BY SUM(cm1) DESC")

            self.fill_ranking_tables(f"MTD R1", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE month = '{month}' AND code = 'JP10' "
                                                f"GROUP BY customer, bu1 "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R2", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'PBN Plnt Based Nutr.' AND month = '{month}' AND code = 'JP10' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R3", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'NPI Nat. Perf. Ing.' AND month = '{month}' AND code = 'JP10' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R4", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'ISS Ing. Syst.&Sol.' AND month = '{month}' AND code = 'JP10' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")
            self.fill_ranking_tables(f"MTD R5", f"SELECT code, bu1, bu2, customer, "
                                                f"printf('%,d', (SUM(vol))), printf('%,d', (SUM(ns))), printf('%,d', (SUM(gs))), "
                                                f"printf('%,d', (SUM(gm))), printf('%,d', (SUM(cm1))) FROM sales "
                                                f"WHERE bu1 = 'Others' AND month = '{month}' AND code = 'JP10' "
                                                f"GROUP BY customer "
                                                f"ORDER BY SUM(cm1) DESC")

            self.prepare_chart_data("YTD PIE 1", "SELECT bu1, SUM(ns) FROM sales WHERE code = 'JP10' GROUP BY bu1 ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("YTD PIE 2", "SELECT bu1, SUM(cm1) FROM sales WHERE code = 'JP10' GROUP BY bu1 ORDER BY SUM(cm1) DESC")
            self.prepare_chart_data("YTD PIE 5", "SELECT code, SUM(ns) FROM sales GROUP BY code ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("YTD PIE 6", "SELECT code, SUM(cm1) FROM sales GROUP BY code ORDER BY SUM(cm1) DESC")

            # self.prepare_chart_data("YTD PIE 5", "SELECT code, SUM(ns) FROM sales WHERE code = 'JP10' GROUP BY code ORDER BY SUM(ns) DESC")
            # self.prepare_chart_data("YTD PIE 6", "SELECT code, SUM(cm1) FROM sales WHERE code = 'JP10' GROUP BY code ORDER BY SUM(cm1) DESC")

            self.prepare_bar_chart_data("YTD PIE 3", "SELECT bu2, SUM(ns) FROM sales WHERE code = 'JP10' GROUP BY bu2 ORDER BY SUM(ns) ASC")
            self.prepare_bar_chart_data("YTD PIE 4", "SELECT bu2, SUM(cm1) FROM sales WHERE code = 'JP10' GROUP BY bu2 ORDER BY SUM(cm1) ASC")

            self.prepare_chart_data("MTD PIE 1", f"SELECT bu1, SUM(ns) FROM sales WHERE month = '{month}' AND code = 'JP10' GROUP BY bu1 ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("MTD PIE 2", f"SELECT bu1, SUM(cm1) FROM sales WHERE month = '{month}' AND code = 'JP10' GROUP BY bu1 ORDER BY SUM(cm1) DESC")
            self.prepare_chart_data("MTD PIE 5", f"SELECT code, SUM(ns) FROM sales WHERE month = '{month}' GROUP BY code ORDER BY SUM(ns) DESC")
            self.prepare_chart_data("MTD PIE 6", f"SELECT code, SUM(cm1) FROM sales WHERE month = '{month}' GROUP BY code ORDER BY SUM(cm1) DESC")


            # self.prepare_chart_data("MTD PIE 5", f"SELECT code, SUM(ns) FROM sales WHERE month = '{month}' AND code = 'JP10' GROUP BY code ORDER BY SUM(ns) DESC")
            # self.prepare_chart_data("MTD PIE 6", f"SELECT code, SUM(cm1) FROM sales WHERE month = '{month}' AND code = 'JP10' GROUP BY code ORDER BY SUM(cm1) DESC")

            self.prepare_bar_chart_data("MTD PIE 3", f"SELECT bu2, SUM(ns) FROM sales WHERE month = '{month}' AND code = 'JP10' GROUP BY bu2 ORDER BY SUM(ns) ASC")
            self.prepare_bar_chart_data("MTD PIE 4", f"SELECT bu2, SUM(cm1) FROM sales WHERE month = '{month}' AND code = 'JP10' GROUP BY bu2 ORDER BY SUM(cm1) ASC")

    def retranslateUi(self, SalesResultsVis):
        _translate = QtCore.QCoreApplication.translate
        SalesResultsVis.setWindowTitle(_translate("SalesResultsVis", "MainWindow"))
        self.ytd_top_order_label.setText(_translate("SalesResultsVis", "All rankings are ordered by CM1"))
        self.ytd_b2b_label1.setText(_translate("SalesResultsVis", "YTD B2B Level 1"))
        self.ytd_b2b_label2.setText(_translate("SalesResultsVis", "YTD B2B Level 2"))
        self.ytd_le_label.setText(_translate("SalesResultsVis", "YTD Local/Destination comparison"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SalesResultsVis", "YTD"))
        self.ytd_top_bu2_label.setText(_translate("SalesResultsVis", "YTD Top ranking - NPI"))
        self.ytd_top_bu1_label.setText(_translate("SalesResultsVis", "YTD Top ranking - PBN"))
        self.ytd_top_label.setText(_translate("SalesResultsVis", "Top ranking all Business Units YTD"))
        self.ytd_top_bu4_label.setText(_translate("SalesResultsVis", "YTD Top ranking - Others"))
        self.ytd_top_bu3_label.setText(_translate("SalesResultsVis", "YTD Top ranking - ISS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                  _translate("SalesResultsVis", "YTD - Top Performers"))
        self.mtd_top_order_label.setText(_translate("SalesResultsVis", "All rankings are ordered by CM1"))
        self.mtd_le_label.setText(_translate("SalesResultsVis", f"Month {self.month} - Local/Destination comparison"))
        self.mtd_b2b_label2.setText(_translate("SalesResultsVis", f"Month {self.month} - B2B Level 2"))
        self.mtd_b2b_label1.setText(_translate("SalesResultsVis", f"Month {self.month} - B2B Level 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SalesResultsVis", "MTD"))
        self.mtd_top_bu2_label.setText(_translate("SalesResultsVis", f"Month {self.month} - Top ranking - NPI"))
        self.mtd_top_bu1_label.setText(_translate("SalesResultsVis", f"Month {self.month} - ranking - PBN"))
        self.mtd_top_label.setText(_translate("SalesResultsVis", f"Top ranking all Business Units - Month {self.month}"))
        self.mtd_top_bu4_label.setText(_translate("SalesResultsVis", f"Month {self.month} - Top ranking - Others"))
        self.mtd_top_bu3_label.setText(_translate("SalesResultsVis", f"Month {self.month} - Top ranking - ISS"))
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
        for column in [0, 4, 5, 6, 7, 8]:
            scale_to_tableframe.setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeToContents)
        #scale_to_tableframe.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def prepare_chart_data(self, chart_push, query_push):
        assign_charts = {"YTD PIE 1": self.ytd_b2b1_chart1, "YTD PIE 2": self.ytd_b2b1_chart2,
                         "YTD PIE 3": self.ytd_b2b2_chart1, "YTD PIE 4": self.ytd_b2b2_chart2,
                         "YTD PIE 5": self.ytd_le_chart1, "YTD PIE 6": self.ytd_le_chart2,

                         "MTD PIE 1": self.mtd_b2b1_chart1, "MTD PIE 2": self.mtd_b2b1_chart2,
                         "MTD PIE 3": self.mtd_b2b2_chart1, "MTD PIE 4": self.mtd_b2b2_chart2,
                         "MTD PIE 5": self.mtd_le_chart1, "MTD PIE 6": self.mtd_le_chart2}

        assign_titles = {"YTD PIE 1": "Net Sales B2B Level 1 - YTD", "YTD PIE 2": "CM1 B2B Level 1 - YTD",
                         "YTD PIE 3": "Net Sales B2B Level 2 - YTD", "YTD PIE 4": "CM1 B2B Level 2- YTD",
                         "YTD PIE 5": "Net Sales Legal Entity - YTD", "YTD PIE 6": "CM1 Legal Entity - YTD",

                         "MTD PIE 1": "Net Sales B2B Level 1 - MTD", "MTD PIE 2": "CM1 B2B Level 1 - MTD",
                         "MTD PIE 3": "Net Sales B2B Level 2 - MTD", "MTD PIE 4": "CM1 B2B Level 2 - MTD",
                         "MTD PIE 5": "Net Sales Legal Entity - MTD", "MTD PIE 6": "CM1 Legal Entity - MTD"}


        connect = sqlite3.connect("..\\..\\Databases\\sales.db")
        c = connect.cursor()

        c.execute(query_push)
        data = c.fetchall()

        chart_labels_legend = [i for i in data for i in i if isinstance(i, str)]  # A list in list, so we need nested comprehension
        chart_data = [i for i in data for i in i if isinstance(i, int)]

        summed_data = 0
        for amt in chart_data:
            summed_data += amt
        percentages = [round(float(p / summed_data * 100), 1) for p in chart_data]

        if "JP10" in chart_labels_legend:  # for the LE pie chart, we only want to show JP10 in the chart
            chart_labels_chart = ["" if i != "JP10" else "JP10" for i in chart_labels_legend]
        else:
            chart_labels_chart = chart_labels_legend

        chart_labels_legend = ['%s, %1.1f %%' % (l, s) for l, s in zip(chart_labels_legend, percentages)]



        for index, value in enumerate(chart_data):  # Cant put minus values in a pie. Just put to 0
            if value < 0:
                chart_data[index] = 0

        chart_figure = Figure()
        chart_canvas = FigureCanvasQTAgg(chart_figure)
        chart_final = chart_figure.add_subplot(111)

        chart_final.pie(chart_data, labels=chart_labels_chart, startangle=180, autopct=self.autopct)

        chart_final.set_title(label=assign_titles[chart_push], fontsize=16)
        chart_final.legend(labels=chart_labels_legend, loc="upper left", bbox_to_anchor=(-1.65, 1.25), fontsize=8)
        chart_figure.patch.set_facecolor("#E6E6E6")

        chart_figure.subplots_adjust(left=0.4, top=0.8)

        chart_canvas.show()

        assign_charts[chart_push].addWidget(chart_canvas)

        c.close()
        connect.close()

    def prepare_bar_chart_data(self, chart_push, query_push):
        assign_charts = {"YTD PIE 3": self.ytd_b2b2_chart1, "YTD PIE 4": self.ytd_b2b2_chart2,
                         "MTD PIE 3": self.mtd_b2b2_chart1, "MTD PIE 4": self.mtd_b2b2_chart2}
        assign_titles = {"YTD PIE 3": "Net Sales B2B Level 2 - YTD", "YTD PIE 4": "CM1 B2B Level 2 - YTD",
                         "MTD PIE 3": "Net Sales B2B Level 2 - MTD", "MTD PIE 4": "CM1 B2B Level 2 - MTD"}

        connect = sqlite3.connect("..\\..\\Databases\\sales.db")
        c = connect.cursor()

        c.execute(query_push)
        data = c.fetchall()

        chart_labels = [i for i in data for i in i if isinstance(i, str)]  # A list in list, so we need nested comprehension
        chart_data = [i for i in data for i in i if isinstance(i, int)]

        summed_data = 0
        for amt in chart_data:
            summed_data += amt
        percentages = [round(float(p / summed_data * 100), 1) for p in chart_data]
        print(percentages)

        chart_labels_pct = ['%s, %1.1f %%' % (l, s) for l, s in zip(chart_labels, percentages)]

        for index, value in enumerate(chart_data):
            if value < 0:
                chart_data[index] = 0

        chart_figure = Figure()
        chart_canvas = FigureCanvasQTAgg(chart_figure)
        chart_final = chart_figure.add_subplot(111)

        chart_final.barh(chart_labels_pct, percentages)

        chart_final.set_title(assign_titles[chart_push], fontsize=16)
        #chart_final.set_xlim([0, 100])
        chart_final.tick_params(axis="both", labelsize=8)
        chart_figure.patch.set_facecolor("#E6E6E6")
        chart_final.patch.set_facecolor("#E6E6E6")


        chart_figure.subplots_adjust(left=0.3, right=0.9)

        chart_canvas.show()

        assign_charts[chart_push].addWidget(chart_canvas)

        c.close()
        connect.close()

    def autopct(self, pct):
        return ('%1.1f%%' % pct) if pct > 12 else ''


if __name__ == "__main__":
    import sys

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    SalesResultsVis = QtWidgets.QMainWindow()
    ui = Ui_SalesResultsVis()
    ui.setupUi(SalesResultsVis)
    SalesResultsVis.show()
    sys.exit(app.exec_())
