def menu():
    print("Agenda \n")
    print("1.Buscar un contacto")
    print("2.Agregar un contacto")
    print("3.Actualizar un contacto")
    print("4.Eliminar un contacto")
    print("5.Salir \n")


def buscar_agenda(agente, busqueda):
    if busqueda.lower() in agente or busqueda in agente:
        posicion = agente.index(busqueda) or agente.index(busqueda.lower())
        return posicion
    else:
        return None

def controlador(agente, agregador, num):
    if buscar_agenda(agente, agregador) == None:
        return True
    else:
        print("El contacto ya se encuentra registrado \n")
        return False
def agregar_agen(nombre, numero):
    nombre_contactos.append(nombre)
    numero_contactos.append(numero)



while(True):
    menu()
    opcion = input("Ingrese su opcion:")
    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        break
    else:
        print("Opcion incorrecta")


