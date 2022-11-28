import sqlite3
from db.create_db import create_tables_for_sql

conn = sqlite3.connect('database.db')
cur = conn.cursor()
create_tables_for_sql(cur, conn)