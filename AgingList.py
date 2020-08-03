# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgingList.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
import sqlite3
from pathlib import Path
import pprint
import os
from AgingListFunction import *

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("Databases\\payment_terms.db")
db.open()


class Ui_AgingWindow(object):
    def setupUi(self, AgingWindow):
        AgingWindow.setObjectName("MainWindow")
        AgingWindow.resize(900, 500)
        AgingWindow.setMinimumSize(QtCore.QSize(900, 500))
        AgingWindow.setMaximumSize(QtCore.QSize(900, 500))

        self.centralwidget = QtWidgets.QWidget(AgingWindow)
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

        self.database_box = QtWidgets.QGroupBox(self.centralwidget)
        self.database_box.setGeometry(QtCore.QRect(400, 90, 491, 371))
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.database_box.setFont(font)
        self.database_box.setObjectName("database_box")
        self.database_table = QtWidgets.QTableView(self.database_box)
        self.database_table.setGeometry(QtCore.QRect(10, 70, 471, 291))
        self.database_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.database_table.setObjectName("database_table")

        self.remove_button = QtWidgets.QPushButton(self.database_box)
        self.remove_button.setGeometry(QtCore.QRect(385, 30, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(16)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")

        self.find_lineedit = QtWidgets.QLineEdit(self.database_box)
        self.find_lineedit.setGeometry(QtCore.QRect(120, 30, 151, 31))
        self.find_lineedit.setObjectName("find_lineedit")

        self.add_button = QtWidgets.QPushButton(self.database_box)
        self.add_button.setGeometry(QtCore.QRect(280, 30, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(16)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")

        self.find_label = QtWidgets.QLabel(self.database_box)
        self.find_label.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setPixelSize(12)
        self.find_label.setFont(font)
        self.find_label.setObjectName("find_label")

        self.extract_box = QtWidgets.QGroupBox(self.centralwidget)
        self.extract_box.setGeometry(QtCore.QRect(19, 89, 371, 371))
        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.extract_box.setFont(font)
        self.extract_box.setObjectName("extract_box")

        self.upload_button = QtWidgets.QPushButton(self.extract_box)
        self.upload_button.setGeometry(QtCore.QRect(20, 140, 341, 61))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.upload_button.setFont(font)
        self.upload_button.setObjectName("upload_button")

        self.month_combobox = QtWidgets.QComboBox(self.extract_box)
        self.month_combobox.setGeometry(QtCore.QRect(20, 40, 81, 22))
        font = QtGui.QFont()
        font.setPixelSize(16)
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
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.type_combobox.setFont(font)
        self.type_combobox.setObjectName("type_combobox")
        self.type_combobox.addItem("")
        self.type_combobox.addItem("")

        self.month_label = QtWidgets.QLabel(self.extract_box)
        self.month_label.setGeometry(QtCore.QRect(140, 40, 131, 21))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.month_label.setFont(font)
        self.month_label.setObjectName("month_label")
        self.type_label = QtWidgets.QLabel(self.extract_box)
        self.type_label.setGeometry(QtCore.QRect(140, 90, 131, 21))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")

        self.save_button = QtWidgets.QPushButton(self.extract_box)
        self.save_button.setGeometry(QtCore.QRect(20, 280, 341, 61))
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.save_button.setEnabled(False)

        self.upload_label = QtWidgets.QLabel(self.extract_box)
        self.upload_label.setGeometry(QtCore.QRect(20, 220, 341, 31))
        font = QtGui.QFont()
        font.setPixelSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.upload_label.setFont(font)
        self.upload_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upload_label.setObjectName("upload_label")
        self.app_title.raise_()
        self.logo_label.raise_()
        self.database_box.raise_()
        self.extract_box.raise_()

        AgingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AgingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 18))
        self.menubar.setObjectName("menubar")
        AgingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AgingWindow)
        self.statusbar.setObjectName("statusbar")
        AgingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AgingWindow)
        QtCore.QMetaObject.connectSlotsByName(AgingWindow)

        # Loading database into table
        self.model = QSqlTableModel(db=db)
        self.model.setTable("terms")

        self.query = QSqlQuery(db=db)

        self.query.prepare("SELECT * FROM terms ORDER BY term")
        self.query.exec_()
        self.model.setQuery(self.query)

        self.database_table.setModel(self.model)
        self.database_table.resizeColumnsToContents()

        # Buttons clicked actions
        self.upload_button.clicked.connect(self.upload_aging)
        self.save_button.clicked.connect(self.save_aging)
        self.remove_button.clicked.connect(self.remove_term)
        self.add_button.clicked.connect(self.add_term)

        self.find_lineedit.returnPressed.connect(self.find_payment_term)

    def retranslateUi(self, AgingWindow):
        _translate = QtCore.QCoreApplication.translate
        AgingWindow.setWindowTitle(_translate("AgingWindow", "MainWindow"))
        self.app_title.setText(_translate("AgingWindow", "BW Aging List"))
        self.database_box.setTitle(_translate("AgingWindow", "Payment Terms Database"))
        self.remove_button.setText(_translate("AgingWindow", "Remove"))
        self.add_button.setText(_translate("AgingWindow", "Add"))
        self.find_label.setText(_translate("AgingWindow", "Find customer ID:"))
        self.extract_box.setTitle(_translate("AgingWindow", "File Extract"))
        self.upload_button.setText(_translate("AgingWindow", "Upload GX File"))
        self.month_combobox.setItemText(0, _translate("AgingWindow", "Jan"))
        self.month_combobox.setItemText(1, _translate("AgingWindow", "Feb"))
        self.month_combobox.setItemText(2, _translate("AgingWindow", "Mar"))
        self.month_combobox.setItemText(3, _translate("AgingWindow", "Apr"))
        self.month_combobox.setItemText(4, _translate("AgingWindow", "May"))
        self.month_combobox.setItemText(5, _translate("AgingWindow", "Jun"))
        self.month_combobox.setItemText(6, _translate("AgingWindow", "Jul"))
        self.month_combobox.setItemText(7, _translate("AgingWindow", "Aug"))
        self.month_combobox.setItemText(8, _translate("AgingWindow", "Sep"))
        self.month_combobox.setItemText(9, _translate("AgingWindow", "Oct"))
        self.month_combobox.setItemText(10, _translate("AgingWindow", "Nov"))
        self.month_combobox.setItemText(11, _translate("AgingWindow", "Dec"))
        self.type_combobox.setItemText(0, _translate("AgingWindow", "Monthly"))
        self.type_combobox.setItemText(1, _translate("AgingWindow", "Daily"))
        self.month_label.setText(_translate("AgingWindow", "Reporting Month"))
        self.type_label.setText(_translate("AgingWindow", "Reporting Type"))
        self.save_button.setText(_translate("AgingWindow", "Save Formatted File"))
        self.upload_label.setText(_translate("AgingWindow", "Please upload 142 Accounts Receivable  細目残高一覧"))

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
            self.aging_file_formatted = convert_aging_list(self.aging_file[0], self.reporting_month,
                                                           self.reporting_type)
        except:
            unknown_error = QtWidgets.QErrorMessage()
            unknown_error.showMessage("An unknown error has occured while formatting the file. Please debug the code.")

        # If the 'return' is a string, then we know the format test has failed at some area. We write this in a dialog.
        if isinstance(self.aging_file_formatted[0], str):
            print("A string has returned, setting up a error dialog box")
            error_dialog = QtWidgets.QErrorMessage()
            font = QtGui.QFont()
            font.setPixelSize(15)
            error_dialog.setFont(font)
            error_dialog.showMessage(self.aging_file_formatted[0])
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

        self.aging_file_formatted[0].save(self.save_dir[0])

        # Saving the unmatched terms as a txt for reference if there are any unmatched.
        if self.aging_file_formatted[1]:
            with open(f"{os.path.dirname(self.save_dir[0])}\\{Path(self.save_dir[0]).stem} - Unmatched.txt", 'w') as f:
                f.write(pprint.pformat(self.aging_file_formatted[1]))

        self.upload_label.setText("Succesfully saved.")
        self.upload_button.setEnabled(True)
        self.save_button.setEnabled(False)

    def find_payment_term(self):
        find = self.find_lineedit.text()

        if not self.find_lineedit.text():
            self.query.prepare("SELECT * FROM terms ORDER BY term")
        else:
            self.query.prepare(f"SELECT * FROM terms WHERE id LIKE '%{find}%' OR customer LIKE '%{find}%'")

        self.query.exec_()
        self.model.setQuery(self.query)
        self.database_table.resizeColumnsToContents()

    def remove_term(self):
        self.remove_term = QtWidgets.QInputDialog()
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.remove_term.setFont(font)
        delete_id, confirmed = self.remove_term.getText(None, "Remove customer ID", "Enter the customer ID for "
                                                                                    "removing:")

        if not confirmed:
            print("Removing canceled")
            return

        self.confirm_deletion = QtWidgets.QMessageBox()
        self.confirm_deletion.setText(f"You are about to delete customer {delete_id}\n"
                                      f"Continue?")
        self.confirm_deletion.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.confirm_deletion_result = self.confirm_deletion.exec_()

        if self.confirm_deletion_result != QtWidgets.QMessageBox.Ok:
            self.confirm_deletion.setText("Aborted")
            self.confirm_deletion.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.confirm_deletion.exec_()
            return

        connect = sqlite3.connect("Databases\\payment_terms.db")
        c = connect.cursor()

        c.execute("SELECT id FROM terms")
        existing_id = c.fetchall()

        # Have to search for id as Tuple, as the existing_id is a list of tuples.
        if (delete_id,) not in existing_id:  # If ID not in current data, report to user.
            self.confirm_deletion.setText(f"There is no customer with ID {delete_id}. Remove canceled.")
            self.confirm_deletion.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.confirm_deletion.exec_()
        else:  # ID exists, deleting from database
            c.execute("DELETE FROM terms WHERE id = ?", (delete_id,))
            connect.commit()
            self.confirm_deletion.setText(f"Succesfully deleted customer {delete_id}.")
            self.confirm_deletion.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.confirm_deletion.exec_()

        c.close()
        connect.close()


    def add_term(self):
        self.AddWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self.AddWindow)
        self.AddWindow.show()


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(509, 124)
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.customer_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPixelSize(14)
        self.customer_label.setFont(font)
        self.customer_label.setObjectName("customer_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.customer_label)
        self.customerNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.customerNameLineEdit.setObjectName("customerNameLineEdit")
        self.customerNameLineEdit.setFont(font)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.customerNameLineEdit)
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPixelSize(14)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.id_label)
        self.customerIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.customerIDLineEdit.setFont(font)
        self.customerIDLineEdit.setObjectName("customerIDLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.customerIDLineEdit)
        self.term_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPixelSize(14)
        self.term_label.setFont(font)
        self.term_label.setObjectName("term_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.term_label)
        self.paymentTermLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.paymentTermLineEdit.setFont(font)
        self.paymentTermLineEdit.setObjectName("paymentTermLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.paymentTermLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        AddWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 18))
        self.menubar.setObjectName("menubar")
        AddWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ok_button)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

        self.ok_button.clicked.connect(self.add_data)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "AddWindow"))
        self.customer_label.setText(_translate("AddWindow", "Customer Name"))
        self.id_label.setText(_translate("AddWindow", "Customer ID"))
        self.term_label.setText(_translate("AddWindow", "Payment Term"))
        self.ok_button.setText(_translate("AddWindow", "Click to add new payment terms data"))

    def add_data(self):
        customer = self.customerNameLineEdit.text()
        customer_id = self.customerIDLineEdit.text()
        payment_term = self.paymentTermLineEdit.text()

        new_data = [customer, customer_id, payment_term]

        # Checking whether ID and TERM are integers
        try:
            int(customer_id)
            int(payment_term)
        except ValueError:
            self.none_error = QtWidgets.QErrorMessage()
            self.none_error.showMessage("For Customer ID or Payment Term, please only fill in numbers.")
            return

        # Checking whether nothing had been filled into the form
        if "" in [customer, customer_id, payment_term]:
            self.none_error = QtWidgets.QErrorMessage()
            self.none_error.showMessage("You have to fill in all boxes. Please try again.")
            return

        # Final confirmation to the user
        self.confirm_message = QtWidgets.QMessageBox()
        self.confirm_message.setText(f"You are about to add the following to the database:\n"
                                     f"Customer Name: {customer}\n"
                                     f"customer ID: {customer_id}\n"
                                     f"Payment Term: {payment_term} days\n\n"
                                     f"Proceed?")
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.confirm_message.setFont(font)
        self.confirm_message.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Discard)

        self.confirm_data = self.confirm_message.exec_()
        if self.confirm_data != QtWidgets.QMessageBox.Ok:
            return

        connect = sqlite3.connect("Databases\\payment_terms.db")
        c = connect.cursor()

        # First checking whether the inserted ID already exists. If it does, we do not want to add it in the db
        c.execute(f"SELECT * FROM terms WHERE id = ?", (customer_id,))
        existing_data = c.fetchall()

        if existing_data:
            self.already_exists_error = QtWidgets.QErrorMessage()
            self.already_exists_error.setFont(font)
            self.already_exists_error.showMessage(f"This customer ID already exists:\n"
                                                  f"{existing_data}\n\n"
                                                  f"Edit the data in the main field.")
            c.close()
            connect.close()
            return

        c.execute("INSERT INTO terms VALUES (?, ?, ?)", new_data)
        connect.commit()

        c.close()
        connect.close()

        self.confirm_message.setText("Succesfully added!")
        self.confirm_message.exec_()
        self.customerIDLineEdit.setText("")
        self.customerNameLineEdit.setText("")
        self.paymentTermLineEdit.setText("")



if __name__ == "__main__":
    import sys

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    AgingWindow = QtWidgets.QMainWindow()
    ui = Ui_AgingWindow()
    ui.setupUi(AgingWindow)
    AgingWindow.show()
    sys.exit(app.exec_())
