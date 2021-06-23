# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ltoSQLTableEnlarged.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Apps.DailySalesUpload.Backend.MarginWindow_backend import MarginWindowBackend

class Ui_margin_window(object):
    def setupUi(self, lto_database):
        lto_database.setObjectName("lto_database")
        lto_database.resize(560, 800)
        lto_database.setMinimumSize(QtCore.QSize(560, 800))
        lto_database.setMaximumSize(QtCore.QSize(560, 800))
        font = QtGui.QFont()
        font.setPixelSize(9)
        lto_database.setFont(font)
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
        self.update_label = QtWidgets.QLabel(self.frame)
        self.update_label.setEnabled(True)
        self.update_label.setGeometry(QtCore.QRect(0, 0, 551, 81))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.update_label.setFont(font)
        self.update_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")
        self.update_label.setObjectName("update_label")
        self.verticalLayout.addWidget(self.frame)
        self.actions_frame = QtWidgets.QFrame(self.centralwidget)
        self.actions_frame.setMinimumSize(QtCore.QSize(1601, 71))
        self.actions_frame.setStyleSheet("background-color: rgb(0, 40, 72);")
        self.actions_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.actions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actions_frame.setObjectName("actions_frame")
        self.query_lineedit = QtWidgets.QLineEdit(self.actions_frame)
        self.query_lineedit.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.query_lineedit.setFont(font)
        self.query_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.query_lineedit.setObjectName("query_lineedit")
        self.query_label = QtWidgets.QLabel(self.actions_frame)
        self.query_label.setGeometry(QtCore.QRect(10, 0, 161, 21))
        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.query_label.setFont(font)
        self.query_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.query_label.setObjectName("query_label")
        self.extract_button = QtWidgets.QPushButton(self.actions_frame)
        self.extract_button.setGeometry(QtCore.QRect(180, 10, 81, 51))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.extract_button.setFont(font)
        self.extract_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 111, 196);")
        self.extract_button.setObjectName("extract_button ")
        self.update_button = QtWidgets.QPushButton(self.actions_frame)
        self.update_button.setGeometry(QtCore.QRect(270, 10, 81, 51))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.update_button.setFont(font)
        self.update_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 111, 196);")
        self.update_button.setObjectName("update_button")
        self.query_label_2 = QtWidgets.QLabel(self.actions_frame)
        self.query_label_2.setGeometry(QtCore.QRect(390, 10, 161, 51))
        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.query_label_2.setFont(font)
        self.query_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.query_label_2.setObjectName("query_label_2")
        self.verticalLayout.addWidget(self.actions_frame)
        self.table_data = QtWidgets.QTableView(self.centralwidget)
        self.table_data.setMinimumSize(QtCore.QSize(400, 400))
        self.table_data.setMaximumSize(QtCore.QSize(550, 600))
        self.table_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_data.setObjectName("table_data")
        self.verticalLayout.addWidget(self.table_data)
        lto_database.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lto_database)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 18))
        self.menubar.setObjectName("menubar")
        lto_database.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lto_database)
        self.statusbar.setObjectName("statusbar")
        lto_database.setStatusBar(self.statusbar)

        self.retranslateUi(lto_database)
        QtCore.QMetaObject.connectSlotsByName(lto_database)

        backend = MarginWindowBackend(self)

    def retranslateUi(self, lto_database):
        _translate = QtCore.QCoreApplication.translate
        lto_database.setWindowTitle(_translate("lto_database", "MainWindow"))
        self.update_label.setText(_translate("lto_database", "Upload: File must be without headers and with columns \'A\' and \'B\' as displayed below"))
        self.query_label.setText(_translate("lto_database", "Product Number"))
        self.extract_button.setText(_translate("lto_database", "Extract"))
        self.update_button.setText(_translate("lto_database", "Update"))
        self.query_label_2.setText(_translate("lto_database", "Japan Margin/kg"))