
from funciones import *
db = MySQLdb.connect("localhost","andres1","andres1","proyectopython")



opcion = 0
while opcion != "7":
        print("Menú:")
        print("1  Listar todos los mediadores y ver cuantos hay")
        print("2. Buscar a un mediador")
        print("3. Añadir a un mediador")
        print("4. Borrar a un mediador")
        print("5. Actualizar datos de un mediador")
        print("6. Ver todos los datos de un mediador (DNI)")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            listar_mediadores()
        if opcion == "2":
             nombre = input("Introduce el nombre del mediador:")
             buscar_mediadores_por_nombre(nombre)
        if opcion == "3":
            dni = input("Ingrese DNI: ")
            nombre = input("Ingrese nombre: ")
            apellido1 = input("Ingrese apellido1: ")
            insertar_mediador(dni, nombre, apellido1)
            num_oficina = input("Ingrese número de oficina: ")
            fecha = input("Ingrese fecha (YYYY-MM-DD): ")
            insertar_adscrito_mediador_oficina(dni, num_oficina, fecha)
        elif opcion == "4":
            nombre = input("Ingrese nombre: ")
            borrar_mediador(nombre)
        elif opcion == "5":
            dni = input("Ingrese DNI: ")
            nombre = input("Ingrese nombre: ")
            apellido1 = input("Ingrese apellido1: ")
            actualizar_mediador(dni, nombre, apellido1)
        elif opcion == "6":
             dni_mediador = input("DAme dni")
             buscar_mediador_y_oficina(dni_mediador)