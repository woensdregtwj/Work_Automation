# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LTODateFixer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from LTODateConverterFunction import *
import openpyxl
import os


class Ui_lto_date(object):
    def setupUi(self, individual_forecast):
        individual_forecast.setObjectName("individual_forecast")
        individual_forecast.resize(800, 320)
        individual_forecast.setMinimumSize(QtCore.QSize(800, 320))
        individual_forecast.setMaximumSize(QtCore.QSize(800, 320))
        self.centralwidget = QtWidgets.QWidget(individual_forecast)
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
        self.upload_box = QtWidgets.QGroupBox(self.centralwidget)
        self.upload_box.setGeometry(QtCore.QRect(10, 100, 781, 171))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.upload_box.setFont(font)
        self.upload_box.setObjectName("upload_box")
        self.upload_label = QtWidgets.QLabel(self.upload_box)
        self.upload_label.setGeometry(QtCore.QRect(30, 30, 491, 18))
        self.upload_label.setObjectName("upload_label")
        self.uploaded_label = QtWidgets.QLabel(self.upload_box)
        self.uploaded_label.setGeometry(QtCore.QRect(30, 120, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.uploaded_label.setFont(font)
        self.uploaded_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploaded_label.setObjectName("uploaded_label")
        self.upload_button = QtWidgets.QPushButton(self.upload_box)
        self.upload_button.setGeometry(QtCore.QRect(30, 60, 211, 31))
        self.upload_button.setObjectName("upload_button")
        self.save_button = QtWidgets.QPushButton(self.upload_box)
        self.save_button.setEnabled(False)
        self.save_button.setGeometry(QtCore.QRect(480, 40, 261, 111))
        self.save_button.setObjectName("save_button")
        individual_forecast.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(individual_forecast)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        individual_forecast.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(individual_forecast)
        self.statusbar.setObjectName("statusbar")
        individual_forecast.setStatusBar(self.statusbar)

        self.retranslateUi(individual_forecast)
        QtCore.QMetaObject.connectSlotsByName(individual_forecast)

        self.upload_button.clicked.connect(self.upload_clicked)
        self.save_button.clicked.connect(self.save_clicked)

    def retranslateUi(self, individual_forecast):
        _translate = QtCore.QCoreApplication.translate
        individual_forecast.setWindowTitle(_translate("individual_forecast", "MainWindow"))
        self.app_title.setText(_translate("individual_forecast", "Simple LTO Date Formatter"))
        self.upload_box.setTitle(_translate("individual_forecast", "Upload Forecast File"))
        self.upload_label.setText(_translate("individual_forecast", "Upload raw .xlsx LTO File"))
        self.uploaded_label.setText(_translate("individual_forecast", "No File Loaded"))
        self.upload_button.setText(_translate("individual_forecast", "Upload LTO File"))
        self.save_button.setText(_translate("individual_forecast", "Save"))

    def upload_clicked(self):
        self.lto_file = QtWidgets.QFileDialog.getOpenFileName(filter="*.xlsx")

        if not self.lto_file[0]:
            return
        self.lto_file = os.path.abspath(self.lto_file[0])

        try:
            self.lto_output_file = lto_date_format(self.lto_file)

            if not self.lto_output_file: # If the function returned False, it has failed the test.
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("The file uploaded does not match the desired format. Please check whether "
                                         "the correct file has been uploaded.")
                error_dialog.exec_()
                return

            self.uploaded_label.setText(f"Formatting: {os.path.basename(self.lto_file)}...")
            self.uploaded_label.setStyleSheet("background-color: rgb(255, 69, 0);")
        except (TypeError, ValueError):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("TypeError has occured. File format was correct, but something went wrong "
                                     "when re-formatting the data")
            error_dialog.exec_()
            return

        self.upload_button.setEnabled(False)
        self.uploaded_label.setText(f"FORMATTING COMPLETE. PRESS SAVE >>>")
        self.uploaded_label.setStyleSheet("background-color: rgb(174, 217, 167);")
        self.save_button.setEnabled(True)

    def save_clicked(self):
        self.save_directory = QtWidgets.QFileDialog.getSaveFileName(filter="*.xlsx")

        if not self.save_directory[0]:
            return

        self.lto_output_file.save(os.path.abspath(self.save_directory[0]))

        self.uploaded_label.setText("Succesfully saved!")
        self.save_button.setEnabled(False)
        self.upload_button.setEnabled(True)

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    lto_date = QtWidgets.QMainWindow()
    ui = Ui_lto_date()
    ui.setupUi(lto_date)
    lto_date.show()
    sys.exit(app.exec_())
