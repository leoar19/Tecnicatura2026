# Ejercicio 11: Menu interactivo - Cajero Automatico
# Hacer un programa que simule un cajero automatico con un saldo inicial
# de $1000 y tendra el siguiente menu de opciones:
#                           1. Ingresar dinero en la cuenta
#                           2. Retirar dinero de la cuenta
#                           3. Mostrar dinero disponible
#                           4. Salir
saldo = 1000
salir = False # variable para controlar el bucle

print("=== CAJERO AUTOMÁTICO ===")
print(f"Saldo inicial: ${saldo}\n")

while not salir:
    # Mostrar el menú
    print("--- MENÚ ---")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Salir")
    
    # Pedir opción al usuario
    opcion = input("Elige una opción (1-4): ")
    
    # Procesar la opción
    if opcion == "1":
        # Ingresar dinero
        monto = float(input("¿Cuánto dinero deseas ingresar? $"))
        if monto > 0:
            saldo += monto
            print(f"Has ingresado ${monto:.2f}. Nuevo saldo: ${saldo:.2f}\n")
        else:
            print("El monto debe ser mayor que cero.\n")
    elif opcion == "2":
        # Retirar dinero
        monto = float(input("¿Cuánto dinero deseas retirar? $"))
        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f"Has retirado ${monto:.2f}. Nuevo saldo: ${saldo:.2f}\n")
            else:
                print(f"Saldo insuficiente. Tu saldo actual es ${saldo:.2f}\n")
        else:
            print("El monto debe ser mayor que cero.\n")
    elif opcion == "3":
        # Mostrar saldo
        print(f"Tu saldo actual es: ${saldo:.2f}\n")
    elif opcion == "4":
        # Salir
        salir = True
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
    else:
        # Opción no válida
        print("Opción no válida. Por favor, elige un número del 1 al 4.\n")