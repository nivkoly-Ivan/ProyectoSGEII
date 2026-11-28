from logs import Log
import menu
log = Log()


def cargar_usuario(usuario, password):
    login_correcto = False

    #bugfix002 - Ismael
    # Pusiste users.txt.txt, y no encontraba el archivo
    #Arreglé tambien el fallo que tenias al intentar leer las lienas del fichero
    try:
        with open("users.txt", "r", encoding="utf-8") as f:
            for lines in f:
                datos = lines.strip().split(";")

                if datos[0] == usuario and datos[1] == password:
                    login_correcto = True
                    log.escribir("INFO", f"Usuario {usuario} login correcto")
                    return menu.menu_principal(datos[0], datos[2])

        # Saco el else que tenias despues del if para que si no lo encuentra recorra todo el fichero
        # Si lo recorre entero y no lo encuentra, ya fuera del for y fuera de todo
        # manda al usuario al menu inicio
        if not login_correcto:
            print("Usuario o contraseña incorrectos")
            log.escribir("ERROR", f"Usuario {usuario} incorrecto")
            return menu.menu_inicio()
    except FileNotFoundError as FNFE:
        log.escribir("ERROR", f"No se ha encontrado el fichero: {FNFE}")
    except OSError as OSE:
        log.escribir("ERROR", f"No se pudo leer el archivo: {OSE}")

    #Todo en un try except para que no pete







