# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailySalesUpload.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

from Apps.DailySalesUpload.Backend.DailySales_backend import DailySalesBackend


class Ui_Daily_Sales_Upload(object):
    def setupUi(self, LTO_Date_Formatting):
        LTO_Date_Formatting.setObjectName("LTO_Date_Formatting")
        LTO_Date_Formatting.resize(800, 400)
        LTO_Date_Formatting.setMinimumSize(QtCore.QSize(800, 380))
        LTO_Date_Formatting.setMaximumSize(QtCore.QSize(800, 380))
        self.centralwidget = QtWidgets.QWidget(LTO_Date_Formatting)
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
        self.upload_box = QtWidgets.QGroupBox(self.centralwidget)
        self.upload_box.setGeometry(QtCore.QRect(10, 90, 781, 261))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.upload_box.setFont(font)
        self.upload_box.setObjectName("upload_box")
        self.uploaded_label = QtWidgets.QLabel(self.upload_box)
        self.uploaded_label.setGeometry(QtCore.QRect(260, 80, 291, 31))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.uploaded_label.setFont(font)
        self.uploaded_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploaded_label.setObjectName("uploaded_label")
        self.upload_button = QtWidgets.QPushButton(self.upload_box)
        self.upload_button.setGeometry(QtCore.QRect(30, 80, 211, 31))
        self.upload_button.setObjectName("upload_button")

        self.save_button = QtWidgets.QPushButton(self.upload_box)
        self.save_button.setEnabled(True)
        self.save_button.setGeometry(QtCore.QRect(620, 40, 121, 111))
        self.save_button.setObjectName("save_button")

        self.db_button = QtWidgets.QPushButton(self.upload_box)
        self.db_button.setGeometry(QtCore.QRect(400, 30, 151, 31))
        self.db_button.setObjectName("save_button")

        self.uploaded_label_2 = QtWidgets.QLabel(self.upload_box)
        self.uploaded_label_2.setGeometry(QtCore.QRect(260, 130, 291, 31))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.uploaded_label_2.setFont(font)
        self.uploaded_label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploaded_label_2.setObjectName("uploaded_label_2")
        self.upload_button_2 = QtWidgets.QPushButton(self.upload_box)
        self.upload_button_2.setGeometry(QtCore.QRect(30, 130, 211, 31))
        self.upload_button_2.setObjectName("upload_button_2")

        self.uploaded_label_3 = QtWidgets.QLabel(self.upload_box)
        self.uploaded_label_3.setGeometry(QtCore.QRect(260, 180, 291, 31))
        font = QtGui.QFont()
        font.setPixelSize(15)
        self.uploaded_label_3.setFont(font)
        self.uploaded_label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploaded_label_3.setObjectName("uploaded_label_2")
        self.upload_button_3 = QtWidgets.QPushButton(self.upload_box)
        self.upload_button_3.setGeometry(QtCore.QRect(30, 180, 211, 31))
        self.upload_button_3.setObjectName("upload_button_2")

        self.comboBox = QtWidgets.QComboBox(self.upload_box)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        LTO_Date_Formatting.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LTO_Date_Formatting)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        LTO_Date_Formatting.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LTO_Date_Formatting)
        self.statusbar.setObjectName("statusbar")
        LTO_Date_Formatting.setStatusBar(self.statusbar)

        self.retranslateUi(LTO_Date_Formatting)
        QtCore.QMetaObject.connectSlotsByName(LTO_Date_Formatting)

        self.backend = DailySalesBackend(self)

    def retranslateUi(self, LTO_Date_Formatting):
        _translate = QtCore.QCoreApplication.translate
        LTO_Date_Formatting.setWindowTitle(_translate("LTO_Date_Formatting", "MainWindow"))
        self.app_title.setText(_translate("LTO_Date_Formatting", "Daily Sales Upload"))
        self.upload_box.setTitle(_translate("LTO_Date_Formatting", "Upload Sales Result Files"))
        self.uploaded_label.setText(_translate("LTO_Date_Formatting", "No File Loaded"))
        self.upload_button.setText(_translate("LTO_Date_Formatting", "Sales Results - Prev. Week"))
        self.save_button.setText(_translate("LTO_Date_Formatting", "Save"))
        self.db_button.setText(_translate("LTO_Date_Formatting", "Gross Margin DB"))
        self.uploaded_label_2.setText(_translate("LTO_Date_Formatting", "No File Loaded"))
        self.upload_button_2.setText(_translate("LTO_Date_Formatting", "Sales Results - Latest Data"))
        self.uploaded_label_3.setText(_translate("LTO_Date_Formatting", "No File Loaded"))
        self.upload_button_3.setText(_translate("LTO_Date_Formatting", "Orders On Hands Main File"))
        self.comboBox.setItemText(0, _translate("LTO_Date_Formatting", "First Upload Of Month?"))
        self.comboBox.setItemText(1, _translate("LTO_Date_Formatting", "Yes"))
        self.comboBox.setItemText(2, _translate("LTO_Date_Formatting", "No"))


if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    LTO_Date_Formatting = QtWidgets.QMainWindow()
    ui = Ui_Daily_Sales_Upload()
    ui.setupUi(LTO_Date_Formatting)
    LTO_Date_Formatting.show()
    sys.exit(app.exec_())
