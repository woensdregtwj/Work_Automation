"""Backend code for filling the database data correctly into charts
and tables into the dashboard."""
import matplotlib

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlTableModel

from Apps.ConnectDatabase import SQLiteAuth, QSqlAuth


class SalesDashboardBackend:
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

        self.prepare_dashboard()

    def prepare_dashboard(self):
        """Managing method and calls all the other methods in its
        correct order for setting up the dashboard correctly."""
        self.define_results_type()
        self.define_qsql_connections()
        self.query_chart_tables()
        self.query_ranking_tables()
        self.query_chart_data()

        self.connection.qsql_close()

    def define_results_type(self):
        """Reads the combobox result type from the window instance.
        If the combobox is on 'Destination Sales Results', then we
        prepare the dashboard with data of all entities. Else, the
        dashboard will be prepared with JP10 entity only.
        Local and Legal Results both only require JP10.

        Reads the combobox for defining what table in the database
        to read. If 'Legal View', we have to read from a different
        table as opposed to 'Destination Sales Results' and
        'Local Sales Results'.

        Attributes
        -----------
        self.result_type // self.result_type_and : str
            This attr is used for the query. If local data must be
            prepared, then we have to add a condition into the query.
            The second attr is for if there already is a 'WHERE'
            condition and we still have to add the JP10 condition.
            If we are preparing destination data, then no condition
            should be added into the query, so nothing will be
            assigned.
            """
        if self.main.results_type == "Destination Sales Results":
            self.result_type = ""
            self.result_type_and = ""
        else:
            self.result_type = "WHERE code = 'JP10'"
            self.result_type_and = f"AND code = 'JP10'"

        if self.main.results_type == "Legal View":
            self.db_table = "local"
        else:
            self.db_table = "sales"

    def define_qsql_connections(self):
        """Sets up a QSqlAuth connection that will be used by the
        other methods that require a connection for writing data
        to tables (charts will use QSqliteAuth)."""
        self.connection = QSqlAuth(self.database_used)
        self.connection.qsql_open()

    def query_chart_tables(self):
        """For the YTD and MTD tables, sends queries for writing data
        to tables. First argument that gets called before the query
        defines what table the data has to be written to.

        Contains f-strings that has attributes that either has a
        string value or not, depending on whether local data or
        destination data is set in the combobox. See method
        'define_results_type'.

        There are fixed headers that require specific data, so if
        the queries have to be adjusted, be sure to first look at
        whether the query aligns with the fixed headers in the methods
        being called within this method."""
        # Filling the YTD and MTD tables
        self.fill_chart_tables(f"YTD 1",
                               f"SELECT bu1, "
                               f"printf('%,d', (SUM(vol))), "
                               f"printf('%,d', (SUM(ns))), "
                               f"printf('%,d', (SUM(gs))), "
                               f"printf('%,d', (SUM(gm))), "
                               f"printf('%,d', (SUM(cm1))) "
                               f"FROM {self.db_table} "
                               f"{self.result_type} "
                               f"GROUP BY bu1 "
                               f"ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables(f"YTD 2",
                               f"SELECT bu2, "
                               f"printf('%,d', (SUM(vol))), "
                               f"printf('%,d', (SUM(ns))), "
                               f"printf('%,d', (SUM(gs))), "
                               f"printf('%,d', (SUM(gm))), "
                               f"printf('%,d', (SUM(cm1))) "
                               f"FROM {self.db_table} "
                               f"{self.result_type} "
                               f"GROUP BY bu2 "
                               f"ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables(f"YTD 3",
                               f"SELECT code, company, "
                               f"printf('%,d', (SUM(vol))), "
                               f"printf('%,d', (SUM(ns))), "
                               f"printf('%,d', (SUM(gs))), "
                               f"printf('%,d', (SUM(gm))), "
                               f"printf('%,d', (SUM(cm1))) "
                               f"FROM {self.db_table} "
                               f"{self.result_type} "
                               f"GROUP BY code "
                               f"ORDER BY SUM(cm1) DESC")

        self.fill_chart_tables(f"MTD 1",
                               f"SELECT bu1, "
                               f"printf('%,d', (SUM(vol))), "
                               f"printf('%,d', (SUM(ns))), "
                               f"printf('%,d', (SUM(gs))), "
                               f"printf('%,d', (SUM(gm))), "
                               f"printf('%,d', (SUM(cm1))) "
                               f"FROM {self.db_table} "
                               f"WHERE month = '{self.main.month}' "
                               f"{self.result_type_and} "
                               f"GROUP BY bu1 "
                               f"ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables(f"MTD 2",
                               f"SELECT bu2, "
                               f"printf('%,d', (SUM(vol))), "
                               f"printf('%,d', (SUM(ns))), "
                               f"printf('%,d', (SUM(gs))), "
                               f"printf('%,d', (SUM(gm))), "
                               f"printf('%,d', (SUM(cm1))) "
                               f"FROM {self.db_table} "
                               f"WHERE month = '{self.main.month}' "
                               f"{self.result_type_and} "
                               f"GROUP BY bu2 "
                               f"ORDER BY SUM(cm1) DESC")
        self.fill_chart_tables(f"MTD 3",
                               f"SELECT code, company, "
                               f"printf('%,d', (SUM(vol))), "
                               f"printf('%,d', (SUM(ns))), "
                               f"printf('%,d', (SUM(gs))), "
                               f"printf('%,d', (SUM(gm))), "
                               f"printf('%,d', (SUM(cm1))) "
                               f"FROM {self.db_table} "
                               f"WHERE month = '{self.main.month}' "
                               f"{self.result_type_and} "
                               f"GROUP BY code "
                               f"ORDER BY SUM(cm1) DESC")

    def query_ranking_tables(self):
        """For the YTD and MTD Ranking tables, sends queries for
        writing data to tables. First argument that gets called
        before the query defines what table the data has to be
        written to.

        Contains f-strings that has attributes that either has a
        string value or not, depending on whether local data or
        destination data is set in the combobox. See method
        'define_results_type'.

        There are fixed headers that require specific data, so if
        the queries have to be adjusted, be sure to first look at
        whether the query aligns with the fixed headers in the methods
        being called within this method."""
        # Filling the YTD and MTD Ranking lists
        self.fill_ranking_tables("YTD R1",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"{self.result_type} "
                                 f"GROUP BY customer, bu1 "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R2",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'PBN Plnt Based Nutr.' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R3",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'NPI Nat. Perf. Ing.' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R4",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'ISS Ing. Syst.&Sol.' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables("YTD R5",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'Others' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")

        self.fill_ranking_tables(f"MTD R1",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE month = '{self.main.month}' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer, bu1 "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R2",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'PBN Plnt Based Nutr.' "
                                 f"AND month = '{self.main.month}' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R3",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'NPI Nat. Perf. Ing.' "
                                 f"AND month = '{self.main.month}' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R4",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'ISS Ing. Syst.&Sol.' "
                                 f"AND month = '{self.main.month}' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")
        self.fill_ranking_tables(f"MTD R5",
                                 f"SELECT code, bu1, bu2, customer, "
                                 f"printf('%,d', (SUM(vol))), "
                                 f"printf('%,d', (SUM(ns))), "
                                 f"printf('%,d', (SUM(gs))), "
                                 f"printf('%,d', (SUM(gm))), "
                                 f"printf('%,d', (SUM(cm1))) "
                                 f"FROM {self.db_table} "
                                 f"WHERE bu1 = 'Others' "
                                 f"AND month = '{self.main.month}' "
                                 f"{self.result_type_and} "
                                 f"GROUP BY customer "
                                 f"ORDER BY SUM(cm1) DESC")

    def query_chart_data(self):
        """Sends queries to 2 methods that sets up pie charts and
        horizontal bar charts.
        First argument that gets called before the query
        defines what table the data has to be written to.

        Contains f-strings that has attributes that either has a
        string value or not, depending on whether local data or
        destination data is set in the combobox. See method
        'define_results_type'.

        The 1st SELECT in the query is the label, the second is
        the sum of the label. Be sure to check the chart data prep
        methods before adjusting the queries to know what exactly
        is necessary to be put into the query."""
        self.prepare_chart_data("YTD PIE 1",
                                f"SELECT bu1, SUM(ns) "
                                f"FROM {self.db_table} "
                                f"{self.result_type} "
                                f"GROUP BY bu1 "
                                f"ORDER BY SUM(ns) DESC")
        self.prepare_chart_data("YTD PIE 2",
                                f"SELECT bu1, SUM(cm1) "
                                f"FROM {self.db_table} "
                                f"{self.result_type} "
                                f"GROUP BY bu1 "
                                f"ORDER BY SUM(cm1) DESC")
        self.prepare_chart_data("YTD PIE 5",
                                f"SELECT code, SUM(ns) "
                                f"FROM {self.db_table} "
                                f"GROUP BY code "
                                f"ORDER BY SUM(ns) DESC")
        self.prepare_chart_data("YTD PIE 6",
                                f"SELECT code, SUM(cm1) "
                                f"FROM {self.db_table} "
                                f"GROUP BY code "
                                f"ORDER BY SUM(cm1) DESC")

        self.prepare_bar_chart_data("YTD PIE 3",
                                    f"SELECT bu2, SUM(ns) "
                                    f"FROM {self.db_table} "
                                    f"{self.result_type} "
                                    f"GROUP BY bu2 "
                                    f"ORDER BY SUM(ns) ASC")
        self.prepare_bar_chart_data("YTD PIE 4",
                                    f"SELECT bu2, SUM(cm1) "
                                    f"FROM {self.db_table} "
                                    f"{self.result_type} "
                                    f"GROUP BY bu2 "
                                    f"ORDER BY SUM(cm1) ASC")

        self.prepare_chart_data("MTD PIE 1",
                                f"SELECT bu1, SUM(ns) "
                                f"FROM {self.db_table} "
                                f"WHERE month = '{self.main.month}' "
                                f"{self.result_type_and} "
                                f"GROUP BY bu1 "
                                f"ORDER BY SUM(ns) DESC")
        self.prepare_chart_data("MTD PIE 2",
                                f"SELECT bu1, SUM(cm1) "
                                f"FROM {self.db_table} "
                                f"WHERE month = '{self.main.month}' "
                                f"{self.result_type_and} "
                                f"GROUP BY bu1 "
                                f"ORDER BY SUM(cm1) DESC")
        self.prepare_chart_data("MTD PIE 5",
                                f"SELECT code, SUM(ns) "
                                f"FROM {self.db_table} "
                                f"WHERE month = '{self.main.month}' "
                                f"GROUP BY code "
                                f"ORDER BY SUM(ns) DESC")
        self.prepare_chart_data("MTD PIE 6",
                                f"SELECT code, SUM(cm1) "
                                f"FROM {self.db_table} "
                                f"WHERE month = '{self.main.month}' "
                                f"GROUP BY code "
                                f"ORDER BY SUM(cm1) DESC")

        self.prepare_bar_chart_data("MTD PIE 3",
                                    f"SELECT bu2, SUM(ns) "
                                    f"FROM {self.db_table} "
                                    f"WHERE month = '{self.main.month}' "
                                    f"{self.result_type_and} "
                                    f"GROUP BY bu2 "
                                    f"ORDER BY SUM(ns) ASC")
        self.prepare_bar_chart_data("MTD PIE 4",
                                    f"SELECT bu2, SUM(cm1) "
                                    f"FROM {self.db_table} "
                                    f"WHERE month = '{self.main.month}' "
                                    f"{self.result_type_and} "
                                    f"GROUP BY bu2 "
                                    f"ORDER BY SUM(cm1) ASC")

    def fill_chart_tables(self, table_push, query_push):
        """Creates the charts, contains a lot of styling methods
        from QsqlTable.

        Parameters
        -----------
        table_push : str
            Must hold a string that is the same as one of the keys in
            dict 'assign_tables'. The value of the key will be used
            for writing the data into the table.
        query_push : str
            A query that grabs the necessary data for the headers."""
        assign_tables = {"YTD 1": self.main.ytd_b2b1_table,
                         "YTD 2": self.main.ytd_b2b2_table,
                         "YTD 3": self.main.ytd_le_table,
                         "MTD 1": self.main.mtd_b2b_table1,
                         "MTD 2": self.main.mtd_b2b_table2,
                         "MTD 3": self.main.mtd_le_table
                         }

        self.model = QSqlTableModel(db=self.connection.qsql)
        self.model.setTable(self.db_table)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.connection.query.prepare(query_push)
        self.connection.query.exec_()
        self.model.setQuery(self.connection.query)

        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Volume")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Net Sales")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Gross Sales")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Gross Margin")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "CM 1")

        if table_push == "YTD 3" or table_push == "MTD 3":
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "LE")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "LE Name")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Volume")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Net Sales")
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Gross Sales")
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Gross Margin")
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, "CM 1")
            assign_tables[table_push].setModel(self.model)
            scale_to_tableframe = assign_tables[table_push].horizontalHeader()
            scale_to_tableframe.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeToContents)
            scale_to_tableframe.setSectionResizeMode(
                1, QtWidgets.QHeaderView.Stretch
            )
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "BU Level 1")
            assign_tables[table_push].setModel(self.model)
            scale_to_tableframe = assign_tables[table_push].horizontalHeader()
            scale_to_tableframe.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeToContents)
            scale_to_tableframe.setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch
            )
        else:
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "BU Level 1")
            assign_tables[table_push].setModel(self.model)
            scale_to_tableframe = assign_tables[table_push].horizontalHeader()
            scale_to_tableframe.setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeToContents)
            scale_to_tableframe.setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch)
            scale_to_tableframe.setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch)

    def fill_ranking_tables(self, table_push, query_push):
        """Creates the charts, contains a lot of styling methods
        from QsqlTable.

        Parameters
        -----------
        table_push : str
            Must hold a string that is the same as one of the keys in
            dict 'assign_tables'. The value of the key will be used
            for writing the data into the table.
        query_push : str
            A query that grabs the necessary data for the headers."""
        assign_tables = {"YTD R1": self.main.ytd_top_table,
                         "YTD R2": self.main.ytd_top_bu1_table,
                         "YTD R3": self.main.ytd_top_bu2_table,
                         "YTD R4": self.main.ytd_top_bu3_table,
                         "YTD R5": self.main.ytd_top_bu4_table,

                         "MTD R1": self.main.mtd_top_table,
                         "MTD R2": self.main.mtd_top_bu1_table,
                         "MTD R3": self.main.mtd_top_bu2_table,
                         "MTD R4": self.main.mtd_top_bu3_table,
                         "MTD R5": self.main.mtd_top_bu4_table}

        self.model = QSqlTableModel(db=self.connection.qsql)
        self.model.setTable(self.db_table)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.connection.query.prepare(query_push)
        self.connection.query.exec_()
        self.model.setQuery(self.connection.query)

        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "LE")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "BU1")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "BU2")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Customer")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Vol")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "N. Sales")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "G. Sales")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "G. Marg")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "CM1")

        assign_tables[table_push].setModel(self.model)
        scale_to_tableframe = assign_tables[table_push].horizontalHeader()

        """Only resizes specific columns in the table. These columns
        are not identified by name, but by index."""
        for column in [0, 4, 5, 6, 7, 8]:
            scale_to_tableframe.setSectionResizeMode(
                column, QtWidgets.QHeaderView.ResizeToContents
            )

    def prepare_chart_data(self, chart_push, query_push):
        """Creates the charts, contains a lot of styling methods
        from matplotlib.

        Parameters
        -----------
        chart_push : str
            Must hold a string that is the same as one of the keys in
            dict 'assign_tables'. The value of the key will be used
            for writing the data into the table.
        query_push : str
            A query that grabs the necessary data for the headers."""
        assign_charts = {"YTD PIE 1": self.main.ytd_b2b1_chart1,
                         "YTD PIE 2": self.main.ytd_b2b1_chart2,
                         "YTD PIE 3": self.main.ytd_b2b2_chart1,
                         "YTD PIE 4": self.main.ytd_b2b2_chart2,
                         "YTD PIE 5": self.main.ytd_le_chart1,
                         "YTD PIE 6": self.main.ytd_le_chart2,

                         "MTD PIE 1": self.main.mtd_b2b1_chart1,
                         "MTD PIE 2": self.main.mtd_b2b1_chart2,
                         "MTD PIE 3": self.main.mtd_b2b2_chart1,
                         "MTD PIE 4": self.main.mtd_b2b2_chart2,
                         "MTD PIE 5": self.main.mtd_le_chart1,
                         "MTD PIE 6": self.main.mtd_le_chart2
                         }
        assign_titles = {"YTD PIE 1": "Net Sales B2B Level 1 - YTD",
                         "YTD PIE 2": "CM1 B2B Level 1 - YTD",
                         "YTD PIE 3": "Net Sales B2B Level 2 - YTD",
                         "YTD PIE 4": "CM1 B2B Level 2- YTD",
                         "YTD PIE 5": "Net Sales Legal Entity - YTD",
                         "YTD PIE 6": "CM1 Legal Entity - YTD",

                         "MTD PIE 1": "Net Sales B2B Level 1 - MTD",
                         "MTD PIE 2": "CM1 B2B Level 1 - MTD",
                         "MTD PIE 3": "Net Sales B2B Level 2 - MTD",
                         "MTD PIE 4": "CM1 B2B Level 2 - MTD",
                         "MTD PIE 5": "Net Sales Legal Entity - MTD",
                         "MTD PIE 6": "CM1 Legal Entity - MTD"
                         }

        with SQLiteAuth(self.database_used) as datab:
            datab.sqlite_show(query_push)
            data = datab.data_extract

        """A list in list, so we need nested comprehension to grab the
        necessary information."""
        chart_labels_legend = [i for i in data for i in i if
                               isinstance(i, str)]
        chart_data = [i for i in data for i in i if isinstance(i, int)]

        """the total amount of data is necessary for
        calculating percentages."""
        summed_data = 0
        for amt in chart_data:
            summed_data += amt
        percentages = [
            round(float(p / summed_data * 100), 1) for p in chart_data
        ]

        """For the LE pie chart, we only want to show JP10 in the chart"""
        if "JP10" in chart_labels_legend:
            chart_labels_chart = [
                "" if i != "JP10" else "JP10" for i in chart_labels_legend
            ]
        else:
            chart_labels_chart = chart_labels_legend

        """Changes label string formatting so that percentage
        is shown behind the string."""
        chart_labels_legend = [
            '%s, %1.1f %%' % (l, s) for l, s in zip(
                chart_labels_legend, percentages
            )
        ]
        """Cant put minus values in a pie. Just put to 0"""
        for index, value in enumerate(chart_data):
            if value < 0:
                chart_data[index] = 0

        chart_figure = Figure()
        chart_canvas = FigureCanvasQTAgg(chart_figure)
        chart_final = chart_figure.add_subplot(111)

        chart_final.pie(chart_data,
                        labels=chart_labels_chart,
                        startangle=180,
                        autopct=self.autopct
                        )
        chart_final.set_title(
            label=assign_titles[chart_push],
            fontsize=16
        )
        chart_final.legend(
            labels=chart_labels_legend,
            loc="upper left",
            bbox_to_anchor=(-1.65, 1.25),
            fontsize=8)
        chart_figure.patch.set_facecolor("#E6E6E6")

        chart_figure.subplots_adjust(left=0.4, top=0.8)

        chart_canvas.show()

        assign_charts[chart_push].addWidget(chart_canvas)

    def prepare_bar_chart_data(self, chart_push, query_push):
        """Creates the charts, contains a lot of styling methods
        from matplotlib.

        Parameters
        -----------
        chart_push : str
            Must hold a string that is the same as one of the keys in
            dict 'assign_tables'. The value of the key will be used
            for writing the data into the table.
        query_push : str
            A query that grabs the necessary data for the headers."""
        assign_charts = {"YTD PIE 3": self.main.ytd_b2b2_chart1,
                         "YTD PIE 4": self.main.ytd_b2b2_chart2,
                         "MTD PIE 3": self.main.mtd_b2b2_chart1,
                         "MTD PIE 4": self.main.mtd_b2b2_chart2}
        assign_titles = {"YTD PIE 3": "Net Sales B2B Level 2 - YTD",
                         "YTD PIE 4": "CM1 B2B Level 2 - YTD",
                         "MTD PIE 3": "Net Sales B2B Level 2 - MTD",
                         "MTD PIE 4": "CM1 B2B Level 2 - MTD"}

        with SQLiteAuth(self.database_used) as datab:
            datab.sqlite_show(query_push)
            data = datab.data_extract

        """A list in list, so we need nested comprehension to grab the
        necessary information."""
        chart_labels = [i for i in data for i in i if
                        isinstance(i, str)]  # A list in list, so we need nested comprehension
        chart_data = [i for i in data for i in i if isinstance(i, int)]

        """the total amount of data is necessary for
        calculating percentages."""
        summed_data = 0
        for amt in chart_data:
            summed_data += amt
        percentages = [
            round(float(p / summed_data * 100), 1) for p in chart_data
        ]

        """Changes label string formatting so that percentage
        is shown behind the string."""
        chart_labels_pct = [
            '%s, %1.1f %%' % (l, s) for l, s in zip(
                chart_labels, percentages
            )
        ]

        """Cant put minus values in a pie. Just put to 0"""
        for index, value in enumerate(chart_data):
            if value < 0:
                chart_data[index] = 0

        chart_figure = Figure()
        chart_canvas = FigureCanvasQTAgg(chart_figure)
        chart_final = chart_figure.add_subplot(111)

        chart_final.barh(chart_labels_pct, percentages)

        chart_final.set_title(assign_titles[chart_push], fontsize=16)
        chart_final.tick_params(axis="both", labelsize=8)
        chart_figure.patch.set_facecolor("#E6E6E6")
        chart_final.patch.set_facecolor("#E6E6E6")

        chart_figure.subplots_adjust(left=0.3, right=0.9)

        chart_canvas.show()

        assign_charts[chart_push].addWidget(chart_canvas)

    def autopct(self, pct):
        return ('%1.1f%%' % pct) if pct > 12 else ''

