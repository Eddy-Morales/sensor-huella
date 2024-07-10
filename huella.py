import random
import webbrowser

nombres = []
huellas = []
codigos = []

def solicitar_numero_personas():
    while True:
        try:
            numero = int(input("Ingrese el número de personas a registrar (1-20): "))
            if 1 <= numero <= 20:
                return numero
            else:
                print("Por favor, ingrese un número en el rango de 1 a 20.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def solicitar_opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese la opción: "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Por favor, ingrese una opción válida (1, 2, 3 o 4).")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def solicitar_nombre():
    while True:
        nombre = input("Nombre: ")
        if nombre.isalpha():
            return nombre
        else:
            print("El nombre no debe contener números ni caracteres especiales.")

def menu_opciones():
    print("¿Qué acción desea realizar?: ")
    print('*  1) Ingresar usuarios')
    print('*  2) Mostrar usuarios')
    print('*  3) Buscar y enviar código de recuperación')
    print('*  4) Salir del sistema')
    return solicitar_opcion_menu()

def ingreso_personal(numPersonas):
    for i in range(numPersonas):
        print("Ingrese los datos de la persona", i + 1)
        nombreUsuario = solicitar_nombre()
        huellaUsuario = input("Huella: ")
        nombres.append(nombreUsuario)
        huellas.append(huellaUsuario)
        codigos.append(random.randrange(1000, 9999))

def mostrar_registros():
    for i in range(len(nombres)):
        print("-------------------------------------")
        print("Mostrando los datos de la persona", i + 1)
        print("* Nombre:", nombres[i])
        print("* Huella dactilar:", huellas[i])
        print("* Código de acceso:", codigos[i])
        print("-------------------------------------")

def buscar_enviar_codigo(nombreUsuario):
    if nombreUsuario in nombres:
        indice = nombres.index(nombreUsuario)
        print("Usuario encontrado")
        print("¿Desea enviar el código a su número de teléfono?")
        opcion = input("Ingrese si o no: ").lower()
        if opcion == "si":
            num = input("Ingrese el número de teléfono: ")
            url = f'https://api.whatsapp.com/send?phone={num}&text=El código de recuperación es: {codigos[indice]}'
            webbrowser.open(url)
    else:
        print("No existe ese usuario registrado")

def main():
    print("--------------- SISTEMA DACTILAR -------------")
    print("------------------- Bienvenid@ -------------------")
    while True:
        caso = menu_opciones()
        if caso == 1:
            numPersonas = solicitar_numero_personas()
            ingreso_personal(numPersonas)
        elif caso == 2:
            mostrar_registros()
        elif caso == 3:
            personaBuscar = solicitar_nombre()
            buscar_enviar_codigo(personaBuscar)
        elif caso == 4:
            print("Muchas gracias")
            break

main()
