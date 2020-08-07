# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendForecast.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from SendForecastFunction import *
from SendForecastSummaryFunction import *
from SalesDashboard import *
import time


class Ui_individual_forecast(object):
    def setupUi(self, individual_forecast):
        individual_forecast.setObjectName("individual_forecast")
        individual_forecast.resize(800, 640)
        individual_forecast.setMinimumSize(QtCore.QSize(800, 640))
        individual_forecast.setMaximumSize(QtCore.QSize(800, 640))
        self.centralwidget = QtWidgets.QWidget(individual_forecast)
        self.centralwidget.setObjectName("centralwidget")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(100, 0, 701, 81))
        self.app_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.selection_box = QtWidgets.QGroupBox(self.centralwidget)
        self.selection_box.setGeometry(QtCore.QRect(10, 100, 351, 321))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.selection_box.setFont(font)
        self.selection_box.setObjectName("selection_box")
        self.kam_label = QtWidgets.QLabel(self.selection_box)
        self.kam_label.setGeometry(QtCore.QRect(20, 40, 161, 21))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.kam_label.setFont(font)
        self.kam_label.setObjectName("kam_label")
        self.kam_box = QtWidgets.QComboBox(self.selection_box)
        self.kam_box.setGeometry(QtCore.QRect(240, 40, 91, 23))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.kam_box.setFont(font)
        self.kam_box.setObjectName("kam_box")
        self.kam_box.addItem("")
        self.kam_box.addItem("")
        self.kam_box.addItem("")
        self.kam_box.addItem("")
        self.kam_box.addItem("")
        self.month_box = QtWidgets.QComboBox(self.selection_box)
        self.month_box.setGeometry(QtCore.QRect(240, 90, 91, 23))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.month_box.setFont(font)
        self.month_box.setObjectName("month_box")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_box.addItem("")
        self.month_label = QtWidgets.QLabel(self.selection_box)
        self.month_label.setGeometry(QtCore.QRect(20, 90, 221, 21))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.month_label.setFont(font)
        self.month_label.setObjectName("month_label")
        self.currency_label = QtWidgets.QLabel(self.selection_box)
        self.currency_label.setGeometry(QtCore.QRect(20, 140, 181, 21))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.currency_label.setFont(font)
        self.currency_label.setObjectName("currency_label")
        self.currency_box = QtWidgets.QComboBox(self.selection_box)
        self.currency_box.setGeometry(QtCore.QRect(240, 140, 91, 23))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.currency_box.setFont(font)
        self.currency_box.setObjectName("currency_box")
        self.currency_box.addItem("")
        self.currency_box.addItem("")
        self.fx_label = QtWidgets.QLabel(self.selection_box)
        self.fx_label.setGeometry(QtCore.QRect(18, 190, 141, 18))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.fx_label.setFont(font)
        self.fx_label.setObjectName("fx_label")
        self.fx_edit = QtWidgets.QLineEdit(self.selection_box)
        self.fx_edit.setEnabled(True)
        self.fx_edit.setGeometry(QtCore.QRect(240, 190, 91, 23))
        self.fx_edit.setText("")
        self.fx_edit.setObjectName("fx_edit")
        self.actions_box = QtWidgets.QGroupBox(self.centralwidget)
        self.actions_box.setGeometry(QtCore.QRect(10, 450, 781, 101))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.actions_box.setFont(font)
        self.actions_box.setObjectName("actions_box")
        self.extract_label = QtWidgets.QLabel(self.actions_box)
        self.extract_label.setGeometry(QtCore.QRect(30, 30, 291, 18))
        self.extract_label.setObjectName("extract_label")
        self.extract_button = QtWidgets.QPushButton(self.actions_box)
        self.extract_button.setEnabled(False)
        self.extract_button.setGeometry(QtCore.QRect(30, 60, 211, 31))
        self.extract_button.setObjectName("extract_button")
        self.dashboard_label = QtWidgets.QLabel(self.actions_box)
        self.dashboard_label.setGeometry(QtCore.QRect(505, 30, 201, 20))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dashboard_label.setFont(font)
        self.dashboard_label.setObjectName("dashboard_label")
        self.dashboard_button = QtWidgets.QPushButton(self.actions_box)
        self.dashboard_button.setEnabled(False)
        self.dashboard_button.setGeometry(QtCore.QRect(440, 60, 271, 31))
        self.dashboard_button.setObjectName("dashboard_button")
        self.upload_box = QtWidgets.QGroupBox(self.centralwidget)
        self.upload_box.setGeometry(QtCore.QRect(380, 100, 411, 191))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.upload_box.setFont(font)
        self.upload_box.setObjectName("upload_box")
        self.upload_label = QtWidgets.QLabel(self.upload_box)
        self.upload_label.setGeometry(QtCore.QRect(30, 30, 491, 18))
        self.upload_label.setObjectName("upload_label")
        self.uploaded_label = QtWidgets.QLabel(self.upload_box)
        self.uploaded_label.setGeometry(QtCore.QRect(30, 120, 371, 31))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.uploaded_label.setFont(font)
        self.uploaded_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploaded_label.setObjectName("uploaded_label")
        self.upload_button = QtWidgets.QPushButton(self.upload_box)
        self.upload_button.setGeometry(QtCore.QRect(30, 60, 211, 31))
        self.upload_button.setObjectName("upload_button")
        self.forecast_box = QtWidgets.QGroupBox(self.centralwidget)
        self.forecast_box.setGeometry(QtCore.QRect(380, 310, 411, 111))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.forecast_box.setFont(font)
        self.forecast_box.setObjectName("forecast_box")
        self.overhead_label = QtWidgets.QLabel(self.forecast_box)
        self.overhead_label.setGeometry(QtCore.QRect(40, 30, 141, 18))
        self.overhead_label.setObjectName("overhead_label")
        self.summary_button = QtWidgets.QPushButton(self.forecast_box)
        self.summary_button.setEnabled(False)
        self.summary_button.setGeometry(QtCore.QRect(30, 70, 201, 31))
        self.summary_button.setObjectName("summary_button")
        self.overhead_edit = QtWidgets.QLineEdit(self.forecast_box)
        self.overhead_edit.setGeometry(QtCore.QRect(242, 30, 131, 23))
        self.overhead_edit.setText("")
        self.overhead_edit.setObjectName("overhead_edit")
        individual_forecast.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(individual_forecast)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        individual_forecast.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(individual_forecast)
        self.statusbar.setObjectName("statusbar")
        individual_forecast.setStatusBar(self.statusbar)

        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setGeometry(QtCore.QRect(30, 560, 751, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")

        self.retranslateUi(individual_forecast)
        QtCore.QMetaObject.connectSlotsByName(individual_forecast)

        self.upload_button.clicked.connect(self.upload_forecast)
        self.extract_button.clicked.connect(self.extract_forecast)
        self.summary_button.clicked.connect(self.extract_summary)
        self.dashboard_button.clicked.connect(self.open_dashboard)


    def retranslateUi(self, individual_forecast):
        _translate = QtCore.QCoreApplication.translate
        individual_forecast.setWindowTitle(_translate("individual_forecast", "MainWindow"))
        self.app_title.setText(_translate("individual_forecast", "Individual Sales Forecast"))
        self.selection_box.setTitle(_translate("individual_forecast", "KAM Select"))
        self.kam_label.setText(_translate("individual_forecast", "Select KAM"))
        self.kam_box.setItemText(0, _translate("individual_forecast", "All"))
        self.kam_box.setItemText(1, _translate("individual_forecast", "Seiichi Hiyoshi"))
        self.kam_box.setItemText(2, _translate("individual_forecast", "Takao Yamamoto"))
        self.kam_box.setItemText(3, _translate("individual_forecast", "Yasuhiko Suzuki"))
        self.kam_box.setItemText(4, _translate("individual_forecast", "Kota Takahashi"))
        self.month_box.setItemText(0, _translate("individual_forecast", "Jan"))
        self.month_box.setItemText(1, _translate("individual_forecast", "Feb"))
        self.month_box.setItemText(2, _translate("individual_forecast", "Mar"))
        self.month_box.setItemText(3, _translate("individual_forecast", "Apr"))
        self.month_box.setItemText(4, _translate("individual_forecast", "May"))
        self.month_box.setItemText(5, _translate("individual_forecast", "Jun"))
        self.month_box.setItemText(6, _translate("individual_forecast", "Jul"))
        self.month_box.setItemText(7, _translate("individual_forecast", "Aug"))
        self.month_box.setItemText(8, _translate("individual_forecast", "Sep"))
        self.month_box.setItemText(9, _translate("individual_forecast", "Oct"))
        self.month_box.setItemText(10, _translate("individual_forecast", "Nov"))
        self.month_box.setItemText(11, _translate("individual_forecast", "Dec"))
        self.month_label.setText(_translate("individual_forecast", "Current Forecast Month"))
        self.currency_label.setText(_translate("individual_forecast", "Currency Convert"))
        self.currency_box.setItemText(0, _translate("individual_forecast", "No"))
        self.currency_box.setItemText(1, _translate("individual_forecast", "Yes"))
        self.fx_label.setText(_translate("individual_forecast", "FX Rate"))
        self.actions_box.setTitle(_translate("individual_forecast", "Actions"))
        self.extract_label.setText(_translate("individual_forecast", "Extract forecast file for KAM"))
        self.extract_button.setText(_translate("individual_forecast", "Extract File"))
        self.dashboard_label.setText(_translate("individual_forecast", "View sales dashboard"))
        self.dashboard_button.setText(_translate("individual_forecast", "Dashboard"))
        self.upload_box.setTitle(_translate("individual_forecast", "Upload Forecast File"))
        self.upload_label.setText(_translate("individual_forecast", "Upload latest forecast file"))
        self.uploaded_label.setText(_translate("individual_forecast", "No Sales Forecast File Loaded"))
        self.upload_button.setText(_translate("individual_forecast", "Upload Sales Forecast"))
        self.forecast_box.setTitle(_translate("individual_forecast", "Extract Forecast Summary"))
        self.overhead_label.setText(_translate("individual_forecast", "Overhead costs"))
        self.summary_button.setText(_translate("individual_forecast", "Extract Summary"))


    def upload_forecast(self):
        self.forecast_file = QtWidgets.QFileDialog.getOpenFileName(filter="*.xlsx")

        if not self.forecast_file[0]:
            self.uploaded_label.setText("No file has been uploaded")
            self.uploaded_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.uploaded_label.setText(f"Loaded: {os.path.basename(self.forecast_file[0])}")
            self.uploaded_label.setStyleSheet("background-color: rgb(174, 217, 167);")
            self.forecast_file = os.path.abspath(self.forecast_file[0])
            print(self.forecast_file)

            self.extract_button.setEnabled(True)
            self.summary_button.setEnabled(True)
            self.dashboard_button.setEnabled(True)

    def extract_forecast(self):
        self.kam = self.kam_box.currentText()
        self.month = self.month_box.currentText()
        self.currency_enabled = self.currency_box.currentText()
        print(self.kam, self.month)

        self.confirm_details = QtWidgets.QMessageBox()
        self.confirm_details.setIcon(QtWidgets.QMessageBox.Question)

        if self.currency_enabled == "Yes":
            try:
                self.fx = int(self.fx_edit.text())
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("Please only enter NUMBERS as FX Rate.")
                error_dialog.exec_()
                return
            self.confirm_details.setText(f"Selected KAM: {self.kam}\n"
                                         f"Selected month: {self.month}\n\n"
                                         f"Currency convert enabled.\n"
                                         f"FX rate: {self.fx}\n\n"
                                         f"Continue?")
        else:
            self.fx = None
            self.confirm_details.setText(f"Selected KAM: {self.kam}\n"
                                         f"Selected month: {self.month}\n\n"
                                         f"Continue?")

        self.confirm_details.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.confirm_details_pressed = self.confirm_details.exec_()

        if self.confirm_details_pressed != QtWidgets.QMessageBox.Ok:
            return

        self.extract_button.setEnabled(False)

        time.sleep(1)

        self.progress_bar.setProperty("value", 55)

        self.output_file = main_forecast_file(self.forecast_file, self.kam, self.month, self.fx)

        self.progress_bar.setProperty("value", 100)


        print(self.output_file)

        self.save_directory = QtWidgets.QFileDialog.getSaveFileName(filter="*.xlsx")

        if not self.save_directory[0]:
            self.progress_bar.setProperty("value", 0)
            self.extract_button.setEnabled(True)
            return

        self.output_file.save(os.path.abspath(self.save_directory[0]))
        self.progress_bar.setProperty("value", 0)
        self.extract_button.setEnabled(True)

    def extract_summary(self):
        self.currency_enabled = self.currency_box.currentText()

        try:
            self.overhead = int(self.overhead_edit.text())
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Please only enter NUMBERS as overhead costs.")
            error_dialog.exec_()
            return

        if not self.overhead:  # For if nothing gets filled in, we just use 0 as default
            self.overhead = 0


        self.confirm_details = QtWidgets.QMessageBox()
        self.confirm_details.setIcon(QtWidgets.QMessageBox.Question)

        if self.currency_enabled == "Yes":
            try:
                self.fx = int(self.fx_edit.text())
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("Please only enter NUMBERS as FX Rate.")
                error_dialog.exec_()
                return

            self.confirm_details.setText(f"EXTRACTING SUMMARY\n\n"
                                         f"Overhead cost: {self.overhead}\n"
                                         f"Currency convert enabled\n"
                                         f"FX rate: {self.fx}\n\n"
                                         f"Continue?")
        else:
            self.fx = None
            self.confirm_details.setText(f"EXTRACTING SUMMARY\n\n"
                                         f"Overhead cost: {self.overhead}\n"
                                         f"Currency in JPY\n\n"
                                         f"Continue?")


        self.confirm_details.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.confirm_details_pressed = self.confirm_details.exec_()

        if self.confirm_details_pressed != QtWidgets.QMessageBox.Ok:
            return

        self.summary_button.setEnabled(False)

        time.sleep(1)

        self.progress_bar.setProperty("value", 55)

        # Summary file with everything pasted from the forecast file
        self.summary = create_summary(self.forecast_file, self.overhead, self.fx)

        self.progress_bar.setProperty("value", 70)
        time.sleep(1)
        self.progress_bar.setProperty("value", 100)
        print(self.summary)

        self.save_directory = QtWidgets.QFileDialog.getSaveFileName(filter="*.xlsx")

        if not self.save_directory[0]:
            self.progress_bar.setProperty("value", 0)
            self.extract_button.setEnabled(True)
            return

        self.summary.save(os.path.abspath(self.save_directory[0]))
        self.progress_bar.setProperty("value", 0)
        self.summary_button.setEnabled(True)

    def open_dashboard(self):
        self.FCWindow = QtWidgets.QMainWindow()
        self.ui = Ui_FCWindow()
        self.ui.setupUi(self.FCWindow, self.forecast_file)
        self.FCWindow.show()




if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    individual_forecast = QtWidgets.QMainWindow()
    ui = Ui_individual_forecast()
    ui.setupUi(individual_forecast)
    individual_forecast.show()
    sys.exit(app.exec_())
