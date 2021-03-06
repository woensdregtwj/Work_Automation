# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.2
"""Sales Results Analysis window that displays data of actual sales
only through a QSql Table View. Can adjust what data to display
through inserting a SQLite3 syntax-based query.

The data is uploaded monthly by the user into the SQLite3
database, uploading can only be done via this window.
Possibility for overwriting a certain month also implemented.

Through this window the user can also open a statistics dashboard
that displays multiple charts and tables for analytical purposes.

This window also makes it possible to extract the data being displayed
in the QSql Table View. Based on the inserted query, a personalized
data extraction is possible. Export file is a .xlsx workbook.

This is the UI file, backend code is separated in
'SalesResultsAnalysis_backend'.
"""

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel

from Apps.SalesResultsVisuals.Backend import SalesResultsAnalysis_backend \
    as backend
from Apps.SalesResultsVisuals.LinkApplications import \
    SalesResultsAnalysisApplications
from Apps.ConnectDatabase import QSqlAuth, SQLiteAuth


class Ui_sales_database(object):
    def setupUi(self, sales_database):
        sales_database.setObjectName("sales_database")
        sales_database.resize(1600, 805)
        sales_database.setMinimumSize(QtCore.QSize(1600, 800))
        sales_database.setMaximumSize(QtCore.QSize(16777215, 16777215))
        sales_database.setStyleSheet("background-color: rgb(0, 40, 72);")
        self.centralwidget = QtWidgets.QWidget(sales_database)
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
        font.setPixelSize(15)
        self.query_lineedit.setFont(font)
        self.query_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.query_lineedit.setObjectName("query_lineedit")
        self.query_label = QtWidgets.QLabel(self.actions_frame)
        self.query_label.setGeometry(QtCore.QRect(10, 0, 261, 21))
        font = QtGui.QFont()
        font.setPixelSize(20)
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
        font.setPixelSize(15)
        self.visualize_button.setFont(font)
        self.visualize_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(0, 111, 196);")
        self.visualize_button.setObjectName("visualize_button")

        self.extract_button = QtWidgets.QPushButton(self.actions_frame)
        self.extract_button.setGeometry(QtCore.QRect(740, 10, 100, 51))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.extract_button.setFont(font)
        self.extract_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(0, 111, 196);")
        self.extract_button.setObjectName("visualize_button")

        self.update_button = QtWidgets.QPushButton(self.actions_frame)
        self.update_button.setGeometry(QtCore.QRect(1040, 10, 181, 51))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.update_button.setFont(font)
        self.update_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 111, 196);")
        self.update_button.setObjectName("update_button")
        self.update_label = QtWidgets.QLabel(self.actions_frame)
        self.update_label.setEnabled(True)
        self.update_label.setGeometry(QtCore.QRect(1230, 20, 361, 31))
        font = QtGui.QFont()
        font.setPixelSize(10)
        self.update_label.setFont(font)
        self.update_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(0, 85, 127);")
        self.update_label.setObjectName("update_label")
        self.tableload_label = QtWidgets.QLabel(self.actions_frame)
        self.tableload_label.setGeometry(QtCore.QRect(260, 0, 451, 21))
        font = QtGui.QFont()
        font.setPixelSize(20)
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
        font.setPixelSize(14)
        self.table_data.setFont(font)
        self.verticalLayout.addWidget(self.table_data)
        sales_database.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sales_database)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 18))
        self.menubar.setObjectName("menubar")
        sales_database.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sales_database)
        self.statusbar.setObjectName("statusbar")
        sales_database.setStatusBar(self.statusbar)

        self.retranslateUi(sales_database)
        QtCore.QMetaObject.connectSlotsByName(sales_database)

        ######  Initiating the backend code.
        #################################################
        back = backend.SalesResultsAnalysisBackend(self)

    def retranslateUi(self, sales_database):
        _translate = QtCore.QCoreApplication.translate
        sales_database.setWindowTitle(_translate("sales_database", "MainWindow"))
        self.app_title.setText(_translate("sales_database", "Sales Results EURk - Doehler Japan"))
        self.query_label.setText(_translate("sales_database", "SQLite syntax"))
        self.visualize_button.setText(_translate("sales_database", "Visualize displayed data"))
        self.extract_button.setText(_translate("sales_database,", "Extract shown data"))
        self.update_button.setText(_translate("sales_database", "Update database"))
        self.update_label.setText(
            _translate("sales_database", "To update  - Please select excel file originating from \'WE LEAD ANALYTICS\'"))
        self.tableload_label.setText(_translate("sales_database", "'sales' table loaded - Available tables: 'sales', "
                                                                  "'local'."))

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    sales_database = QtWidgets.QMainWindow()
    ui = Ui_sales_database()
    ui.setupUi(sales_database)
    sales_database.show()
    sys.exit(app.exec_())
