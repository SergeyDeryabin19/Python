# list of products to buy
import sqlite3 as sq
with sq.connect("product_list.db") as con:
    cur=con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS prod_list (
        name TEXT,
        condition TEXT,
        quantity INTEGER,
        need_now TEXT
    )
    """)