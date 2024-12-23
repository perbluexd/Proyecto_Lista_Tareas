# -*- coding: utf-8 -*-


diccionario = {"Tareas pendientes": []}

def mostrar(diccionario):
    # Muestra las tareas en un formato claro
    for clave, valor in diccionario.items():
        tareas = "\n".join([f"{i+1}. {tarea}" for i, tarea in enumerate(valor)])
        return f"!Hola, bienvenido a tu lista de tareas!\nTu lista actual es:\n{clave}:\n{tareas if tareas else 'No hay tareas pendientes.'}"

def agregarTarea(diccionario):
    # Agrega tareas a un registro existente
    opcion = input("¿En qué registro te gustaría agregar tareas?: ")
    if opcion in diccionario:
        while True:
            tarea = input("Escribe la tarea a agregar: ")
            diccionario[opcion].append(tarea)
            salida = input("¿Deseas agregar otra tarea? (presiona 'n' para salir): ").lower()
            if salida == "n":
                break
    else:
        print(f"El registro '{opcion}' no existe. Inténtalo de nuevo.")

def eliminarTarea(diccionario):
    # Elimina una tarea existente en "Tareas pendientes"
    if "Tareas pendientes" in diccionario and diccionario["Tareas pendientes"]:
        print("Tareas actuales:")
        for i, elemento in enumerate(diccionario["Tareas pendientes"], start=1):
            print(f"{i}. {elemento}")
        try:
            elemento_eliminar = int(input("Selecciona el número de la tarea que deseas eliminar: ")) - 1
            if 0 <= elemento_eliminar < len(diccionario["Tareas pendientes"]):
                tarea_eliminada = diccionario["Tareas pendientes"].pop(elemento_eliminar)
                print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
            else:
                print("Número de tarea no válido.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    else:
        print("No hay tareas pendientes para eliminar.")

def agregarTipoTarea(diccionario):
    # Agrega un nuevo tipo de registro de tareas
    nuevo_tipo = input("Ingresa el nombre del nuevo registro de tareas: ")
    if nuevo_tipo in diccionario:
        print(f"El registro '{nuevo_tipo}' ya existe.")
    else:
        diccionario[nuevo_tipo] = []
        print(f"Registro '{nuevo_tipo}' agregado con éxito.")

def menu():
    while True:
        print("\nEsta es la lista de opciones de nuestra lista de tareas:")
        opcion = input("1. Mostrar Pendientes\n2. Agregar Tarea\n3. Eliminar Tarea\n4. Agregar tipo tarea\n5. Salir\nElige una opción: ")

        if opcion == "1":
            print(mostrar(diccionario))
        elif opcion == "2":
            agregarTarea(diccionario)
        elif opcion == "3":
            eliminarTarea(diccionario)
        elif opcion == "4":
            agregarTipoTarea(diccionario)
        elif opcion == "5":
            print("¡Gracias por usar la lista de tareas! Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

