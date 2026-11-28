from logs import Log
from menu import *
log = Log()


def cargar_usuario(usuario, password):
    login_correcto = False
    with open("users.txt","r") as f:
        lines = f.readlines()
        while lines:
            datos = lines.strip().split(";")
            try:
                if datos[0] == usuario and datos[1] == password:
                    log.escribir("INFO", f"Usuario {usuario} login correcto")
                    return menu_principal(datos[0],datos[2])
                else:
                    log.escribir("ERROR", f"Usuario {usuario} incorrecto")
                    return menu_inicio()
            except FileNotFoundError:
                log.escribir("ERROR", "FileNotFoundError")
                return menu_inicio()
            except IndexError:
                log.escribir("ERROR", "IndexError")
                return menu_inicio()






