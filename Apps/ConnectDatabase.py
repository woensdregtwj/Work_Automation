"""Classses and functions for connecting to the database"""
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QErrorMessage
import sqlite3
import logging

from Apps.MessageBoxes import ErrorMessage

def sql_input_check(method):
    """Decorator: Checking whether parameters meet expectations
    for the '..._show' methods"""
    def wrapper(*args):
        if not args[0].isConnected:
            raise NotConnectedError(
                "No connection established with database yet, "
                "be sure to first call 'sqlite_open()'"
            )
        try:  # Testing gui object
            getattr(args[1], args[4])
        except AttributeError:
            logging.exception("Gui object not submitted as argument.")
            ErrorMessage("Query failure: "
                         "'gui' arg is not an instance of a window, "
                         "please enter 'self' as argument for the gui.")
            return
        try:  # testing str objects
            for item in args[2:4]:
                if not isinstance(item, str):
                    raise AttributeError
            if not args[3].upper().startswith("SELECT"):
                raise InvalidQueryFormat()
        except AttributeError:
            logging.exception("'table', 'query' or 'widget' not a string")
            ErrorMessage("Query failure: "
                         "Input for arg 'table, 'query' or 'widget' "
                         "only accepts a string as an argument.")
            return
        except InvalidQueryFormat:
            logging.exception("Query has incorrect SQL syntax")
            ErrorMessage("Query failure: "
                         "Query string did not start with 'SELECT'")
            return

        return method(*args)
    return wrapper


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
        self.isConnected = False

    def sqlite_open(self):
        """Connects to the database and creates a cursor
        for executing queries through """
        self.connection = sqlite3.connect(self.dbpath)
        self.c = self.connection.cursor()

        self.isConnected = True

    def sqlite_show(
            self,
            query,
    ):
        """Communicates to several PyQt5 widgets for displaying the
        query results.

        Parameters:
            query : str, holds the SQLite3 query that will be displayed
        """
        self.c.execute(query)
        self.data_extract = self.c.fetchall()
        self.data_headers = self.c.description

    def sqlite_close(self):
        """Disconnects from the database."""
        self.c.close()
        self.connection.close()

        self.isConnected = False

    def __enter__(self):
        self.sqlite_open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sqlite_close()


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
        self.isConnected = False

    def qsql_open(self):
        """Connects to the database and creates a cursor
        for executing queries through """
        self.qsql = QSqlDatabase("QSQLITE")
        self.qsql.setDatabaseName(self.dbpath)
        self.qsql.open()

        self.query = QSqlQuery(db=self.qsql)
        self.isConnected = True

    @sql_input_check
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
            gui : class instance, main window of the pyqt5 application
            table : str, name of table in database
            query : str, query to execute
            widget : str, the attribute that holds the table widget
            edit : QSqlTableModel, save method for db adjustments
        """
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
                         + str(e) + ". Either the 'gui' argument is not"
                                    "an instance or the widget attribute"
                                    " does not exist"
                         )

    def qsql_close(self):
        """Disconnects from the database."""
        self.qsql.close()

        self.isConnected = False

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
