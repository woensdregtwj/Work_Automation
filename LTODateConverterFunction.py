import openpyxl as pyxl
import datetime

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
            date = datetime.datetime.strptime(lto_ws.cell(row=cell, column=column).value, "%d.%m.%Y")
            lto_ws.cell(row=cell, column=column).value = date.strftime("%Y/%m/%d")

    for col in ["D", "E", "G", "H", "J", "K", "M", "N", "O", "P"]:
        lto_ws.column_dimensions[col].hidden = True

    return lto_wb





