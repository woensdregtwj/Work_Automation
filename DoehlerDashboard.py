# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doehlerDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from SalesForecastUpdateEOM import *
from SalesResultsAnalysis import *
from SendForecast import *
from LTODateFormatting import *
from ltoAnalysis import *
from AgingList import *

import datetime
import webbrowser

from LinkApplications import WindowApplication
from Calculations.Deadlines import Deadlines

class Ui_Doehler_title(object):
    def setupUi(self, Doehler_title):
        Doehler_title.setObjectName("Doehler_title")
        Doehler_title.setEnabled(True)
        Doehler_title.resize(1220, 645)
        Doehler_title.setMinimumSize(QtCore.QSize(1220, 645))
        Doehler_title.setMaximumSize(QtCore.QSize(1220, 645))
        Doehler_title.setAutoFillBackground(False)
        Doehler_title.setWindowTitle("Doehler Japan")
        self.centralwidget = QtWidgets.QWidget(Doehler_title)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(100, 0, 1121, 81))
        self.app_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.app_title.setText("Doehler Japan Dashboard")
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPixelSize(32)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.app_title.setFont(font)
        self.app_title.setStyleSheet("background-color: rgb(0, 35, 72);\n"
"color: rgb(255, 255, 255);")
        self.app_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.app_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.app_title.setMidLineWidth(0)
        self.app_title.setTextFormat(QtCore.Qt.PlainText)
        self.app_title.setAlignment(QtCore.Qt.AlignCenter)
        self.app_title.setWordWrap(False)
        self.app_title.setObjectName("app_title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 101, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/DoehlerLogo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.__add_forecasting_box()
        self.__add_monthly_box()
        self.__add_controlling_box()
        self.__add_deadlines_box()
        self.__add_extra_box()
        self.__connect_buttons()

        self.calculate_deadlines()
        Doehler_title.setCentralWidget(self.centralwidget)

    def __add_forecasting_box(self):
        self.forecasting_box = QtWidgets.QGroupBox(self.centralwidget)
        self.forecasting_box.setGeometry(QtCore.QRect(10, 80, 361, 431))
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.forecasting_box.setFont(font)
        self.forecasting_box.setObjectName("forecasting_box")
        self.forecasting_box.setTitle("Forecasting")
        self.sforecast_button = QtWidgets.QPushButton(self.forecasting_box)
        self.sforecast_button.setGeometry(QtCore.QRect(170, 40, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sforecast_button.setFont(font)
        self.sforecast_button.setObjectName("sforecast_button")
        self.sforecast_button.setText("Sales Forecast Update")
        self.sforecast_eom_button = QtWidgets.QPushButton(self.forecasting_box)
        self.sforecast_eom_button.setGeometry(QtCore.QRect(170, 120, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        self.sforecast_eom_button.setFont(font)
        self.sforecast_eom_button.setObjectName("sforecast_eom_button")
        self.sforecast_eom_button.setText("Sales Forecast EOM")
        self.sresults_visuals = QtWidgets.QPushButton(self.forecasting_box)
        self.sresults_visuals.setGeometry(QtCore.QRect(170, 200, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        self.sresults_visuals.setFont(font)
        self.sresults_visuals.setObjectName("sresults_visuals")
        self.sresults_visuals.setText("Sales Results Visuals")
        self.bpm_forecast_button = QtWidgets.QPushButton(self.forecasting_box)
        self.bpm_forecast_button.setGeometry(QtCore.QRect(170, 280, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        self.bpm_forecast_button.setFont(font)
        self.bpm_forecast_button.setObjectName("bpm_forecast_button")
        self.bpm_forecast_button.setText("BPM Forecast")
        self.bpm_visuals_button = QtWidgets.QPushButton(self.forecasting_box)
        self.bpm_visuals_button.setGeometry(QtCore.QRect(170, 360, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        self.bpm_visuals_button.setFont(font)
        self.bpm_visuals_button.setObjectName("bpm_visuals_button")
        self.bpm_visuals_button.setText("BPM Visuals")
        self.forecast1_label = QtWidgets.QLabel(self.forecasting_box)
        self.forecast1_label.setEnabled(True)
        self.forecast1_label.setGeometry(QtCore.QRect(20, 60, 141, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forecast1_label.sizePolicy().hasHeightForWidth())
        self.forecast1_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.forecast1_label.setFont(font)
        self.forecast1_label.setObjectName("forecast1_label")
        self.forecast1_label.setText("MTD Sales <> Forecast")
        self.forecast2_label = QtWidgets.QLabel(self.forecasting_box)
        self.forecast2_label.setGeometry(QtCore.QRect(20, 140, 151, 21))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.forecast2_label.setFont(font)
        self.forecast2_label.setObjectName("forecast2_label")
        self.forecast2_label.setText("After Sales Upload")

    def __add_monthly_box(self):
        self.monthly_box = QtWidgets.QGroupBox(self.centralwidget)
        self.monthly_box.setGeometry(QtCore.QRect(420, 80, 371, 431))
        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.monthly_box.setFont(font)
        self.monthly_box.setObjectName("monthly_box")
        self.monthly_box.setTitle("Monthly Closing")
        self.bwaging_button = QtWidgets.QPushButton(self.monthly_box)
        self.bwaging_button.setGeometry(QtCore.QRect(180, 40, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bwaging_button.setFont(font)
        self.bwaging_button.setObjectName("bwaging_button")
        self.bwaging_button.setText("BW Aging List")
        self.salesupload_button = QtWidgets.QPushButton(self.monthly_box)
        self.salesupload_button.setGeometry(QtCore.QRect(180, 120, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.salesupload_button.setFont(font)
        self.salesupload_button.setObjectName("salesupload_button")
        self.salesupload_button.setText("Sales Upload")
        self.bcs_button = QtWidgets.QPushButton(self.monthly_box)
        self.bcs_button.setGeometry(QtCore.QRect(180, 200, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bcs_button.setFont(font)
        self.bcs_button.setObjectName("bcs_button")
        self.bcs_button.setText("BCS + Inventory")
        self.ic_button = QtWidgets.QPushButton(self.monthly_box)
        self.ic_button.setGeometry(QtCore.QRect(180, 280, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ic_button.setFont(font)
        self.ic_button.setObjectName("ic_button")
        self.ic_button.setText("IC Reconciliation")
        self.bpc_button = QtWidgets.QPushButton(self.monthly_box)
        self.bpc_button.setGeometry(QtCore.QRect(180, 360, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bpc_button.setFont(font)
        self.bpc_button.setObjectName("bpc_button")
        self.bpc_button.setText("BPC")
        self.monthly1_label = QtWidgets.QLabel(self.monthly_box)
        self.monthly1_label.setGeometry(QtCore.QRect(20, 60, 151, 21))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.monthly1_label.setFont(font)
        self.monthly1_label.setObjectName("monthly1_label")
        self.monthly2_label = QtWidgets.QLabel(self.monthly_box)
        self.monthly2_label.setGeometry(QtCore.QRect(20, 140, 151, 21))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.monthly2_label.setFont(font)
        self.monthly2_label.setObjectName("monthly2_label")
        self.monthly4_label = QtWidgets.QLabel(self.monthly_box)
        self.monthly4_label.setGeometry(QtCore.QRect(20, 300, 151, 21))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.monthly4_label.setFont(font)
        self.monthly4_label.setObjectName("monthly4_label")
        self.monthly3_label = QtWidgets.QLabel(self.monthly_box)
        self.monthly3_label.setGeometry(QtCore.QRect(20, 220, 151, 21))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.monthly3_label.setFont(font)
        self.monthly3_label.setObjectName("monthly3_label")
        self.monthly5_label = QtWidgets.QLabel(self.monthly_box)
        self.monthly5_label.setGeometry(QtCore.QRect(20, 380, 151, 21))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.monthly5_label.setFont(font)
        self.monthly5_label.setObjectName("monthly5_label")

    def __add_controlling_box(self):
        self.controlling_box = QtWidgets.QGroupBox(self.centralwidget)
        self.controlling_box.setGeometry(QtCore.QRect(840, 80, 371, 281))
        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.controlling_box.setFont(font)
        self.controlling_box.setObjectName("controlling_box")
        self.controlling_box.setTitle("Controlling")
        self.lto_button = QtWidgets.QPushButton(self.controlling_box)
        self.lto_button.setGeometry(QtCore.QRect(180, 40, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lto_button.setFont(font)
        self.lto_button.setObjectName("lto_button")
        self.lto_button.setText("LTO Analysis")
        self.legal_button = QtWidgets.QPushButton(self.controlling_box)
        self.legal_button.setGeometry(QtCore.QRect(180, 120, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.legal_button.setFont(font)
        self.legal_button.setObjectName("legal_button")
        self.legal_button.setText("Local FC Analysis")
        self.bpm_analysis_button = QtWidgets.QPushButton(self.controlling_box)
        self.bpm_analysis_button.setGeometry(QtCore.QRect(180, 200, 151, 61))
        font = QtGui.QFont()
        font.setPixelSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bpm_analysis_button.setFont(font)
        self.bpm_analysis_button.setObjectName("bpm_analysis_button")
        self.bpm_analysis_button.setText("BPM FC Analysis")

    def __add_deadlines_box(self):
        self.deadlines_box = QtWidgets.QGroupBox(self.centralwidget)
        self.deadlines_box.setGeometry(QtCore.QRect(840, 370, 371, 141))
        font = QtGui.QFont()
        font.setPixelSize(14)
        self.deadlines_box.setFont(font)
        self.deadlines_box.setObjectName("deadlines_box")
        self.deadlines_box.setTitle("Fixed Deadlines")
        self.deadline1_label = QtWidgets.QLabel(self.deadlines_box)
        self.deadline1_label.setGeometry(QtCore.QRect(20, 30, 341, 16))
        self.deadline1_label.setObjectName("deadline1_label")
        self.deadline1_label.setText("Fixed Deadline 1")
        self.deadline2_label = QtWidgets.QLabel(self.deadlines_box)
        self.deadline2_label.setGeometry(QtCore.QRect(20, 50, 341, 16))
        self.deadline2_label.setObjectName("deadline2_label")
        self.deadline2_label.setText("Fixed Deadline 2")
        self.deadline3_label = QtWidgets.QLabel(self.deadlines_box)
        self.deadline3_label.setGeometry(QtCore.QRect(20, 70, 341, 16))
        self.deadline3_label.setObjectName("deadline3_label")
        self.deadline3_label.setText("Fixed Deadline 3")
        self.deadline4_label = QtWidgets.QLabel(self.deadlines_box)
        self.deadline4_label.setGeometry(QtCore.QRect(20, 90, 341, 16))
        self.deadline4_label.setObjectName("deadline4_label")
        self.deadline4_label.setText("Fixed Deadline 4")
        self.deadline5_label = QtWidgets.QLabel(self.deadlines_box)
        self.deadline5_label.setGeometry(QtCore.QRect(20, 110, 341, 16))
        self.deadline5_label.setObjectName("deadline5_label")
        self.deadline5_label.setText("Fixed Deadline 5")

    def __add_extra_box(self):
        self.extra_box = QtWidgets.QGroupBox(self.centralwidget)
        self.extra_box.setGeometry(QtCore.QRect(10, 510, 1201, 91))
        self.extra_box.setObjectName("groupBox_3")
        self.extra_box.setTitle("Extra Tools")
        self.pushButton = QtWidgets.QPushButton(self.extra_box)
        self.pushButton.setGeometry(QtCore.QRect(60, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("FX Calculator")
        self.pushButton_5 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("tm5 Login")
        self.pushButton_6 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText("Salesforce")
        self.pushButton_7 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText("Commerzbank")
        self.pushButton_8 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_8.setGeometry(QtCore.QRect(500, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setText("BPM System")
        self.pushButton_9 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_9.setGeometry(QtCore.QRect(610, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setText("Doehler Portal")
        self.pushButton_10 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_10.setGeometry(QtCore.QRect(720, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setText("TBA")
        self.pushButton_11 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_11.setGeometry(QtCore.QRect(830, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setText("TBA")
        self.pushButton_12 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_12.setGeometry(QtCore.QRect(940, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setText("TBA")
        self.pushButton_13 = QtWidgets.QPushButton(self.extra_box)
        self.pushButton_13.setGeometry(QtCore.QRect(1050, 40, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setText("LTO Date Format")

    def __connect_buttons(self):
        self.open_app = WindowApplication()

        self.sforecast_button.clicked.connect(self.open_app.sales_forecast_update)
        self.sforecast_eom_button.clicked.connect(self.open_app.sales_forecast_EOM)
        self.legal_button.clicked.connect(self.open_app.local_fc_analysis)
        self.bwaging_button.clicked.connect(self.open_app.aging_upload)
        self.lto_button.clicked.connect(self.open_app.lto_analysis)
        self.sresults_visuals.clicked.connect(self.open_app.sales_visuals)
        self.salesupload_button.clicked.connect(self.open_app.sales_upload)

        self.pushButton_13.clicked.connect(self.open_app.lto_date_convert)
        self.pushButton_5.clicked.connect(self.open_app.tm5_website)
        self.pushButton_6.clicked.connect(self.open_app.salesforce_website)
        self.pushButton_7.clicked.connect(self.open_app.commerz_website)
        self.pushButton_8.clicked.connect(self.open_app.bpm_website)
        self.pushButton_9.clicked.connect(self.open_app.doehler_website)

    def calculate_deadlines(self):
        deadlines = Deadlines()
        deadlines.prepare_deadline_dates()
        deadlines.format_deadline_text()

        self.monthly1_label.setText(deadlines.deadline_days_text[1])
        self.monthly2_label.setText(deadlines.deadline_days_text[1])
        self.monthly3_label.setText(deadlines.deadline_days_text[2])
        self.monthly4_label.setText(deadlines.deadline_days_text[0])
        self.monthly5_label.setText(deadlines.deadline_days_text[4])


if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    Doehler_title = QtWidgets.QMainWindow()
    ui = Ui_Doehler_title()
    ui.setupUi(Doehler_title)
    Doehler_title.show()
    sys.exit(app.exec_())
