import sqlite3
import openpyxl as pyxl
from LTODateConverterFunction import *

def format_test(sheet):
    test_sheet = sheet
    test_column_headers = ["Opportunity ID", "Opportunity Name", "Customer", "Region", "Area",
                           "Customer Responsibility", "Döhler Opportunity", "Customer Opportunity",
                           "Opportunity Stage", "Stage Start Date", "Start Date", "Launch Date",
                           "Diamond Project", "Project Importance", "Development Order ID",
                           "Development Order Status", "Potential (EURk)", "Volume in k"]

    # Test 1, checking headers
    for index, header in enumerate(test_column_headers):
        if header != test_sheet.cell(row=1, column=index + 1).value:
            print("Headers correct, data should be OK")
            return True
        else:
            return False


def updateLTO(workbook):
    connect = sqlite3.connect("databases\\LTO.db")
    c = connect.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS lto (id INT, name TEXT, cus TEXT, kam TEXT, stage TEXT, "
              "launch DATE, sales INT, vol INT, status TEXT, comment TEXT)")

    wb = lto_date_format(workbook)  # Using the function lto_date_format from our LTO date converter
    ws = wb.active

    # Concatenating each change of the database, will return this
    new_adds = 0
    existing_adds = 0
    closed_adds = 0

    c.execute("SELECT id FROM lto")
    data = c.fetchall()

    existing_data = []  # Will append all existing opportunity IDs in order to prevent overwriting existing data
    for opp_id in range(len(data)):
        existing_data.append(data[opp_id][0])

    # Section for checking whether the template has the correct data usage
    is_correct_template = format_test()

    for cell in range(2, ws.max_row + 1):
        if not is_correct_template:
            break

        id = int(ws.cell(row=cell, column=1).value)
        name = ws.cell(row=cell, column=2).value
        cus = ws.cell(row=cell, column=3).value
        kam = ws.cell(row=cell, column=6).value
        stage = ws.cell(row=cell, column=9).value
        launch = ws.cell(row=cell, column=12).value
        sales = ws.cell(row=cell, column=17).value
        vol = ws.cell(row=cell, column=18).value
        status = "None"
        comment = "None"

        data_holder = [id, name, cus, kam, stage, launch, sales, vol, status,
                       comment]  # Change this to create this when opp id is new

        # Testing the opportunity ID for if it already is in the database, will update BUT keep the comment and status
        if id in existing_data:
            existing_adds += 1
            data_exist = [name, cus, kam, stage, launch, sales, vol, id]
            c.execute("UPDATE lto SET name = ?, "
                      "cus = ?, "
                      "kam = ?, "
                      "stage = ?, "
                      "launch = ?, "
                      "sales = ?, "
                      "vol = ? WHERE id = ?", data_exist)
            connect.commit()
        else:
            new_adds += 1
            data_new = [id, name, cus, kam, stage, launch, sales, vol, status, comment]
            c.execute("INSERT INTO lto VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data_new)
            connect.commit()

    c.execute("SELECT * FROM lto")
    data = c.fetchall()
    print(f"New added: {new_adds}\nExisting adjusted: {existing_adds}\nTotal in Table: {len(data)}")
