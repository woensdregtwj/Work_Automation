"""Backend code for button click."""

import os
from PyQt5 import QtWidgets

from Apps.ErrorClass import IncorrectMonth
from Apps.ErrorClass import MonthNotFound
from Apps.ErrorClass import WrongNumberFormatting
from Apps.ErrorClass import HeaderMissing
from Apps.ErrorClass import UploadFailure
from Apps.ErrorClass import UserCancel
from Apps.ErrorClass import NoFileSelected
from sqlite3 import OperationalError

from Apps.SalesResultsVisuals.Backend.UpdateSalesDatabase import SalesRConfirmFormat
from Apps.SalesResultsVisuals.Backend.UpdateSalesDatabase import SalesRUpload
from Apps.SalesResultsVisuals.Backend.UpdateSalesDatabase import SalesRFile
from Apps.MessageBoxes import ErrorMessage, BasicMessage
from Apps.ConnectDatabase import SQLiteAuth


class UploadSalesBackend:
    """Backend code for when 'Upload Sales Results' button gets
    clicked. Checks whether a month has properly been selected in the
    combo box, then checks whether this month already has data in the
    database. Finally, starts upload workflow from excel sheet to db.

    Methods
    ---------------
    __connect_buttons - Connects button to code
    upload_manager - Starts the upload process
    __confirm_combobox - Confirms whether month in combobox is valid
    __check_existing_data - Checks whether month has data in db
    __delete_month - Asks user whether to delete existing month data
    __obtain_directory - File dialog for retrieving excel file directory
    __upload_to_db - Tests excel file and uploads data to db
    """
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
        """Gets called at init and connects buttons to method."""
        self.main.upload1_lbutton.clicked.connect(
            lambda: self.upload_manager()
        )

    def upload_manager(self):
        """Manager method that starts the workflow for uploading data."""
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
        except IncorrectMonth:
            return  # Raised from 'upload_to_db()'
        except MonthNotFound:
            return  # Raised from 'upload_to_db()'
        except WrongNumberFormatting:
            return  # Raised from 'upload_to_db()'
        except HeaderMissing:
            return  # Raised from 'upload_to_db()'

    def __confirm_combobox(self):
        """Confirms that a month and view type
         is selected in the combo box."""
        self.month = self.main.month_combobox.currentText()
        self.data_view = self.main.data_type_combobox.currentText()
        if self.month == "Select":
            ErrorMessage(
                "No month has been selected. Please select a month."
            )
            raise UploadFailure()
        elif self.data_view == "Select":
            ErrorMessage(
                "No data view type has been selected. "
                "Please select the correct type."
            )
            raise UploadFailure()

    def __check_existing_data(self):
        """Depending on selected data view, will check the proper db table.
        Then checks whether the selected month from combo box already
        has data in the database. User input requested for whether to
        overwrite or not. If yes, calls method for clearing data of
        selected month.

        If in combo box 2 'Destination' view has been selected, then
        we set our table to 'sales', if not, then we check the data
        of table 'local'."""
        if self.data_view == "Destination View":
            db_table = "sales"
        else:  # Local View
            db_table = "local"

        with SQLiteAuth(self.database_used) as datab:
            try:
                datab.sqlite_show(
                    f"SELECT COUNT(month) FROM {db_table} "
                    f"WHERE month = '{self.month}'"
                )
                data_count = datab.data_extract[0][0]
            except OperationalError:  # Table does not exist
                self.__create_db_table(datab, db_table)
                print("error")
                data_count = 0

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
                self.__delete_month(db_table)
                '''Clearing data of month in db and next method called
                in upload manager method will add new data.'''

    def __delete_month(self, table):
        """Deletes data of month if user agreed."""
        with SQLiteAuth(self.database_used) as datab:
            datab.execute_query(
                f"DELETE FROM {table} "
                f"WHERE month = '{self.month}'"
            )

    def __create_db_table(self, datab, db_table):
        datab.execute_query(
            f"CREATE TABLE IF NOT EXISTS {db_table} ("
            f"month TEXT, "
            f"code TEXT, "
            f"company TEXT, "
            f"customer TEXT, "
            f"bu1 TEXT, "
            f"bu2 TEXT, "
            f"materialid TEXT, "
            f"material TEXT, "
            f"vol INT, "
            f"ns INT, "
            f"gs INT, "
            f"gm INT, "
            f"cm1 INT)"
        )



    def __obtain_directory(self):
        """"Obtains file path from file dialog. If no dialog inserted,
        UI box will change color and text to notify that no file
        has been loaded."""
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
        """
        Attributes & workflow
        -----------
        sales_results : SalesRFile instance
            Creates an instance that holds the workbook and month that
             will be written to the database. This instance holds
             class dictionary attributes of header names with empty
             values. The values will be changed to the correct column
             index through an instance of 'SalesRConfirmFormat'.
        test_format : SalesRConfirmFormat instance
            Inserts the sales_results instance as an argument, holding
            it as a composition.
        test_format.start_test()
            Performs multiple tests for checking whether the format
            of the excel sheet is viable for the database.
            Also assigns the correct column index for the required
            headers in created instance 'sales_results'

        upload_data : SalesRUpload instance
            Creates and instance that holds the workbook and month
            that will be written to the database.
        upload_data.start_upload()
            Based off the class dictionary of instance 'sales_results'
            that has the column index for each valid data, reads
            this data to the database.
        """
        sales_results = SalesRFile(self.sales_dir, self.month)

        test_format = SalesRConfirmFormat(sales_results)

        try:
            if self.data_view == "Destination View":
                test_format.start_test(test_format.file.group)
            else:
                test_format.start_test(test_format.file.local)
        except IncorrectMonth:
            raise IncorrectMonth
        except MonthNotFound:
            raise MonthNotFound
        except WrongNumberFormatting:
            raise WrongNumberFormatting
        except HeaderMissing:
            raise HeaderMissing
        print("ALL GOOD")

        upload_data = SalesRUpload(sales_results)
        upload_data.start_upload()
