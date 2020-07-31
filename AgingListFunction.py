import openpyxl as pyxl
import datetime
import sqlite3

wb = pyxl.load_workbook("C:\\Users\\woens\\Desktop\\July Reporting\\Aging list\\142_AR_2007.xlsx")
ws = wb.active  # Original file will only have 1 sheet, so you can use ws = wb.active

upload_wb = pyxl.load_workbook("Excel Templates\\Receivables_Upload.xlsx")
upload_ws = upload_wb.active

conn = sqlite3.connect("Databases\\payment_terms.db")
c = conn.cursor()
# Database columns are: customer, id, term

reporting_month = 7  # Change this into being an argument for the function.
reporting_type = 12  # Change this into being an argument for the function

payment_data = {}  # Data structure will be {customerid: Account Receivable}
delete_payment_data = []  # Duplicates with "-1" in its cusid will be concatenated to its original and deleted

# Defining the starting row with data. According to the GX file output.
# It starts at row with string "Accounts Receivable" on column B.

for row in range(1, ws.max_row + 1):
    if ws.cell(row=row, column=1).value == "142" and ws.cell(row=row, column=2).value == "Accounts Receivable":
        starting_row = row
        break

# From starting_row, we loop over each customerid and AR amount and add this to our dictionary.
for row in range(starting_row, ws.max_row + 1):
    if not ws.cell(row=row, column=6).value and not ws.cell(row=row + 1, column=6).value:
        print("Reached the end, exiting loop")
        break
    payment_data.setdefault(ws.cell(row=row, column=6).value, ws.cell(row=row, column=10).value)

# Now we look for keys with "-" in its name, we have to delete these and concatinate the value to the key without "-"
for dup_data in payment_data.keys():
    if "-" in dup_data:
        original_data = dup_data.split("-")
        payment_data[original_data[0]] += payment_data[dup_data]

        delete_payment_data.append(dup_data)

# We delete the keys with "-" from our dictionary, as we concatinated the amount to its non "-" key
for dup_data in delete_payment_data:
    print(f"Deleting {dup_data} from our data")
    del payment_data[dup_data]

# Now that we have the data for being written to the upload template, we can start pasting the dictionary.
paste_in_row = 2
for key, value in payment_data.items():
    paste_row = [datetime.datetime.now().year, reporting_month, key, 3900, "JPY", "", reporting_type, "Legal", 0, 0, 0,
                 0, value, value, 0, 0, 0, 0, 0, 0, 0, 0]  # This is 1 row to be pasted. There are a lot of default
    # data, so change here if any values have to be changed. The empty "" is where we will paste the payment term
    print(f"Pasting in row {paste_in_row} - {paste_row}")

    for index, paste_value in enumerate(paste_row):
        upload_ws.cell(row=paste_in_row, column=index + 1).value = paste_value
    paste_in_row += 1

# Here we call the payment_terms.db and match the correct payment terms with its SAP customer number code;
# If the SAP code is not in the database, then assign it as 60

for term_cell in range(2, len(payment_data) + 2):
    match_term = upload_ws.cell(row=term_cell, column=3).value

    c.execute("SELECT term FROM terms WHERE id = ?", (match_term,))
    is_matched = c.fetchall()

    try:
        if not is_matched:
            print("Not matched, payment term will be 60 days")
            upload_ws.cell(row=term_cell, column=6).value = 60
        else:
            print(f"{match_term} has a payment term of {is_matched}")
            upload_ws.cell(row=term_cell, column=6).value = str(is_matched).strip("'[(,)]'")
    except:
        print(f"{is_matched} - Is this a duplicate?")
        # return False

# return workbook
# return how many duplicates were deleted from the sql database.
# if we ever had to delete a duplicate, then it means that it the database should be checked for mistakes!!!!

# Do we really need this?
def delete_duplicates():
    c.execute("SELECT id FROM terms")
    check_data = c.fetchall()

    for data in check_data:
        if check_data.count(data) > 1:
            c.execute("SELECT * FROM terms WHERE id = ?", data)
            fix_duplicate = c.fetchall()

            return data  # Found a duplicate, has to be fixed

    return False
