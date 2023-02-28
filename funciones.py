import MySQLdb
import sys

#archivo 4 funciona ok no tocar mas ni borrar
db = MySQLdb.connect("localhost","andres1","andres1","proyectopython")


def conectar():
    try:
        db = MySQLdb.connect("localhost","andres1","andres1","proyectopython")
    except MySQLdb.Error as e:
        print("Error, no se ha podido conectar con la base de datos",e)
        sys.exit(1)
    print("Conexion correcta")
    return db


def listar_mediadores():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM MEDIADOR")
    mediadores = cursor.fetchall()
    print("Lista de mediadores:")
    for mediador in mediadores:
        print(mediador)
    print("Total de mediadores:", len(mediadores))
    return db

def buscar_mediadores_por_nombre(nombre):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM MEDIADOR WHERE NOMBRE = %s", (nombre,))
    mediadores = cursor.fetchall()
    print("Listado de mediadores cuyo nombre es", nombre)
    for mediador in mediadores:
        print(mediador)
    print("Total de mediadores:", len(mediadores))
    db.close()

def buscar_mediador_y_oficina(dni_mediador):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM MEDIADOR WHERE DNI_MEDIADOR = %s", (dni_mediador,))
    mediador = cursor.fetchone()
    if mediador:
        cursor.execute("SELECT * FROM ADSCRITO_MEDIADOR_OFICINA WHERE DNI_MEDIADOR = %s", (dni_mediador,))
        adscritos = cursor.fetchall()
        print("Datos del mediador:")
        print(mediador)
        if adscritos:
            print("Oficina(s) a la que pertenece:")
            for adscrito in adscritos:
                cursor.execute("SELECT * FROM OFICINA WHERE NUM_OFICINA = %s", (adscrito[1],))
                oficina = cursor.fetchone()
                print(oficina)
        else:
            print("El mediador no está adscrito a ninguna oficina.")
    else:
        print("No se encontró ningún mediador con ese DNI.")
    db.close()

def insertar_mediador(dni, nombre, apellido1):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO MEDIADOR (DNI_MEDIADOR, NOMBRE, APELLIDO1) VALUES (%s, %s, %s)", (dni, nombre, apellido1))
    conexion.commit()
    print(cursor.rowcount, "registro(s) insertado(s)")
    conexion.close()

def insertar_adscrito_mediador_oficina(dni_mediador, num_oficina, fecha):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO ADSCRITO_MEDIADOR_OFICINA (DNI_MEDIADOR, NUM_OFICINA, FECHA) VALUES (%s, %s, %s)", (dni_mediador, num_oficina, fecha))
    conexion.commit()
    print(cursor.rowcount, "registro(s) insertado(s)")
    conexion.close()

def borrar_mediador(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM ADSCRITO_MEDIADOR_OFICINA WHERE DNI_MEDIADOR IN (SELECT DNI_MEDIADOR FROM MEDIADOR WHERE NOMBRE = %s)", (nombre,))
    cursor.execute("DELETE FROM MEDIADOR WHERE NOMBRE = %s", (nombre,))
    conexion.commit()
    print(cursor.rowcount, "registro(s) eliminado(s)")
    conexion.close()

def actualizar_mediador(dni, nombre, apellido1):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE MEDIADOR SET NOMBRE = %s, APELLIDO1 = %s WHERE DNI_MEDIADOR = %s", (nombre, apellido1, dni))
    conexion.commit()
    print(cursor.rowcount, "registro(s) actualizado(s)")
    conexion.close()

