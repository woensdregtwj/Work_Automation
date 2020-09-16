from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
import os

from Apps.SalesResultsVisuals.UpdateSalesDatabase import (
create_sales_db, UpdateSalesResultsTest
)

class Ui_SalesResultsUploadWindow(object):
    def setupUi(self, SalesResultsUploadWindow):
        SalesResultsUploadWindow.setObjectName("SalesResultsUploadWindow")
        SalesResultsUploadWindow.resize(1379, 620)
        SalesResultsUploadWindow.setMinimumSize(QtCore.QSize(1379, 620))
        SalesResultsUploadWindow.setMaximumSize(QtCore.QSize(1379, 620))
        self.centralwidget = QtWidgets.QWidget(SalesResultsUploadWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.example_picture = QtWidgets.QLabel(self.centralwidget)
        self.example_picture.setGeometry(QtCore.QRect(0, 360, 1381, 201))
        self.example_picture.setText("")
        self.example_picture.setPixmap(QtGui.QPixmap("../../Images/sales_results_new_example.png"))
        self.example_picture.setObjectName("example_picture")
        self.upload_box = QtWidgets.QGroupBox(self.centralwidget)
        self.upload_box.setGeometry(QtCore.QRect(9, 79, 621, 261))
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.upload_box.setFont(font)
        self.upload_box.setObjectName("upload_box")
        self.month_combobox = QtWidgets.QComboBox(self.upload_box)
        self.month_combobox.setGeometry(QtCore.QRect(20, 50, 171, 31))
        font = QtGui.QFont()
        font.setPixelSize(18)
        self.month_combobox.setFont(font)
        self.month_combobox.setObjectName("month_combobox")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_combobox.addItem("")
        self.month_label = QtWidgets.QLabel(self.upload_box)
        self.month_label.setGeometry(QtCore.QRect(230, 50, 291, 31))
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.month_label.setFont(font)
        self.month_label.setObjectName("month_label")
        self.upload1_lbutton = QtWidgets.QPushButton(self.upload_box)
        self.upload1_lbutton.setGeometry(QtCore.QRect(20, 100, 171, 61))
        font = QtGui.QFont()
        font.setPixelSize(18)
        self.upload1_lbutton.setFont(font)
        self.upload1_lbutton.setObjectName("upload1_lbutton")
        self.upload1_label = QtWidgets.QLabel(self.upload_box)
        self.upload1_label.setGeometry(QtCore.QRect(230, 110, 351, 31))
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.upload1_label.setFont(font)
        self.upload1_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.upload1_label.setObjectName("upload1_label")
        self.upload2_button = QtWidgets.QPushButton(self.upload_box)
        self.upload2_button.setGeometry(QtCore.QRect(20, 190, 171, 61))
        font = QtGui.QFont()
        font.setPixelSize(18)
        self.upload2_button.setFont(font)
        self.upload2_button.setObjectName("upload2_button")
        self.upload2_label = QtWidgets.QLabel(self.upload_box)
        self.upload2_label.setGeometry(QtCore.QRect(230, 200, 351, 31))
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.upload2_label.setFont(font)
        self.upload2_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.upload2_label.setObjectName("upload2_label")
        self.explanation_box = QtWidgets.QGroupBox(self.centralwidget)
        self.explanation_box.setGeometry(QtCore.QRect(650, 80, 721, 261))
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.explanation_box.setFont(font)
        self.explanation_box.setObjectName("explanation_box")
        self.explanation_browser = QtWidgets.QTextBrowser(self.explanation_box)
        self.explanation_browser.setGeometry(QtCore.QRect(30, 40, 671, 211))
        self.explanation_browser.setObjectName("explanation_browser")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(100, 0, 1281, 81))
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
        self.doehler_label = QtWidgets.QLabel(self.centralwidget)
        self.doehler_label.setGeometry(QtCore.QRect(0, 0, 101, 81))
        self.doehler_label.setText("")
        self.doehler_label.setPixmap(QtGui.QPixmap("../../Images/DoehlerLogo.png"))
        self.doehler_label.setScaledContents(True)
        self.doehler_label.setObjectName("doehler_label")
        SalesResultsUploadWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SalesResultsUploadWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1379, 18))
        self.menubar.setObjectName("menubar")
        SalesResultsUploadWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SalesResultsUploadWindow)
        self.statusbar.setObjectName("statusbar")
        SalesResultsUploadWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SalesResultsUploadWindow)
        QtCore.QMetaObject.connectSlotsByName(SalesResultsUploadWindow)

        self.upload1_lbutton.clicked.connect(self.upload_sales)

    def retranslateUi(self, SalesResultsUploadWindow):
        _translate = QtCore.QCoreApplication.translate
        SalesResultsUploadWindow.setWindowTitle(_translate("SalesResultsUploadWindow", "MainWindow"))
        self.upload_box.setTitle(_translate("SalesResultsUploadWindow", "Upload SAP file"))
        self.month_combobox.setItemText(0, _translate("SalesResultsUploadWindow", "Select"))
        self.month_combobox.setItemText(1, _translate("SalesResultsUploadWindow", "01"))
        self.month_combobox.setItemText(2, _translate("SalesResultsUploadWindow", "02"))
        self.month_combobox.setItemText(3, _translate("SalesResultsUploadWindow", "03"))
        self.month_combobox.setItemText(4, _translate("SalesResultsUploadWindow", "04"))
        self.month_combobox.setItemText(5, _translate("SalesResultsUploadWindow", "05"))
        self.month_combobox.setItemText(6, _translate("SalesResultsUploadWindow", "06"))
        self.month_combobox.setItemText(7, _translate("SalesResultsUploadWindow", "07"))
        self.month_combobox.setItemText(8, _translate("SalesResultsUploadWindow", "08"))
        self.month_combobox.setItemText(9, _translate("SalesResultsUploadWindow", "09"))
        self.month_combobox.setItemText(10, _translate("SalesResultsUploadWindow", "10"))
        self.month_combobox.setItemText(11, _translate("SalesResultsUploadWindow", "11"))
        self.month_combobox.setItemText(12, _translate("SalesResultsUploadWindow", "12"))
        self.month_label.setText(_translate("SalesResultsUploadWindow", "Month of sales result data"))
        self.upload1_lbutton.setText(_translate("SalesResultsUploadWindow", "Upload Sales Result"))
        self.upload1_label.setText(_translate("SalesResultsUploadWindow", "No file loaded..."))
        self.upload2_button.setText(_translate("SalesResultsUploadWindow", "Upload Budget"))
        self.upload2_label.setText(_translate("SalesResultsUploadWindow", "Optional..."))
        self.explanation_box.setTitle(_translate("SalesResultsUploadWindow", "Upload explanation"))
        self.explanation_browser.setHtml(_translate("SalesResultsUploadWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\">Please use the variables shown in the image below:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\">Filter</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Company code</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Rep. Customer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- B2B Level 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- B2B Level 2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Material (1-9)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\">Key Figures</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Sales Volume</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Gross Sales</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Net Sales Ex Works</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Standard GM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- Standard CM1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\">Period Structure</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- *1.000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt;\">- MM.YYYY &gt; 1 Month only</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600; text-decoration: underline;\">Have the columns ordered as shown in the image below</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600; text-decoration: underline;\">Be sure to have no cells merged. Unmerge all cells.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\'; font-size:18pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS UI Gothic\';\"><br /></p></body></html>"))
        self.app_title.setText(_translate("SalesResultsUploadWindow", "Doehler Japan - Upload Sales Results"))


    def upload_sales(self):

        # Making sure a month is selected
        self.month = self.month_combobox.currentText()
        if self.month == "Select":
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No month has been selected. Please select a month")
            error_dialog.show()
            error_dialog.exec_()
            return

        # Checking whether this month already is in the database. If it is, give the user the option to overwrite
        month_in = self.month_check()

        if month_in != 0:
            message_dialog = QtWidgets.QMessageBox()
            message_dialog.setText(f"{month_in} lines of data for month {self.month} are already in the database.\n"
                                   f"Do you want to overwrite these lines with new sales results data?")
            message_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            message_dialog_pressed = message_dialog.exec_()

            if message_dialog_pressed != QtWidgets.QMessageBox.Ok:
                message_dialog.setText(f"Upload canceled.")
                message_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
                message_dialog.exec_()
                return
            else:
                self.overwrite_month()  # If Ok was pressed, we overwrite.

        # Obtaining the file path from the file dialog
        self.sales_dir = QtWidgets.QFileDialog.getOpenFileName(filter="*xlsx")
        if not self.sales_dir[0]:
            self.upload1_label.setText("File was not selected.")
            self.upload1_label.setStyleSheet("background-color: rgb(255, 0, 0);")
            return

        self.sales_dir = os.path.abspath(self.sales_dir[0])
        self.upload1_label.setText(f"{os.path.basename(self.sales_dir)} is currently loaded")
        self.upload1_label.setStyleSheet("background-color: rgb(174, 217, 167);")

        # Testing the template of the file, whether it is eligible for upload to db
        # Todo - Connect the functions of UpdateSalesDatabase.py to here.
        template_test = UpdateSalesResultsTest(self.sales_dir, self.month)

        # template_test returns one of: "Header failed", "Header 2 failed", "Header 3 failed", dictionary of headers
        if isinstance(template_test, str):  # Test has failed if this gets read
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(f"There seems to be a mismatch in the template:\n"
                                     f"{template_test}")
            error_dialog.exec_()
            return

        #Test is OK, we received a dictionary value with the header co-ordinates.
        upload_to_db = create_sales_db(self.sales_dir, self.month, template_test)
        print("Exited the poop")
        print(upload_to_db)

        message_dialog = QtWidgets.QMessageBox()
        message_dialog.setText(f"Writing completed. {upload_to_db} new lines have been added to the database.")
        message_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        message_dialog.exec_()


    def month_check(self):
        connect = sqlite3.connect("..\\..\\Databases\\sales.db")
        c = connect.cursor()
        print('Connected to db')

        c.execute(f"SELECT COUNT(month) FROM sales WHERE month = '{self.month}'")
        print("Succesfully executed")

        data_amt = c.fetchall()
        print(data_amt[0][0])

        c.close()
        connect.close()

        return data_amt[0][0]

    def overwrite_month(self):

        connect = sqlite3.connect("..\\..\\Databases\\sales.db")
        c = connect.cursor()
        c.execute(f"DELETE FROM sales WHERE month = '{self.month}'")

        connect.commit()
        c.close()
        connect.close()