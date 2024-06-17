import sqlite3

def conectar():
    conn=sqlite3.connect("datos.db")
    return conn

def crear_tabla(conn):
    try:# probar
        c= conn.cursor()#para realizar accciones de insercion, modificacion
        c.execute(""" CREATE TABLE IF NOT EXISTS contacto (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)""")
        conn.commit()
        
    except Exception as e:#en caso de dar un error 
        print (f" ha ocurrido un error al crear la tabla:{e}")#e nombre del error
            
def insertar(conn, nombre, edad):
    try:
       c= conn.cursor()
       c.execute("INSERT INTO contacto(nombre,edad) values(?,?)",(nombre,edad))
       conn.commit()
    except Exception as e:
        print (f"ha ocurrido un error al insertar : {e}")
        
        
def leer(conn):
    try:
        c= conn.cursor()
        c.execute("SELECT * FROM contacto")
        filas= c.fetchall()#permite capturar todos los elemntos que devuelve sql
        for fila in filas:
            print(fila)
    except Exception as e :
        print (f" ha ocurrido un error al actualizar :{e}")
        

def actualizar (conn,id,nombre,edad):
    try:
        c= conn.cursor()
        c.execute ("UPDATE contacto SET nombre=?, edad=? WHERE id=?",(nombre,edad,id))
        conn.commit()
    except Exception as e:
        print(f"ha ocurrido un error al actualizar : {e}")
        
def eliminar (conn,id):
    try:
        c= conn.cursor()
        c.execute("DELETE FROM contacto WHERE id=?", (id,))
        conn.commit()
    except Exception as e:
        print(f"ha ocurrido un error al eliminar :{e}")
def menu():
    conn= conectar()
    crear_tabla(conn)
    while True:
        print("\n 1.- Insertar nuevo Registro")
        print("2.-Leer Registros Existentes")
        print("3.-Actualizar un Registro")
        print("4.- Eliminar un Registro")
        print("5.-Salir")
        opcion=input("Elige una opcion:")
        if opcion== "1":
            nombre=input("ingrese el nombre:")
            edad=input (" ingrese la edad: ")
            insertar(conn,nombre, edad)
        elif opcion== "2":
            leer(conn)
        elif opcion== "3":
            id= int(input("Ingresa el id del registro a actualizar:"))
            nombre=input("Ingresa el nuevo nombre:")
            edad=int(input("Ingresa la nueva edad"))
            actualizar(conn, id, nombre, edad)
        elif opcion== "4":
            id=int(input("Ingresa el id del registro a eliminar"))
            eliminar(conn,id)
        elif opcion== "5":
            print("saliendo del programa")
            break
        else:
            print("opcion no valida Por favor intenta de nuevo...")
    conn.close()
menu()
            
            

        
        