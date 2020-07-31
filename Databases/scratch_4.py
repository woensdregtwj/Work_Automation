import sqlite3
import aging_payment_terms as terms
import pprint

conn = sqlite3.connect("payment_terms.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS terms (customer TEXT, id TEXT, term INT)")

for key, value in terms.payment_term.items():
    insert = ["EDIT", key, value]
    c.execute("INSERT INTO terms VALUES (?, ?, ?)", insert)
    conn.commit()

c.close()
conn.close()
