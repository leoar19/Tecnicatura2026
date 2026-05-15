"""
1. Mostrar: Ingrese los siguientes datos del libro.
2. Digite el nombre del libro.
3. Digite el ID del libro.
4. Digite el precio del libro.
5. Indicar si el envío es gratuito (True/False).
6. Mostrar todos los datos.
"""
print("Ingrese los siguientes datos del libro.")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el envío es gratuito (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    print("El envío es incorrecto, debe escribir True o False.")

print(f'''
        Nombre: {nombre}
        ID: {id}
        Precio: {precio}
        Envío Gratuito: {envioGratuito}
      ''')