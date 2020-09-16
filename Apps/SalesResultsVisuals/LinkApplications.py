"""
Contains all the run-codes for opening a new window with the
desired application.

Which application will open is dependable on the button pushed on
the SalesResultsAnalysis.py

"""
from PyQt5.QtWidgets import QMainWindow
from Apps.SalesResultsVisuals import UploadSalesWindow
from Apps.SalesResultsVisuals import SelectParamWindow
from Apps.SalesResultsVisuals import SalesResultsDashboard

class SalesResultsAnalysisApplications:
    """This class is meant to be a composition for SalesResultsAnalysis.py"""
    def sales_results_update(self):
        self.SalesResultsUploadWindow = QMainWindow()
        self.ui = UploadSalesWindow.Ui_SalesResultsUploadWindow()
        self.ui.setupUi(self.SalesResultsUploadWindow)
        self.SalesResultsUploadWindow.show()

    def sales_visualize_param(self):
        self.month_visualize = QMainWindow()
        self.ui = SelectParamWindow.Ui_VisualizeMonth()
        self.ui.setupUi(self.month_visualize)
        self.month_visualize.show()

    def show_sales_dashboard(self, combo_param1, combo_param2):
        self.SalesResultsVis = QMainWindow()
        self.ui = SalesResultsDashboard.Ui_SalesResultsVis()
        self.ui.setupUi(self.SalesResultsVis, combo_param1, combo_param2)
        self.SalesResultsVis.show()