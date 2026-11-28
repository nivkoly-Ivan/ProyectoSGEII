from logs import Log
from control_users import cargar_usuario
import juego
import estadisticas
import sys
log = Log()

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
        print("3 } Mirar historial de partidas de la sesión")
        print("-----------------------------------")
        print("4 } Cambiar de sesión")
        print("-----------------------------------")
        print("5 } Salir")
        print("-----------------------------------")
        #Ismael no cambies a "Admin" con mayúscula, que en los txt está en minúscula
        if rol == "admin":
            print("6 } Opciones de administrador")

        opt = input("Ponga su opción:")

        if opt == "1":
            print("1")
            juego.escogerDif(usuario)
        elif opt == "2":
            print("2")
            estadisticas.mostrar_estadisticas(usuario)
        elif opt == "3":
            print("3")
            estadisticas.mostrar_partidas(usuario)
        elif opt == "4":
            print("Cerrando sesión")
            menu_inicio()
        elif opt == "5":
            log.escribir("INFO",f"{usuario} SALE DE LA APLICACIÓN")
            sys.exit()
        elif opt == "6" and rol == "admin":
            menu_administrador(usuario)
        else:
            print("Opción no valida")


def menu_administrador(usuario):
    cheats = False
    while True:
        print("-----------------------------------")
        print(f"Bienvenido administrador {usuario}")
        print("-----------------------------------")
        print("1 } Mirar estadísticas de la sesión como administrador")
        print("-----------------------------------")
        print("2 } Mirar historial de partidas de la sesión como administrador")
        print("-----------------------------------")
        print("3 } Activar cheats")
        print("-----------------------------------")
        print("4 } Salir")
        print("-----------------------------------")
        opt = input("Ponga su opción")
        if opt == "1":
            estadisticas.mostrar_estadisticas(usuario,)
        elif opt == "2":
            estadisticas.mostrar_partidas(usuario,)
        elif opt == "3":
            cheats = True
            print("Ahora te salen los tesoros en las partidas")
        elif opt == "4":
            return
        else:
            print("Opcion no valida")
