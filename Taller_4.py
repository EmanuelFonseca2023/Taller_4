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
#La interfaz del usuario con todas las opciones que este puede hacer
while True:
    x=int(input("""
Que te gustaria hacer en la base de datos.
    0.Cerrar el programa
    1.Crear un usuario
    2.Mostrar Base de datos
    3.Actualizar informacion de un usuario
    4.Borrar Usuario
    Que te gustaria hacer? 
                """))
    if x==0:
        print("Muchas gracias por usar nuestra aplicacion")
        break
    elif x==1:
        datos=list(input("Para añadir un usuario tienes que escribir el nombre, telefono, email,cidad,direccion separado por una , ").split(","))
        create_users(datos[0].strip(), int(datos[1]),datos[2].strip(),datos[3].strip(),datos[4].strip())
        continue
    elif x==2:
        print(leer_users())
        continue
    elif x==3:
        y=int(input("""Que datos te gustaria actualizar
   0.Todos
   1.Telefono
   2.Email
   Oprime cualquier numero para regresar al menu anterior
   Elige uno"""))
        if y == 0:
            datos=list(input("Se modifica todo asi que dame el id ,telefono, email, ciudad,direccion todos separados por , ").split(","))
            actualizar_users(int(datos[0]),int(datos[1]),datos[2].strip,datos[3].strip(),datos[4].strip())
            continue
        elif y == 1:
            datos=list(input("Se modifica el telefono asi que danos la id y el telefono separada por una ,").split(","))
            actualizar_telefono(int(datos[0]), int(datos[1]))
            continue
        elif y == 2:
            datos=list(input("Se modifica el telefono asi que danos la id y el email separada por una ,").split(","))
            actualizar_email(int(datos[0]), datos[1])
        else:
            print("Se regresara a la pantalla anterior")
            continue
            
        continue
    elif x==4:
        datos=int(input("Que usuario quiere borrar? "))
        borrar_users(datos)
        continue
    else:
        print("Opcion invalida")
        continue
    
con.close()