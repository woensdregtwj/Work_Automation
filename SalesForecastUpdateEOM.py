# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SalesForecastUpdate.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from SalesForecastUpdateEOMFunction import *
import datetime
import time

class Ui_forecast_EOM_window(object):
    def setup_fc_update(self, forecast_update_window):
        forecast_update_window.setObjectName("forecast_update_window")
        forecast_update_window.resize(800, 600)
        forecast_update_window.setMinimumSize(QtCore.QSize(800, 600))
        forecast_update_window.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(forecast_update_window)
        self.centralwidget.setObjectName("centralwidget")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(100, 0, 701, 81))
        self.app_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(32)
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 781, 451))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.upload_box = QtWidgets.QGroupBox(self.tab)
        self.upload_box.setGeometry(QtCore.QRect(20, 90, 731, 151))
        self.upload_box.setObjectName("upload_box")
        self.sforecast_button = QtWidgets.QPushButton(self.upload_box)
        self.sforecast_button.setGeometry(QtCore.QRect(30, 90, 211, 31))
        self.sforecast_button.setObjectName("sforecast_button")

        self.sresults_button = QtWidgets.QPushButton(self.upload_box)
        self.sresults_button.setGeometry(QtCore.QRect(30, 50, 211, 31))
        self.sresults_button.setObjectName("sresults_button")

        self.sforecast_label = QtWidgets.QLabel(self.upload_box)
        self.sforecast_label.setGeometry(QtCore.QRect(290, 90, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sforecast_label.setFont(font)
        self.sforecast_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sforecast_label.setObjectName("sforecast_label")
        self.sresults_label = QtWidgets.QLabel(self.upload_box)
        self.sresults_label.setGeometry(QtCore.QRect(290, 50, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sresults_label.setFont(font)
        self.sresults_label.setStyleSheet("border-color: rgb(160, 160, 160);")
        self.sresults_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sresults_label.setObjectName("sresults_label")
        self.month_label = QtWidgets.QLabel(self.tab)
        self.month_label.setGeometry(QtCore.QRect(20, 30, 291, 41))
        self.month_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.month_label.setObjectName("month_label")
        self.month_comboBox = QtWidgets.QComboBox(self.tab)
        self.month_comboBox.setGeometry(QtCore.QRect(200, 40, 101, 21))
        self.month_comboBox.setObjectName("month_comboBox")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.month_comboBox.addItem("")
        self.start_button = QtWidgets.QPushButton(self.tab)
        self.start_button.setGeometry(QtCore.QRect(50, 260, 211, 80))
        self.start_button.setObjectName("start_button")

        self.save_button = QtWidgets.QPushButton(self.tab)
        self.save_button.setGeometry(QtCore.QRect(50, 350, 211, 41))
        self.save_button.setObjectName("save_button")
        self.save_button.setText("Save updated file")
        self.save_button.setEnabled(False)

        self.progress_bar = QtWidgets.QProgressBar(self.tab)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setGeometry(QtCore.QRect(310, 390, 441, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_browser = QtWidgets.QTextBrowser(self.tab)
        self.progress_browser.setGeometry(QtCore.QRect(310, 300, 441, 81))
        self.progress_browser.setObjectName("progress_browser")
        self.errors_label = QtWidgets.QLabel(self.tab)
        self.errors_label.setGeometry(QtCore.QRect(310, 260, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errors_label.setFont(font)
        self.errors_label.setStyleSheet("border-color: rgb(160, 160, 160);")
        self.errors_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.errors_label.setObjectName("errors_label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.error_browser = QtWidgets.QTextBrowser(self.tab_3)
        self.error_browser.setGeometry(QtCore.QRect(10, 10, 761, 401))
        self.error_browser.setObjectName("error_browser")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.unmatched_browser = QtWidgets.QTextBrowser(self.tab_4)
        self.unmatched_browser.setGeometry(QtCore.QRect(10, 10, 761, 401))
        self.unmatched_browser.setObjectName("unmatched_browser")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.sales_browser = QtWidgets.QTextBrowser(self.tab_2)
        self.sales_browser.setGeometry(QtCore.QRect(10, 10, 761, 401))
        self.sales_browser.setObjectName("sales_browser")
        self.tabWidget.addTab(self.tab_2, "")
        forecast_update_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(forecast_update_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        forecast_update_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(forecast_update_window)
        self.statusbar.setObjectName("statusbar")
        forecast_update_window.setStatusBar(self.statusbar)

        self.retranslateUi(forecast_update_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(forecast_update_window)

        # Buttons clicked
        self.sresults_button.clicked.connect(self.upload_clicked)
        self.sforecast_button.clicked.connect(self.upload2_clicked)
        self.start_button.clicked.connect(self.start_update_clicked)
        self.save_button.clicked.connect(self.save_updated_forecast)

    def retranslateUi(self, forecast_update_window):
        _translate = QtCore.QCoreApplication.translate
        forecast_update_window.setWindowTitle(_translate("forecast_update_window", "forecast_update_window"))
        self.app_title.setText(_translate("forecast_update_window", "Sales Forecast End of Month"))
        self.upload_box.setTitle(_translate("forecast_update_window", "Upload Files"))
        self.sforecast_button.setText(_translate("forecast_update_window", "Upload Latest Forecast"))
        self.sresults_button.setText(_translate("forecast_update_window", "Upload EOM Sales"))
        self.sforecast_label.setText(_translate("forecast_update_window", "No Sales Forecast File Loaded"))
        self.sresults_label.setText(_translate("forecast_update_window", "No Sales Result File Loaded"))
        self.month_label.setText(_translate("forecast_update_window", "Sales Result Month"))
        self.month_comboBox.setItemText(0, _translate("forecast_update_window", "Jan"))
        self.month_comboBox.setItemText(1, _translate("forecast_update_window", "Feb"))
        self.month_comboBox.setItemText(2, _translate("forecast_update_window", "Mar"))
        self.month_comboBox.setItemText(3, _translate("forecast_update_window", "Apr"))
        self.month_comboBox.setItemText(4, _translate("forecast_update_window", "May"))
        self.month_comboBox.setItemText(5, _translate("forecast_update_window", "Jun"))
        self.month_comboBox.setItemText(6, _translate("forecast_update_window", "Jul"))
        self.month_comboBox.setItemText(7, _translate("forecast_update_window", "Aug"))
        self.month_comboBox.setItemText(8, _translate("forecast_update_window", "Sep"))
        self.month_comboBox.setItemText(9, _translate("forecast_update_window", "Oct"))
        self.month_comboBox.setItemText(10, _translate("forecast_update_window", "Nov"))
        self.month_comboBox.setItemText(11, _translate("forecast_update_window", "Dec"))
        self.start_button.setText(_translate("forecast_update_window", "Start Updating"))
        self.progress_browser.setHtml(_translate("forecast_update_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\';\">Update progress will appear here:</span></p></body></html>"))
        self.error_browser.setHtml(_translate("forecast_update_window",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\';\">Errors:</span></p></body></html>"))
        self.unmatched_browser.setHtml(_translate("forecast_update_window",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\';\">Unmatched lines:</span></p></body></html>"))
        self.sales_browser.setHtml(_translate("forecast_update_window",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\';\">Sales data:</span></p></body></html>"))
        self.errors_label.setText(_translate("forecast_update_window", "Error message will appear here."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("forecast_update_window", "Updater"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("forecast_update_window", "Errors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("forecast_update_window", "Unmatched Sales"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("forecast_update_window", "Raw Sales Data"))

    def upload_clicked(self):
        self.result_filepath = QtWidgets.QFileDialog.getOpenFileName(filter="*.xlsx")

        if not self.result_filepath[0]:
            self.sresults_label.setText("Loading canceled, please select a file.")
            self.sresults_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.sresults_label.setText(f"Loaded: {os.path.basename(self.result_filepath[0])}")
            self.sresults_label.setStyleSheet("background-color: rgb(174, 217, 167);")
            self.result_filepath = os.path.abspath(self.result_filepath[0])

    def upload2_clicked(self):
        self.forecast_filepath = QtWidgets.QFileDialog.getOpenFileName(filter="*.xlsx")

        if not self.forecast_filepath[0]:
            self.sforecast_label.setText("Loading canceled, please select a file.")
            self.sforecast_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.sforecast_label.setText(f"Loaded: {os.path.basename(self.forecast_filepath[0])}")
            self.sforecast_label.setStyleSheet("background-color: rgb(174, 217, 167);")
            self.forecast_filepath = os.path.abspath(self.forecast_filepath[0])

    def start_update_clicked(self):
        self.start_button.setEnabled(False)

        self.reporting_month = self.month_comboBox.currentText()

        self.report_month_confirm = QtWidgets.QMessageBox()
        self.report_month_confirm.setIcon(QtWidgets.QMessageBox.Question)
        self.report_month_confirm.setText(f"You are about to update the forecast for:\n"
                                          f"{self.reporting_month.center(41)}\n\n"
                                          f"If correct, press 'Ok'")

        self.report_month_confirm.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.report_month_confirm_button = self.report_month_confirm.exec_()

        if self.report_month_confirm_button != QtWidgets.QMessageBox.Ok:
            self.start_button.setEnabled(True)
            return

        self.update_text = f"Starting Forecast Update for {self.reporting_month}\n"
        self.progress_browser.setText(self.update_text)

        try:
            self.progress_update("Sales Results")  # updating text browser

            self.sales_forecast_info = UploadEOMResults(self.result_filepath, self.forecast_filepath, self.reporting_month)  # Calling function from other file
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Please be sure to have the correct files uploaded!")

            self.sresults_label.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.sforecast_label.setStyleSheet("background-color: rgb(255, 0, 0);")

            error_dialog.exec_()
            self.start_button.setEnabled(True)
            self.progress_bar.setProperty("value", 0)
            return

        self.progress_update("Sales Results OK")  # updating text browser
        self.progress_update("Forecast")
        self.progress_update("Forecast OK")
        print("A")
        pprint.pprint(self.sales_forecast_info[1])
        print("B")

        self.progress_update("Inventory Delivery")
        self.progress_update("Trade Business")
        self.progress_update("Storage Delivery Trade")
        self.progress_update("Done")

        if self.sales_forecast_info[3]:
            print(self.sales_forecast_info[3])
            self.errors_label.setText("Non-critical error found, please revise in the \"Errors\" tab")
            self.errors_label.setStyleSheet("background-color: rgb(255, 0, 0); border-color: rgb(160, 160, 160);")

        print(len(self.sales_forecast_info))
        print(self.sales_forecast_info[4])

        self.error_browser.append(pprint.pformat(self.sales_forecast_info[3]))

        self.unmatched_browser.append(pprint.pformat(self.sales_forecast_info[1]))
        #for key, value in self.sales_forecast_info[1].items():
            #self.unmatched_browser.append(f"""<p style="font-size:12pt">{str(key)}: {str(value)}</p>""")

        self.unmatched_browser.append((f"\nTRADE BUSINESS:"))
        for key, value in self.sales_forecast_info[2].items(): #Printing each line nicely
            self.unmatched_browser.append(f"""{str(key)}: {str(value)}""")

        self.sales_browser.append(pprint.pformat(self.sales_forecast_info[0]))

        # Clearing the data for if we want to update again
        sales_data = None
        storage_delivery_trade = None
        trade_business_error = None

        # self.progress_update("Forecast")
        #
        # self.raw_unmatched_data = UploadSalesForecast(self.forecast_filepath)
        # self.progress_update("Forecast OK")
        #
        # print("A")
        # pprint.pprint(self.raw_unmatched_data)
        # print("B")
        # print(type(self.raw_unmatched_data))
        #
        # self.raw_unmatched_data = DeliveryInventory(self.raw_unmatched_data)
        # self.progress_update("Inventory Delivery")
        # pprint.pprint(self.raw_unmatched_data)
        # print("C")
        #
        # TradeBusiness(self.raw_unmatched_data)
        # self.progress_update("Trade Business")
        # pprint.pprint(self.raw_unmatched_data)
        # print("D")
        #
        # if trade_business_error:
        #     print(trade_business_error)
        #     self.errors_label.setText("Non-critical error found, please revise in the \"Errors\" tab")
        #     self.errors_label.setStyleSheet("background-color: rgb(255, 0, 0); border-color: rgb(160, 160, 160);")
        #
        # self.progress_update("Storage Delivery Trade")
        # storageDeliveryTrade()
        #
        # self.progress_update("Done")

    def progress_update(self, progressline):
        self.progressline = progressline
        if self.progressline == "Sales Results":
            self.progress_bar.setProperty("value", 1)
            self.update_text = f"Reading into Sales Result file..."
            time.sleep(0.5)
        elif self.progressline == "Sales Results OK":
            self.progress_bar.setProperty("value", 30)
            self.update_text = f"Reading succesfully completed...\nRaw sales data succesfully copied..."
            time.sleep(0.5)
        elif self.progressline == "Forecast":
            self.progress_bar.setProperty("value", 45)
            self.update_text = f"Reading into file Forecast file..."
            time.sleep(0.5)
        elif self.progressline == "Forecast OK":
            self.progress_bar.setProperty("value", 60)
            self.update_text = f"Reading succesfully completed...\nSuccesfully updated MTD column..."
            time.sleep(0.5)
        elif self.progressline == "Inventory Delivery":
            self.progress_bar.setProperty("value", 72)
            self.update_text = f"Calculating inventory and delivery...\nSuccesfully calculated inventory and delivery..."
            time.sleep(0.5)
        elif self.progressline == "Trade Business":
            self.update_text = f"Calculating trade business..."
            self.progress_bar.setProperty("value", 84)
            time.sleep(0.5)
        elif self.progressline == "Storage Delivery Trade":
            self.progress_bar.setProperty("value", 90)
            self.update_text = f"Trade business calculated succesfully...\nPasting storage/delivery and trade business..."
            time.sleep(0.5)
        elif self.progressline == "Formatting":
            self.progress_bar.setProperty("value", 95)
            self.update_text = f"Formatting file for next month..."
            time.sleep(0.5)
        elif self.progressline == 'Done':
            self.progress_bar.setProperty("value", 100)
            self.update_text = "\n\n\nForecast updated, press the Save button to save!"
            self.progress_browser.append(self.update_text)

            self.update_text = "Be sure to save it as the new month!"
            self.save_button.setEnabled(True)
            self.start_button.setEnabled(False)

        self.progress_browser.append(self.update_text)

    def save_updated_forecast(self):
        self.save_updated_xlsx = QtWidgets.QFileDialog.getSaveFileName(filter="*.xlsx")

        if not self.save_updated_xlsx[0]:
            return

        try:
            self.sales_forecast_info[4].save(os.path.abspath(self.save_updated_xlsx[0]))
        except:
            self.update_text = "\n\n\nSAVE FAILED, BE SURE TO HAVE NO OPEN SIMILAR FILES"
            self.progress_browser.append(self.update_text)
            return

        self.update_text = "\n\n\nSAVE COMPLETE"
        self.sales_forecast_info = None
        self.progress_browser.append(self.update_text)

        self.save_button.setEnabled(False)
        self.start_button.setEnabled(True)

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    forecast_update_window = QtWidgets.QMainWindow()
    ui = Ui_forecast_EOM_window()
    ui.setup_fc_update(forecast_update_window)
    forecast_update_window.show()
    sys.exit(app.exec_())
