#Se importa la base de datos para luego ser conectada y creada
import sqlite3
con = sqlite3.connect("DataBase.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,telefono INTEGER,email TEXT,ciudad TEXT,direccion TEXT)""")
con.commit()