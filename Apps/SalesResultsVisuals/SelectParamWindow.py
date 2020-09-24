from PyQt5 import QtCore, QtWidgets
import sqlite3
from Apps.SalesResultsVisuals.Backend.SelectParamWindow_backend \
    import ParamBackend as backend

class Ui_VisualizeMonth(object):
    def setupUi(self, VizualizeMonth):
        VizualizeMonth.resize(200, 200)
        VizualizeMonth.setMinimumSize(QtCore.QSize(250, 100))
        VizualizeMonth.setMaximumSize(QtCore.QSize(250, 100))

        self.layout = QtWidgets.QVBoxLayout()

        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(["Select Month for visuals", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
        self.combo.setStyleSheet("background-color: rgb(174, 217, 167);")

        self.combo2 = QtWidgets.QComboBox()
        self.combo2.addItems(["Select 'Local' or 'Destination' results", "Local Sales Results", "Destination Sales Results"])
        self.combo2.setStyleSheet("background-color: rgb(100, 217, 167);")

        self.button = QtWidgets.QPushButton("Proceed with visualization")

        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.combo2)
        self.layout.addWidget(self.button)

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)
        VizualizeMonth.setCentralWidget(self.widget)

        ######  Initiating the backend code.
        #################################################
        back = backend(self)