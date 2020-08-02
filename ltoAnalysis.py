# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ltoSQLTableEnlarged.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os
from LTODateConverterFunction import *
from UpdateLTODatabase import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
import sqlite3

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("Databases\\LTO.db")
db.open()

class Ui_lto_database(object):
    def setupUi(self, lto_database):
        lto_database.setObjectName("lto_database")
        lto_database.resize(1600, 805)
        lto_database.setMinimumSize(QtCore.QSize(1600, 800))
        lto_database.setMaximumSize(QtCore.QSize(16777215, 16777215))
        lto_database.setStyleSheet("background-color: rgb(0, 40, 72);")
        self.centralwidget = QtWidgets.QWidget(lto_database)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1601, 80))
        self.frame.setStyleSheet("background-color: rgb(0, 35, 72);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.logo_label = QtWidgets.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(0, 0, 101, 81))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("Images/DoehlerLogo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.app_title = QtWidgets.QLabel(self.frame)
        self.app_title.setGeometry(QtCore.QRect(100, 0, 1491, 81))
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
        self.verticalLayout.addWidget(self.frame)
        self.actions_frame = QtWidgets.QFrame(self.centralwidget)
        self.actions_frame.setMinimumSize(QtCore.QSize(1601, 71))
        self.actions_frame.setStyleSheet("background-color: rgb(0, 40, 72);")
        self.actions_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.actions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actions_frame.setObjectName("actions_frame")
        self.query_lineedit = QtWidgets.QLineEdit(self.actions_frame)
        self.query_lineedit.setGeometry(QtCore.QRect(10, 30, 711, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.query_lineedit.setFont(font)
        self.query_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.query_lineedit.setObjectName("query_lineedit")
        self.query_label = QtWidgets.QLabel(self.actions_frame)
        self.query_label.setGeometry(QtCore.QRect(10, 0, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.query_label.setFont(font)
        self.query_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.query_label.setObjectName("query_label")

        self.visualize_button = QtWidgets.QPushButton(self.actions_frame)
        self.visualize_button.setGeometry(QtCore.QRect(850, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.visualize_button.setFont(font)
        self.visualize_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(0, 111, 196);")
        self.visualize_button.setObjectName("visualize_button")

        self.extract_button = QtWidgets.QPushButton(self.actions_frame)
        self.extract_button.setGeometry(QtCore.QRect(740, 10, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.extract_button.setFont(font)
        self.extract_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(0, 111, 196);")
        self.extract_button.setObjectName("visualize_button")

        self.update_button = QtWidgets.QPushButton(self.actions_frame)
        self.update_button.setGeometry(QtCore.QRect(1040, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.update_button.setFont(font)
        self.update_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 111, 196);")
        self.update_button.setObjectName("update_button")
        self.update_label = QtWidgets.QLabel(self.actions_frame)
        self.update_label.setEnabled(True)
        self.update_label.setGeometry(QtCore.QRect(1230, 20, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update_label.setFont(font)
        self.update_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(0, 85, 127);")
        self.update_label.setObjectName("update_label")
        self.tableload_label = QtWidgets.QLabel(self.actions_frame)
        self.tableload_label.setGeometry(QtCore.QRect(570, 0, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.tableload_label.setFont(font)
        self.tableload_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.tableload_label.setObjectName("tableload_label")
        self.verticalLayout.addWidget(self.actions_frame)
        self.table_data = QtWidgets.QTableView()
        self.table_data.setMinimumSize(QtCore.QSize(1581, 611))
        self.table_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_data.setObjectName("table_data")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.table_data.setFont(font)
        self.verticalLayout.addWidget(self.table_data)
        lto_database.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lto_database)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 18))
        self.menubar.setObjectName("menubar")
        lto_database.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lto_database)
        self.statusbar.setObjectName("statusbar")
        lto_database.setStatusBar(self.statusbar)

        self.retranslateUi(lto_database)
        QtCore.QMetaObject.connectSlotsByName(lto_database)

        self.model = QSqlTableModel(db=db)
        self.model.setTable("lto")
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        self.query = QSqlQuery(db=db)
        self.query.prepare("SELECT * FROM lto ORDER BY launch") # setSort does not working, have to do through Query
        self.query.exec_()
        self.model.setQuery(self.query)

        self.table_data.setModel(self.model)
        self.table_data.resizeColumnsToContents()

        self.update_button.clicked.connect(self.update_lto_clicked)
        self.query_lineedit.returnPressed.connect(self.update_query)

    def retranslateUi(self, lto_database):
        _translate = QtCore.QCoreApplication.translate
        lto_database.setWindowTitle(_translate("lto_database", "MainWindow"))
        self.app_title.setText(_translate("lto_database", "LTO Analysis - Doehler Japan"))
        self.query_label.setText(_translate("lto_database", "Query Box (SQLite syntax)"))
        self.visualize_button.setText(_translate("lto_database", "Visualize displayed data"))
        self.extract_button.setText(_translate("lto_database,", "Extract shown data"))
        self.update_button.setText(_translate("lto_database", "Update database"))
        self.update_label.setText(
            _translate("lto_database", "To update  - Please select excel file originating from \'WE LEAD ANALYTICS\'"))
        self.tableload_label.setText(_translate("lto_database", "lto table loaded"))

    def update_lto_clicked(self):
        self.lto_dir_file = QtWidgets.QFileDialog.getOpenFileName(filter="*.xlsx")

        if not self.lto_dir_file[0]:
            self.update_label.setText("Update file not inserted.")
            self.update_label.setStyleSheet("background-color: rgb(255, 0, 0);")
            return

        self.lto_dir_file = os.path.abspath(self.lto_dir_file[0])
        self.update_label.setText(f"{os.path.basename(self.lto_dir_file)} - Updating database, please wait...")

        # First making sure that the file is correctly formatted
        try:
            self.lto_data_file = lto_date_format(self.lto_dir_file)

            if not self.lto_data_file:  # If the function returned False, it has failed the test.
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("The file uploaded does not match the desired format. Please check whether "
                                         "the correct file has been uploaded.")
                error_dialog.exec_()
                return
        except (TypeError, ValueError):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("TypeError has occured. File format was correct, but something went wrong "
                                     "when re-formatting the data")
            error_dialog.exec_()
            return

        # Importing the excel data into the database ---ERROR HANDLING WHEN WE FIND A BUG HERE---
        db.close() # We have to close the database first before writing in the new data
        self.lto_data_updated = updateLTO(self.lto_data_file)

        print("Succesfully written into database")
        message = QtWidgets.QMessageBox()
        message.setText(f'New opportunities added: {self.lto_data_updated[0]}\n'
                        f'Existing Opportunities updated: {self.lto_data_updated[1]}\n'
                        f'Old opportunities deleted: {self.lto_data_updated[2]}\n'
                        f'\nTotal opportunities active: {self.lto_data_updated[3]}\n')
        message.exec_()
        self.update_label.setText("Database updated!")

        # After done writing, we re-open the file and load in the updated data into the table
        # This is a literal copy from the main class
        db.open()
        self.model = QSqlTableModel(db=db)
        self.model.setTable("lto")
        # self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        self.query.prepare("SELECT * from lto ORDER BY launch")
        self.query.exec_()
        self.model.setQuery(self.query)

        self.table_data.setModel(self.model)
        self.table_data.resizeColumnsToContents()

    def update_query(self):
        if not self.query_lineedit.text():
            self.query.prepare("SELECT * FROM lto ORDER BY launch")
        else:
            self.query.prepare(self.query_lineedit.text())

        self.query.exec_()
        self.model.setQuery(self.query)
        self.table_data.resizeColumnsToContents()


if __name__ == "__main__":
    import sys

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    lto_database = QtWidgets.QMainWindow()
    ui = Ui_lto_database()
    ui.setupUi(lto_database)
    lto_database.show()
    sys.exit(app.exec_())
