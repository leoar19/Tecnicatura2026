# Ejercicio 14: Agenda Telefonica
# Hacer un programa que simule una agenda de contactos. Crear un diccionario
# donde la clave sea el nombre del usuario y el valor sea el telefono, el
# programa tendra el siguiente menu de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

# Diccionario vacío para guardar los contactos
agenda = {}

# Variable para controlar el bucle
salir = False

print("=== AGENDA TELEFÓNICA ===")

while not salir:
    # Mostrar el menú
    print("\n--- MENÚ ---")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    
    # Pedir opción al usuario
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        # Nuevo contacto
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el teléfono del contacto: ")
        
        if nombre in agenda:
            print(f"El contacto '{nombre}' ya existe con el teléfono {agenda[nombre]}.")
        else:
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado correctamente.")
    
    elif opcion == "2":
        # Borrar contacto
        nombre = input("Ingresa el nombre del contacto a borrar: ")
        
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto '{nombre}' eliminado correctamente.")
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")
    
    elif opcion == "3":
        # Ver contactos existentes
        if len(agenda) == 0:
            print("La agenda está vacía. No hay contactos para mostrar.")
        else:
            print("\n--- CONTACTOS ---")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
    
    elif opcion == "4":
        # Salir
        salir = True
        print("Gracias por usar la agenda. ¡Hasta luego!")
    
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 4.")