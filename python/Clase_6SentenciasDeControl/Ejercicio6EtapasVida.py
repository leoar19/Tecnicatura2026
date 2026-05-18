# Haremos un programa que cuando el usuario ingrese su edad le diga, o imprima, la etapa
# de su vida en una breve oracion:
# 0 a 10 =  La infancia es increible y bella
# 10 a 19 = Tienes muchos cambios, mucho que estudiar
# 20 a 29 = Amor y comienza el trabajo
# Para las siguientes etapas, deberas completarlo.
edadUsuario = int(input("Ingresa una edad (0 a 100): "))
if 0 <= edadUsuario <= 100:
    if edadUsuario <= 10:
        print('La infancia es increible y bella')
    elif edadUsuario <= 19:
        print('Tienes muchos cambios, mucho que estudiar')
    elif edadUsuario <= 29:
        print('Amor y comienza el trabajo')
    elif edadUsuario <= 39:
        print('Etapa de construir estabilidad y proyectos')
    elif edadUsuario <= 49:
        print('Mas experiencia y responsabilidades')
    elif edadUsuario <= 59:
        print('Tiempo de madurez y nuevas perspectivas')
    elif edadUsuario <= 69:
        print('Momento de disfrutar lo aprendido en la vida')
    else:
        print('Una etapa para compartir sabiduria y descansar')
else:
    print('No ingresaste una edad en el rango.')