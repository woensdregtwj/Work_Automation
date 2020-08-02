# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgingList.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
import os
from AgingListFunction import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QtCore.QSize(900, 500))
        MainWindow.setMaximumSize(QtCore.QSize(900, 500))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(0, 0, 101, 81))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("Images/DoehlerLogo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")

        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(0, 0, 901, 81))
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

        self.database_box = QtWidgets.QGroupBox(self.centralwidget)
        self.database_box.setGeometry(QtCore.QRect(400, 90, 491, 371))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.database_box.setFont(font)
        self.database_box.setObjectName("database_box")
        self.database_table = QtWidgets.QTableView(self.database_box)
        self.database_table.setGeometry(QtCore.QRect(10, 70, 471, 291))
        self.database_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.database_table.setObjectName("database_table")

        self.remove_button = QtWidgets.QPushButton(self.database_box)
        self.remove_button.setGeometry(QtCore.QRect(385, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")

        self.find_lineedit = QtWidgets.QLineEdit(self.database_box)
        self.find_lineedit.setGeometry(QtCore.QRect(120, 30, 151, 31))
        self.find_lineedit.setObjectName("find_lineedit")

        self.add_button = QtWidgets.QPushButton(self.database_box)
        self.add_button.setGeometry(QtCore.QRect(280, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")

        self.find_label = QtWidgets.QLabel(self.database_box)
        self.find_label.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.find_label.setFont(font)
        self.find_label.setObjectName("find_label")

        self.extract_box = QtWidgets.QGroupBox(self.centralwidget)
        self.extract_box.setGeometry(QtCore.QRect(19, 89, 371, 371))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.extract_box.setFont(font)
        self.extract_box.setObjectName("extract_box")

        self.upload_button = QtWidgets.QPushButton(self.extract_box)
        self.upload_button.setGeometry(QtCore.QRect(20, 140, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.upload_button.setFont(font)
        self.upload_button.setObjectName("upload_button")

        self.month_combobox = QtWidgets.QComboBox(self.extract_box)
        self.month_combobox.setGeometry(QtCore.QRect(20, 40, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
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
        self.type_combobox = QtWidgets.QComboBox(self.extract_box)
        self.type_combobox.setGeometry(QtCore.QRect(20, 90, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.type_combobox.setFont(font)
        self.type_combobox.setObjectName("type_combobox")
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")

        self.month_label = QtWidgets.QLabel(self.extract_box)
        self.month_label.setGeometry(QtCore.QRect(140, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.month_label.setFont(font)
        self.month_label.setObjectName("month_label")
        self.type_label = QtWidgets.QLabel(self.extract_box)
        self.type_label.setGeometry(QtCore.QRect(140, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")

        self.save_button = QtWidgets.QPushButton(self.extract_box)
        self.save_button.setGeometry(QtCore.QRect(20, 280, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.save_button.setEnabled(False)

        self.upload_label = QtWidgets.QLabel(self.extract_box)
        self.upload_label.setGeometry(QtCore.QRect(20, 220, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.upload_label.setFont(font)
        self.upload_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upload_label.setObjectName("upload_label")
        self.app_title.raise_()
        self.logo_label.raise_()
        self.database_box.raise_()
        self.extract_box.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.upload_button.clicked.connect(self.upload_aging)
        self.save_button.clicked.connect(self.save_aging)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_title.setText(_translate("MainWindow", "BW Aging List"))
        self.database_box.setTitle(_translate("MainWindow", "Payment Terms Database"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.find_label.setText(_translate("MainWindow", "Find customer ID:"))
        self.extract_box.setTitle(_translate("MainWindow", "File Extract"))
        self.upload_button.setText(_translate("MainWindow", "Upload GX File"))
        self.month_combobox.setItemText(0, _translate("MainWindow", "Jan"))
        self.month_combobox.setItemText(1, _translate("MainWindow", "Feb"))
        self.month_combobox.setItemText(2, _translate("MainWindow", "Mar"))
        self.month_combobox.setItemText(3, _translate("MainWindow", "Apr"))
        self.month_combobox.setItemText(4, _translate("MainWindow", "May"))
        self.month_combobox.setItemText(5, _translate("MainWindow", "Jun"))
        self.month_combobox.setItemText(6, _translate("MainWindow", "Jul"))
        self.month_combobox.setItemText(7, _translate("MainWindow", "Aug"))
        self.month_combobox.setItemText(8, _translate("MainWindow", "Sep"))
        self.month_combobox.setItemText(9, _translate("MainWindow", "Oct"))
        self.month_combobox.setItemText(10, _translate("MainWindow", "Nov"))
        self.month_combobox.setItemText(11, _translate("MainWindow", "Dec"))
        self.type_combobox.setItemText(0, _translate("MainWindow", "Monthly"))
        self.type_combobox.setItemText(1, _translate("MainWindow", "Daily"))
        self.month_label.setText(_translate("MainWindow", "Reporting Month"))
        self.type_label.setText(_translate("MainWindow", "Reporting Type"))
        self.save_button.setText(_translate("MainWindow", "Save Formatted File"))
        self.upload_label.setText(_translate("MainWindow", "Please upload 142 Accounts Receivable  細目残高一覧"))

    def upload_aging(self):
        self.aging_file = QtWidgets.QFileDialog.getOpenFileName(filter="*.xlsx")

        if not self.aging_file[0]:
            self.upload_label.setStyleSheet("background-color: rgb(255, 0, 0);")
            return
        print(self.aging_file[0])

        self.upload_label.setText(f"Loaded file: {os.path.basename(self.aging_file[0])}")
        self.upload_label.setStyleSheet("background-color: rgb(174, 217, 167);")

        # Grabbing the inputs from the combobox and will show this in a confirmation message box
        self.reporting_month = self.month_combobox.currentText()
        self.reporting_type = self.type_combobox.currentText()

        # Confirmation Message Box
        self.confirm_input = QtWidgets.QMessageBox()
        self.confirm_input.setIcon(QtWidgets.QMessageBox.Question)
        self.confirm_input.setText(f"Reporting File: '{os.path.basename(self.aging_file[0])}'\n"
                                   f"Reporting Month: '{self.reporting_month}'\n"
                                   f"Reporting Type: '{self.reporting_type}'\n\n"
                                   f"Continue?")
        self.confirm_input.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.confirm_input_pressed = self.confirm_input.exec_()

        # Confirmation user response
        if self.confirm_input_pressed != QtWidgets.QMessageBox.Ok:
            self.upload_label.setText("Please upload 142 Accounts Receivable  細目残高一覧")
            self.upload_label.setStyleSheet("background-color: rgb(255, 255, 255);")
            return  # Canceling as user pressed Cancel

        self.upload_button.setEnabled(False)

        try:
            self.aging_file_formatted = convert_aging_list(self.aging_file[0], self.reporting_month, self.reporting_type)
        except:
            unknown_error = QtWidgets.QErrorMessage()
            unknown_error.showMessage("An unknown error has occured while formatting the file. Please debug the code.")

        # If the 'return' is a string, then we know the format test has failed at some area. We write this in a dialog.
        if isinstance(self.aging_file_formatted, str):
            print("A string has returned, setting up a error dialog box")
            error_dialog = QtWidgets.QErrorMessage()
            font = QtGui.QFont()
            font.setPointSize(15)
            error_dialog.setFont(font)
            error_dialog.showMessage(self.aging_file_formatted)
            error_dialog.exec_()

            self.upload_button.setEnabled(True)
            self.upload_label.setText("Please upload 142 Accounts Receivable  細目残高一覧")
            self.upload_label.setStyleSheet("background-color: rgb(255, 255, 255);")
            return

        self.upload_label.setText("Succesfully formatted. --PRESS BELOW TO SAVE--")
        self.upload_label.setStyleSheet("background-color: rgb(174, 200, 167);")
        self.save_button.setEnabled(True)


        # If all is ok, then the self.aging_file_formatted returns the new workbook with the new format

    def save_aging(self):
        self.save_dir = QtWidgets.QFileDialog.getSaveFileName(filter="*.xlsx")

        if not self.save_dir[0]:
            self.upload_label.setText("File not saved. Press below again.")

        self.upload_button.setEnabled(True)

        self.aging_file_formatted.save(self.save_dir[0])

        self.upload_label.setText("Succesfully saved.")
        self.upload_button.setEnabled(True)
        self.save_button.setEnabled(False)











if __name__ == "__main__":
    import sys

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
