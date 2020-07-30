import openpyxl as pyxl
from openpyxl.styles import *
import datetime
import re

def lto_date_format(lto_file):
    lto_wb = pyxl.load_workbook(lto_file)
    lto_ws = lto_wb.active

    if not lto_ws["A1"].value:
        lto_ws.delete_rows(1)
        lto_ws.delete_rows(2)
        lto_ws["Q1"].value = "Potential (EURk)"
        lto_ws["R1"].value = "Volume in k"
        lto_ws.auto_filter.ref = lto_ws.dimensions

    for cell in range(2, lto_ws.max_row + 1):
        for column in range(10, 13):
            try:
                date = datetime.datetime.strptime(lto_ws.cell(row=cell, column=column).value, "%d.%m.%Y")
                lto_ws.cell(row=cell, column=column).value = date.strftime("%Y/%m/%d")
            except:
                if re.search("\d\d\d\d", lto_ws.cell(row=cell, column=column).value):
                    print(f"Date already was correct - {lto_ws.cell(row=cell, column=column).value} \
                     {lto_ws.cell(row=cell, column=1).value}")
                else:
                    print(f"Expected a date, but found {lto_ws.cell(row=cell, column=column).value}. \
                     Marking the cell red for checking.")
                    redFill = PatternFill(start_color='00FF0000', end_color='00FF0000', fill_type='solid')
                    lto_ws.cell(row=cell, column=column).fill = redFill
                continue

    for col in ["D", "E", "G", "H", "J", "K", "M", "N", "O", "P"]:
        if not lto_ws.column_dimensions[col].hidden:
            lto_ws.column_dimensions[col].hidden = True

    return lto_wb





