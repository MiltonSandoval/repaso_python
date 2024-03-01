nombre_contactos = []
numero_contactos = []

def menu():
    print("Agenda \n")
    print("1.Buscar un contacto")
    print("2.Agregar un contacto")
    print("3.Actualizar un contacto")
    print("4.Eliminar un contacto")
    print("5.Salir \n")


def buscar_agenda(agente, busqueda):
    if busqueda.lower() in agente or busqueda in agente:
        try:
            return agente.index(busqueda)
        except ValueError:
            return agente.index(busqueda.lower())
    else:
        return None


def controlador(agregador):
    if len(agregador) <= 11:
        try:
            agregador = int(agregador)
            return 1
        except ValueError:
            return 0
    else:
        return 0


def agregar_agen():
    nombre_contactos.append(nombre)
    numero_contactos.append(numero)

while(True):
    menu()
    opcion = input("Ingrese su opcion:")
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto:")
        posi = buscar_agenda(nombre_contactos, nombre)
        if posi != None:
            print(f"El numero de telefono de {nombre_contactos[posi]} es {numero_contactos[posi]}.")
        else:
            print(f"El contacto no existe")
    elif opcion == "2":
        nombre = input("Ingrese el nombre:")
        if buscar_agenda(nombre_contactos, nombre) == None:
            numero = input("Ingrese el numero:")
            if controlador(numero):
                agregar_agen()
            else:
                print("Ingrese un numero no mayor a 11 digitos y con valores numericos")
        else:
            print("El contacto ya existe \n")

    elif opcion == "3":
        nombre = input("Ingrese el nombre:")
        if buscar_agenda(nombre_contactos, nombre) != None:
            numero = input("Ingrese el nuevo numero:")
            if controlador(numero):
                numero_contactos[buscar_agenda(nombre_contactos, nombre)] = numero
            else:
                print("Ingrese un numero no mayor a 11 digitos y con valores numericos")
        else:
            print("El contacto no existe \n")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto:")
        posi = buscar_agenda(nombre_contactos, nombre)
        if posi != None:
            nombre_contactos.pop(posi)
            numero_contactos.pop(posi)
        else:
            print(f"El contacto no existe")
    elif opcion == "5":
        break
    else:
        print("Opcion incorrecta")
