import os
from PyQt5 import QtWidgets

from Apps.ErrorClass import (
    IncorrectMonth, MonthNotFound, WrongNumberFormatting, HeaderMissing,
UploadFailure, UserCancel, NoFileSelected, NotConnectedError
)
from Apps.SalesResultsVisuals.UpdateSalesDatabase import SalesRConfirmFormat
from Apps.SalesResultsVisuals.UpdateSalesDatabase import SalesRUpload
from Apps.SalesResultsVisuals.UpdateSalesDatabase import SalesRFile
from Apps.MessageBoxes import ErrorMessage, BasicMessage
from Apps.ConnectDatabase import SQLiteAuth


class UploadSalesBackend:
    def __init__(self, windowclass):
        self.main = windowclass
        self.database_used = "sales.db"

        self.__connect_buttons()

    def __connect_buttons(self):
        self.main.upload1_lbutton.clicked.connect(
            lambda: self.upload_manager()
        )

    def upload_manager(self):
        try:
            self.__confirm_combobox()
            self.__check_existing_data()
            self.__obtain_directory()
            self.__upload_to_db()
        except UploadFailure:
            return  # Raised from 'confirm_combobox()'
        except UserCancel:
            return  # Raised from 'check_existing_data()'
        except NoFileSelected:
            return  # Raised from 'obtain_directory()'

        try:
            self.__upload_to_db()
        except HeaderMissing as e:
            print(e, "OKAY THEN")
            return "CANCELLED"
        except NotConnectedError:
            return  # Raised from attr upload_data class
        except NoFileSelected:
            print("I WAS RAISED")
            return

    def __confirm_combobox(self):
        """Confirms that a month is selected in the combo box."""
        self.month = self.main.month_combobox.currentText()
        if self.month == "Select":
            ErrorMessage(
                "No month has been selected. Please select a month."
            )
            raise UploadFailure()

    def __check_existing_data(self):
        """Checks whether the selected month from combo box already has
        data in the database. User input requested for whether to
        overwrite or not. If yes, calls method for clearing data of
        selected month."""
        with SQLiteAuth(self.database_used) as datab:
            datab.sqlite_show(
                f"SELECT COUNT(month) FROM sales WHERE month = '{self.month}'"
            )
            data_count = datab.data_extract[0][0]

        if data_count != 0:
            message_box = BasicMessage(
                f"{data_count} lines of data for month {self.month} are "
                f"already in the database.\nDo you want to overwrite "
                f"these lines with new sales results data?",
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Abort
            )

            if message_box.button_pressed != QtWidgets.QMessageBox.Ok:
                BasicMessage("Upload canceled.")
                raise UserCancel("Overwriting data canceled by user.")
            else:
                self.__delete_month()
                '''Clearing data of month in db and next method called
                in upload manager method will add new data.'''

    def __delete_month(self):
        with SQLiteAuth(self.database_used) as datab:
            datab.execute_query(
                f"DELETE FROM sales WHERE month = '{self.month}'"
            )

    def __obtain_directory(self):
        # Obtaining the file path from the file dialog
        self.sales_dir = QtWidgets.QFileDialog.getOpenFileName(filter="*xlsx")
        if not self.sales_dir[0]:
            self.main.upload1_label.setText("File was not selected.")
            self.main.upload1_label.setStyleSheet(
                "background-color: rgb(255, 0, 0);"
            )
            raise NoFileSelected("No upload file selected")

        self.sales_dir = os.path.abspath(self.sales_dir[0])
        self.main.upload1_label.setText(
            f"{os.path.basename(self.sales_dir)} is currently loaded"
        )
        self.main.upload1_label.setStyleSheet(
            "background-color: rgb(174, 217, 167);"
        )


    def __upload_to_db(self):
        sales_results = SalesRFile(self.sales_dir, self.month)

        test_format = SalesRConfirmFormat(sales_results)
        test_format.start_test()
        print("ALL GOOD")

        upload_data = SalesRUpload(sales_results)
        upload_data.start_upload()
