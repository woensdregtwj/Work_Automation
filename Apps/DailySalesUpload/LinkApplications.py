from PyQt5.QtWidgets import QMainWindow

from Apps.DailySalesUpload import MarginWindow

class DailySalesApplications:
    def show_margin_window(self):
        self.margin_window = QMainWindow()
        self.ui = MarginWindow.Ui_margin_window()
        self.ui.setupUi(self.margin_window)
        self.margin_window.show()
