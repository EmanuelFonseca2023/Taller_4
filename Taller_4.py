#Se importa la base de datos para luego ser conectada y creada
import sqlite3
con = sqlite3.connect("DataBase.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,telefono INTEGER,email TEXT,ciudad TEXT,direccion TEXT)""")
con.commit()
#Se crean las funciones CRUD
def create_users(name,telefono,email,ciudad,direccion):
    cur.execute("INSERT INTO users(name,telefono,email,ciudad,direccion) VALUES (?,?,?,?,?)",(name,telefono,email,ciudad,direccion))
    con.commit()
def leer_users():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()
def actualizar_users(id,telefono,email,ciudad,direccion):
    cur.execute("UPDATE users SET telefono=? ,email=?,ciudad=?,direccion=? WHERE id =?",(telefono,email,ciudad,direccion,id))
    con.commit()
def actualizar_telefono(id,telefono):
    cur.execute("UPDATE users SET telefono=? WHERE id =?",(telefono,id))
    con.commit()
def actualizar_email(id,email):
    cur.execute("UPDATE users SET email=? WHERE id =?",(email,id))
    con.commit()
def borrar_users(id):
    cur.execute("DELETE FROM users WHERE id =?",(id,))
    con.commit()