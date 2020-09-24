"""
Contains all the run-codes for opening a new window with the
desired application.

Which application will open is dependable on the button pushed on
the DoehlerDashboard.py

"""

from PyQt5.QtWidgets import QMainWindow
import webbrowser

from SalesForecastUpdateEOM import *
from SalesResultsAnalysis import *
from SendForecast import *
from LTODateFormatting import *
from ltoAnalysis import *
from AgingList import *

from Apps.ForecastUpdate import SalesForecastUpdate
from Apps.ForecastUpdateEOM import SalesForecastUpdateEOM
from Apps.SalesResultsVisuals import SalesResultsAnalysis

class WindowApplication:
    """This class is meant to be a composition for DoehlerDashboard.py"""
    def sales_forecast_update(self):
        """For button - Sales Forecast Update; From GroupBox - Forecasting"""
        self.forecast_updater = QMainWindow()
        self.ui = SalesForecastUpdate.Ui_forecast_update_window()
        self.ui.setup_fc_update(self.forecast_updater)
        self.forecast_updater.show()

    def sales_forecast_EOM(self):
        """For button - Sales Forecast EOM; From GroupBox - Forecasting"""
        self.forecast_EOM_updater = QMainWindow()
        self.ui = SalesForecastUpdateEOM.Ui_forecast_EOM_window()
        self.ui.setup_fc_update(self.forecast_EOM_updater)
        self.forecast_EOM_updater.show()

    def sales_visuals(self):
        """For button - Sales Results Visuals; From GroupBox - Forecasting"""
        self.sales_database = QMainWindow()
        self.ui = SalesResultsAnalysis.Ui_sales_database()
        self.ui.setupUi(self.sales_database)
        self.sales_database.show()

    def lto_analysis(self):
        """For button - LTO Analysis; From GroupBox - Controlling"""
        self.lto_database = QMainWindow()
        self.ui = Ui_lto_database()
        self.ui.setupUi(self.lto_database)
        self.lto_database.show()

    def local_fc_analysis(self):
        """For button - Local FC Analysis; From GroupBox - Controlling"""
        self.individual_forecast = QMainWindow()
        self.ui = Ui_individual_forecast()
        self.ui.setupUi(self.individual_forecast)
        self.individual_forecast.show()

    def aging_upload(self):
        """For button - BW Aging List; From GroupBox - Monthly Closing"""
        self.AgingWindow = QMainWindow()
        ui = Ui_AgingWindow()
        ui.setupUi(self.AgingWindow)
        self.AgingWindow.show()

    def lto_date_convert(self):
        """For button - LTO Date Format; From GroupBox - Extra Tools"""
        self.lto_date = QMainWindow()
        self.ui = Ui_lto_date()
        self.ui.setupUi(self.lto_date)
        self.lto_date.show()

    def tm5_website(self):
        """For button - tm5 Login; From GroupBox - Extra Tools"""
        webbrowser.open(
            "https://doehler.mytm5.com/system/portal.asp?url=%2FLMCash%2FKAmanValuten%2Easp&a_Meldung=AutoLogout&AG=1u&#e_Benutzer")

    def salesforce_website(self):
        """For button - Salesforce; From GroupBox - Extra Tools"""
        webbrowser.open(
            "https://login.salesforce.com/"
        )

    def commerz_website(self):
        """For button - Commerzbank; From GroupBox - Extra Tools"""
        webbrowser.open(
            "https://cbportal.commerzbank.com/lp/login?fk&cifSecParams=SUxAAYR38N76HAQAKnx47VTw6hOzbzYbex3iUzOItBm4jsqr6GpZQg"
        )

    def bpm_website(self):
        """For button - BPM System; From GroupBox - Extra Tools"""
        webbrowser.open(
            "http://bpm.doehler.com.cn/Login.html"
        )

    def doehler_website(self):
        """For button - Doehler Portal; From GroupBox - Extra Tools"""
        webbrowser.open(
            "https://portal.doehler.com/logon/LogonPoint/tmindex.html"
        )