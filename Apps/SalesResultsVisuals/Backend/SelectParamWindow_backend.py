"""Backend code for buttons."""

from Apps.ConnectDatabase import SQLiteAuth
from Apps.MessageBoxes import ErrorMessage
from Apps.ErrorClass import *

class ParamBackend:
    def __init__(self, windowclass):
        """
        Attributes
        ---------------
        self.main : instance of Ui_sales_database
            Receives the GUI as instance.
        self.database_used : str
            Sets the database name that will be a parameter for
            multiple executions in methods.
        """
        self.main = windowclass
        self.database_used = "sales.db"

        self.__connect_buttons()

    def __connect_buttons(self):
        """Connects button to method"""
        self.main.button.clicked.connect(
            lambda: self.start_dashboard()
        )

    def start_dashboard(self):
        """Manager that starts workflow for starting dashboard."""
        try:
            self.__check_month_box()
            self.__check_results_box()
            self.__check_existing_data()
        except (MonthNotFound, InvalidOption, IncorrectMonth):
            return

        self.show_data()

    def __check_month_box(self):
        """Checks whether month was selected."""
        if self.main.combo.currentText() == "Select Month for visuals":
            ErrorMessage("You did not select a month. Please select a month.")
            raise MonthNotFound

    def __check_results_box(self):
        """Checks whether sales results type was selected."""
        if self.main.combo2.currentText() == \
                "Select 'Local' or 'Destination' results":
            ErrorMessage(
                "Please select what sales results should be visualized. "
                "Please select 'Local' or 'Destination'"
            )
            raise InvalidOption

    def __check_existing_data(self):
        """Checks whether the month in the combobox has any rows."""
        month = self.main.combo.currentText()

        with SQLiteAuth(self.database_used) as datab:
            datab.sqlite_show(
                f"SELECT COUNT(month) FROM sales WHERE month = '{month}'")
            data_amt = datab.data_extract

        if data_amt[0][0] == 0:
            ErrorMessage(
                "This month has not been uploaded to the database yet. "
                "Please upload the month or select a different month."
            )
            raise IncorrectMonth

    def show_data(self):
        """Opens the dashboard app with month and sales results
        type as parameters."""
        from Apps.SalesResultsVisuals.LinkApplications import \
            SalesResultsAnalysisApplications

        print("Starting App")
        self.open_app = SalesResultsAnalysisApplications()
        self.open_app.show_sales_dashboard(
            self.main.combo.currentText(),
            self.main.combo2.currentText()
        )