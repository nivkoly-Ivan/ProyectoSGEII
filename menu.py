from logs import Log
from control_users import cargar_usuario
import juego
import sys

def menu_inicio():
    while True:
        print("Bienvenido")
        print("-----------------------------------")
        print("Debe iniciar sesion para jugar")
        print("-----------------------------------")
        usuario = input("Ponga su nombre de usuario:")
        clave = input("Ponga su clave:")
        cargar_usuario(usuario,clave)


def menu_principal(usuario,rol):
    while True:
        print("-----------------------------------")
        print("Bienvenido")
        print("-----------------------------------")
        print("1 } Empezar partida ")
        print("-----------------------------------")
        print("2 } Mirar estadísticas de la sesión")
        print("-----------------------------------")
        print("3 } Cambiar de sesión")
        print("-----------------------------------")
        print("4 } Salir")
        print("-----------------------------------")
        #Ismael no cambies a "Admin" con mayúscula, que en los txt está en minúscula
        if rol == "admin":
            print("5 } Opciones de administrador")

        opt = input("Ponga su opcion:")

        if opt == "1":
            print("1")
            juego.escogerDif()
        elif opt == "2":
            print("2")
            #mostrar_estadisticas()
        elif opt == "3":
            print("Cerrando sesión")
            menu_inicio()
        elif opt == "4":
            sys.exit()
        elif opt == "5" and rol == "admin":
            menu_administrador(usuario)
        else:
            print("Opcion no valida")


def menu_administrador(usuario):
    print(f"Bienvenido administrador {usuario}")
