"""Classses and functions for connecting to the database"""
from PyQt5.QtSql import QSqlDatabase
import sqlite3

import os

class DatabaseConnector:
    def __init__(self, database):
        """Adds argument to an attribute. Only accepts string."""
        self.dbpath = self.format_path(database)

        self.qsql_isConnected = False
        self.sqlite_isConnected = False

    def format_path(self, database):
        if not database.endswith(".db"):
            raise InvalidDBExt(
                "This class only accepts '.db' file names as a string.")

        return "{}\\Databases\\{}".format(
            os.path.dirname(os.path.abspath(__file__)), database
        )


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


class QSqlAuth(DatabaseConnector):
    """Inheritance of DatabaseConnector that will connect
     "or disconnect to the SQLite database."""
    def __init__(self, database):
        super().__init__(database)
        self.qsql_isConnected = False

    def qsql_open(self):
        """Connects to the database and creates a cursor
        for executing queries through """
        self.qsql = QSqlDatabase("SQLITE")
        self.qsql.setDatabaseName(self.dbpath)
        self.qsql.open()

        self.qsql_isConnected = True

    def qsql_close(self):
        """Disconnects from the database."""
        self.qsql.close()

        self.qsql_isConnected = False

    def __enter__(self):
        self.qsql_open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.qsql_close()

# TODO - Implement error handling for if we are not connected to the db;
"""sqlite3 already has some error handling for closed db's
so we only have to implement documentation?"""
class InvalidDBExt(Exception):
    pass

class NotConnectedError(Exception):
    pass
