import random as ra
import time

from logs import Log
log = Log()

#Creamos un diccionario de partidas, asi guardar las estadisticas y las partidas de la sesion con lo que necesitamos de estadisticas
partidas = []
#Requisito 002 - Ismael

#Funcion para escoger una dificultad
#He añadido los logs donde nos pide el requisito 006 y pasamos usuario como parametro para los logs
#Añado la opción de abandonar y añado variables para el "historial de partidas" y "estadisticas de la sesión"

def escogerDif(usuario):

    try:
        #Escoger la dificultad
        print("=== Dificultad de la partida ===")
        print("1 - Básica (5x5)")
        print("2 - Media (8x8)")
        print("3 - Avanzada (10x10)")

        respuesta = int(input())

        juego(respuesta,usuario)

    except ValueError as VE:
        print("Error de valor en juego.py")
        print(VE)
    except Exception as E:
        print("Error en juego.py")
        print(E)


def juego(dif,usuario):

    ha_abandonado = False
    ha_ganado = False
    contador_turnos = 0

    #Según la dif que se escoja, cambiará el valor de la variable *tam*
    if dif == 1:
        tam = 5
    elif dif == 2:
        tam = 8
    elif dif == 3:
        tam = 10

    #Creacion del mapa
    tesoroFila = ra.randint(0, tam - 1)
    tesoroCol = ra.randint(0, tam - 1)

    tesoro = "💎"

    log.escribir("PARTIDA",f"INICIO DE PARTIDA, DIFICULTAD : {dif} POR {usuario}")
    mapa = crearMapa(tam)

    #Aquí guardamos la partida
    partida = {
        "usuario" : usuario,
        "dificultad": dif,
        "tam": tam,
        "tesoro": (tesoroFila, tesoroCol),
        "intentos": [],
        "pistas": [],
        "estado": "En curso",
        "num_intentos": 0,
        "mapa": mapa
    }
    partidas.append(partida)
    escrbirMapa(mapa,tam)

    while not ha_ganado and not ha_abandonado:
        print("=== Dime las coordenadas ===")
        print("=== Recuerda que puedes abandonar escribiendo -1 en fila o columna ===")
        fila = int(input("Fila: "))
        col = int(input("Columna: "))

        #Metodo de abandonar
        if fila == -1 or col == -1:
            print("Saliendo de la partida, cuenta como abandonada")
            log.escribir("INFO",f"PARTIDA ABANDONADA TRAS {contador_turnos} | POR {usuario}")
            time.sleep(2)
            partida["estado"] = "Abandonada"
            ha_abandonado = True
        #Metodo fuera de Rango
        elif fila < 0 or fila >= tam or col < 0 or col >= tam:
            print(f"Las coordenadas deben de estar entre el 0 y {tam - 1}")
            log.escribir("INTENTO ILEGAL",f"COORDENADAS INEXISTENTES/FUERA DE RANGO | POR {usuario}")
        else:
            #Metodo de busqueda del tesoro
            if fila == tesoroFila and col == tesoroCol:
                contador_turnos += 1
                ha_ganado = True
                print("¡Lo has encontrado!")
                print(f"El tesoro 💎 estaba en {fila}, {col}")
                mapa[tesoroFila][tesoroCol] = tesoro
                escrbirMapa(mapa, tam)
                log.escribir("INTENTO GANADO", f"FILA :{fila} COLUMNA: {col} | POR {usuario}")
                log.escribir("PARTIDA GANADA",f"INTENTOS : {contador_turnos} | POR {usuario}")
                partida["estado"] = "Ganada"
                partida["num_intentos"] = contador_turnos
                partida["intentos"].append((fila,col))
            else:
                contador_turnos += 1
                mapa[fila][col] = "-"
                escrbirMapa(mapa, tam)
                log.escribir("INTENTO FALLIDO", f"FILA :{fila} COLUMNA: {col} | POR {usuario}")
                partida["intentos"].append((fila,col))
                partida["num_intentos"] = contador_turnos

                # Req 004 - Ismael
                # Sistema de psitas, este se habilita cuando el num de intentos es mayor o igual a 3
                if contador_turnos >= 3:
                    print("=== Sistema de pistas ===")
                    if (fila == tesoroFila or fila == tesoroFila + 1 or fila == tesoroFila - 1) and (col == tesoroCol or col == tesoroCol + 1 or col == tesoroCol - 1):
                        print("Te has quedado cerca")
                    else:
                        print("Te has quedado lejos")





#Funcion para crear el mapa
def crearMapa(tam):

    mapa = []
    for i in range(tam):
        fila = []
        for j in range(tam):
            fila.append("?")
        mapa.append(fila)

    #Para poner el tesoro
    #Saco el tesoro de aqui pq antes lo metia en el mapa cuando ni si quiera lo he creado
    #tesoroFila = ra.randint(0, tam-1)
    #tesoroCol = ra.randint(0, tam-1)

    #tesoro = "💎"
    #print(tesoroFila)
    #print(tesoroCol)

    #mapa[tesoroFila][tesoroCol] = tesoro
    return mapa

#Funcion para printear el mapa
def escrbirMapa(mapa, tam):
    # Printeamos el mapa

    # para que salgan los numeros de arriba
    print(" ", end=" ")
    for t in range(tam):
        print(t, end=" ")
    print()
    # mapa como tal + los numeros de la derecha
    for i in range(len(mapa)):
        print(i, end=" ")
        for j in range(len(mapa[i])):
            print(f"{mapa[i][j]} ", end="")
        print()


