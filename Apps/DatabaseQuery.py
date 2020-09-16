"""Facade pattern that will omit all the boilerplate code in the main
window's module. Class below will use ConnectDatabase for establishing
a connection with the database. The class also requires the widget
names in the main window's module to be the same."""

# TODO - Exception raised for when widget name differs from format

class QueryDatabase:
    """Connects and queries a database for displaying
    data in a Qsql widget on PyQt5

    Attributes:
        database (str): filename of database
        window (cls): class of the window with sql widgets
    """
    def __init__(self, window, database, dbtype):
        # main window class (self)
        # database file

        # How do we know whether we want to query from Qsql or sqlite3?
        # either qsql or sqlite3, if other type was given give an exception
            # have a fixed dictionary above __init__ that holds something for qsql or sqlite


