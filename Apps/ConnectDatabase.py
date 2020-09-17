"""Classses and functions for connecting to the database"""
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QErrorMessage
import sqlite3
import traceback
import logging

from Apps.MessageBoxes import ErrorMessage

class DatabaseConnector:
    def __init__(self, database):
        """Adds argument to an attribute. Only accepts string."""
        self.dbpath = self.format_path(database)

    def format_path(self, database):
        if not database.endswith(".db"):
            raise InvalidDBExt(
                "This class only accepts '.db' file names as a string.")

        return "..\\..\\Databases\\{}".format(database)


class SQLiteAuth(DatabaseConnector):
    """Inheritance of DatabaseConnector that will connect
     "or disconnect to the SQLite database."""
    def __init__(self, database):
        super().__init__(database)
        self.sqlite_isConnected = False

    def sqlite_open(self):
        """Connects to the database and creates a cursor
        for executing queries through """
        self.connection = sqlite3.connect(self.dbpath)
        self.c = self.connection.cursor()

        self.sqlite_isConnected = True

    def sqlite_show(self, gui_window):
        if not self.sqlite_isConnected:
            raise NotConnectedError(
                "No connection established with database yet, "
                "be sure to first call 'sqlite_open()'"
            )
        self.gui_window = gui_window




    def sqlite_close(self):
        """Disconnects from the database."""
        self.c.close()
        self.connection.close()

        self.sqlite_isConnected = False

    def __enter__(self):
        self.sqlite_open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sqlite_close()

"""Try and use the context manager as much as possible for preventing
non-closed instances connections to the database."""
class QSqlAuth(DatabaseConnector):
    """Inheritance of DatabaseConnector that will connect or disconnect
    to the SQL database. This class also can perform query display
    actions for the PyQt5 GUI window. Requirement is for the attributes
    to be named the same globally."""
    def __init__(self, database):
        """Takes correct path to database file

        Parameters:
            database : str, filename that is in folder 'Databases'
                    Only requires filename, path is pre-set.
        """
        super().__init__(database)
        self.qsql_isConnected = False

    def qsql_open(self):
        """Connects to the database and creates a cursor
        for executing queries through """
        self.qsql = QSqlDatabase("QSQLITE")
        self.qsql.setDatabaseName(self.dbpath)
        self.qsql.open()

        self.query = QSqlQuery(db=self.qsql)
        self.qsql_isConnected = True

    # Maybe request user to add the names of the widgets for showing?
    # Then use getattr() for turning the input into an actual widget
    def qsql_show(
            self,
            gui,
            table,
            query,
            widget="table_data",
            edit=QSqlTableModel.OnManualSubmit
    ):
        """Communicates to several PyQt5 widgets for displaying the
        query results.

        Parameters:
            query : str, holds the SQLite3 query that will be displayed
            gui_window : class, main window of the pyqt5 application
        """
        if not self.qsql_isConnected:
            raise NotConnectedError(
                "No connection established with database yet, "
                "be sure to first call 'sqlite_open()'"
            )
        try:
            if not query.upper().startswith("SELECT"):
                raise InvalidQueryFormat()
            if not isinstance(table, str):
                raise AttributeError
        except AttributeError:
            return ("You can only insert string values.")
        except InvalidQueryFormat as i:
            logging.exception("setModel to widget failed.")
            ErrorMessage("Query input did not start with 'SELECT'")

        model = QSqlTableModel(db=self.qsql)
        model.setTable(table)
        model.setEditStrategy(edit)

        self.query.prepare(query)
        self.query.exec_()
        model.setQuery(self.query)

        try:
            getattr(gui, widget).setModel(model)
            getattr(gui, widget).resizeColumnsToContents()
        except AttributeError as e:
            logging.exception("setModel to widget failed.")
            ErrorMessage("Failed to set table with sql query: \n"
                         + str(e) + ". Please check the console.")

    def qsql_close(self):
        """Disconnects from the database."""
        self.qsql.close()

        self.qsql_isConnected = False

    def __enter__(self):
        self.qsql_open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.qsql_close()


class InvalidDBExt(Exception):
    pass

class NotConnectedError(Exception):
    pass

class InvalidQueryFormat(Exception):
    pass

if __name__ == "__main__":
    dbb = QSqlAuth("sales.db")
    dbb.qsql_open()
    dbb.qsql_close()
