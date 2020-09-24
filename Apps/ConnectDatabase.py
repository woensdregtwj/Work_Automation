"""Classses and functions for connecting to the database"""
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QErrorMessage
import sqlite3
import logging

from Apps.MessageBoxes import ErrorMessage
from Apps.ErrorClass import (
    InvalidDBExt, InvalidQueryFormat, NotConnectedError)

def sql_input_check(method):
    """Decorator: Checking whether parameters meet expected input
    for the '..._show' method in the 'QsqlAuth' class.

    Except errors
    ---------------
    AttributeError - Wrong GUI instance inserted
    AttributeError - 'table', 'query', 'widget' not a str
    InvalidQueryFormat - query did not start with 'SELECT'"""
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
    """Holds file directory of database.
    Subclassed by 'SQLiteAuth' and 'QSqlAuth'"""
    def __init__(self, database):
        """Adds argument to an attribute. Only accepts string."""
        self.dbpath = self.format_path(database)

    def format_path(self, database):
        if not database.endswith(".db"):
            raise InvalidDBExt(
                "This class only accepts '.db' file names as a string.")

        return "Databases\\{}".format(database)


class SQLiteAuth(DatabaseConnector):
    """Inheritance of DatabaseConnector that will connect
     "or disconnect to the SQLite database."""
    def __init__(self, database):
        """From Superclass, grabs the database file directory.

        Parameters:
            database : str, filename that is in folder 'Databases'
                    Only requires filename, path is pre-set.

        Attribute:
            self.isConnected, False at startup, db not opened yet."""
        super().__init__(database)
        self.isConnected = False

    def sqlite_open(self):
        """Connects to the database.

        Attributes
        -----------
        self.connection : sqlite3 instance
            Calls '.connect' method and opens db.
        self.c : self.connection instance
            Creates a cursor instance.
        self.isConnected : True
            Changes attribute to True due to active connection.

        Usage
        -----------
        Obj.c.execute() to send a query
        Obj.connection.commit() to commit changes to db"""
        self.connection = sqlite3.connect(self.dbpath)
        self.c = self.connection.cursor()

        self.isConnected = True

    def sqlite_show(self, query):
        """Communicates to several PyQt5 widgets for displaying the
        query results or for own use by calling attributes of method.

        Parameters
        -----------
        query : str
            holds the SQLite3 query that will be displayed.

        Attributes
        -----------
        self.data_extract : cursor.fetchall list
            Holds the data based on the query input by user.
        self.data_headers : cursor.description list
            Holds the headers of data based on query input by user.

        Usage
        -----------
        Either use a context manager or manually call
        'sqlite_open' for establishing a db connection. Then call this
        method with a query as parameter.
        Call attr Obj.data_extract for obtaining the data of the query
        Call attr Obj.data_headers for obtaining the headers"""
        self.c.execute(query)
        self.data_extract = self.c.fetchall()
        self.data_headers = self.c.description

    def execute_query(self, query, parameter=None):
        """Executes a query that changes something in the database
        and that requires a .commit().

        Parameters
        -----------
        query : str
            Query that adjusts the db e.g. DELETE / CREATE / INSERT
        parameter : data container
            Holds a data container that is used for queries.
        """
        if not parameter:
            self.c.execute(query)
        else:
            self.c.execute(query, parameter)
        self.connection.commit()

    def sqlite_close(self):
        """Disconnects from the database.
        Closes cursor and connection."""
        self.c.close()
        self.connection.close()

        self.isConnected = False

    def __enter__(self):
        """Context Manager setup."""
        self.sqlite_open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager setup."""
        self.sqlite_close()


class QSqlAuth(DatabaseConnector):
    """Inheritance of DatabaseConnector that will connect or disconnect
    to the SQL database. This class also can perform query display
    actions for the PyQt5 GUI window. Requirement is for the attributes
    to be named the same globally."""

    def __init__(self, database):
        """From Superclass, grabs the database file directory.

        Parameters:
            database : str, filename that is in folder 'Databases'
                    Only requires filename, path is pre-set.

        Attribute:
            self.isConnected, False at startup, db not opened yet."""
        super().__init__(database)
        self.isConnected = False

    def qsql_open(self):
        """Connects to the database and creates a cursor
        for executing queries.

        Usage
        -----------
        You can request queries by Obj.query.prepare(query), however
        qsql queries are mainly used for setting up models in widgets
        in method 'self.qsql_show'. If you need a data container based
        off inserted query, use class 'SQLiteAuth' instead."""
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

        Attributes
        -----------
        model : QSqlTableModel
            QSqlTableModel instance with parameter being the qsql
            connection from method 'qsql_open'.
        model.setTable(table) : QSqlTableModel.setTable()
            From method parameter 'table', which is the name of table
            in database. Sets this as main table in attr 'model'.
        model.setEditStrategy: QSqlTableModel.setEditStrategy()
            Sets the save method for adjustments made by the user
            through the table widget.
        self.query.prepare : QSqlQuery
            Grabs parameter 'query' and communicates to database
        self.query.exec_ : QSqlQuery
            Executes the prepared query, saves it in 'self.query'
        model.setQuery : QSqlTableModel
            Writes the data obtained from the query to the QSqlTable

        Getattr section
        -----------
        getattr(gui, widget).setModel(model)
            turns 'widget' parameter from str into a working attribute
            from the gui instance. This widget usually is a table data
            and we '.setModel' the recent created model with data
            based off self.query.
        getattr(gui, widget).resizeColumnsToContents()
            Resizes to fit columns to contents with the same
            methodology as mentioned in the first getattr call.

        Error handling
        -----------
        AttributeError
            At getattr() calls, if this error occurs, then the widget
            most likely was typed wrongly/could not be found.

        Usage
        -----------
        Within a context manager or manual open/close, all you have
        to do is call this method and fill in the correct parameters.
        Everything else is done within this method automatically.
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