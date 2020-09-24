from PyQt5 import QtCore, QtWidgets
import sqlite3




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

        self.button.clicked.connect(self.show_data)

    def show_data(self):
        if self.combo.currentText() == "Select Month for visuals":
            message = QtWidgets.QMessageBox()
            message.setText("You did not select a month.\n\nPlease select a month.")
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()
            return

        if self.combo2.currentText() == "Select 'Local' or 'Destination' results":
            message = QtWidgets.QMessageBox()
            message.setText("Please select what sales results should be visualized.\n\nPlease select 'Local' or Destination.")
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()
            return

        # Checking whether the month is in the database
        month_in_database = self.check_month()
        if not month_in_database:
            message = QtWidgets.QMessageBox()
            message.setText("This month has not been uploaded to the database yet.\n\n"
                            "Please upload the month or select a different month.")
            message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            message.exec_()
            return

        from Apps.SalesResultsVisuals.LinkApplications import \
            SalesResultsAnalysisApplications

        print("Starting App")
        self.open_app = SalesResultsAnalysisApplications()
        self.open_app.show_sales_dashboard(
            self.combo.currentText(),
            self.combo2.currentText()
        )



    def check_month(self):
        month = self.combo.currentText()

        connect = sqlite3.connect("Databases\\sales.db")
        c = connect.cursor()

        c.execute(f"SELECT COUNT(month) FROM sales WHERE month = '{month}'")
        print(f"SELECT COUNT(month) FROM sales WHERE month = '{month}'")
        data_amt = c.fetchall()

        c.close()
        connect.close()

        if data_amt[0][0] == 0:
            return False

        return True