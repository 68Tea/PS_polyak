import sqlite3


connection = sqlite3.connect("urok10.sl3", 5)
cur = connection.cursor()
cur.execute("UPDATE first_table SET name='Lili' WHERE rowid= 4; ")
connection.commit()
connection.close()