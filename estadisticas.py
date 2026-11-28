import juego
import matplotlib.pyplot as plt
partidas = juego.partidas

#Aquí vamos a mostrar las estadísticas del usuario
#Lo he hecho pasando usuario en caso de que cierren sesión, pero no la app, entonces al guardar partidas pueden ser de distintos usuarios

def mostrar_estadisticas(usuario,rol):
    #TODAS LAS STATS
    winrate = 0.0
    abandonadas = 0
    ganadas = 0
    partidas_jugadas = 0
    partidas_acabadas = 0
    total_intentos = 0
    media_intentos = 0.0
    partidas_facil = 0
    partidas_medium = 0
    partidas_hard = 0
    wins_facil = 0
    wins_medium = 0
    wins_hard = 0
    media_intentos_wins = 0.0
    intentos_wins = 0
    por_usuario = {}

    if rol == "admin":
        titulo = "DE LA SESIÓN"
    else:
        titulo = f"DE {usuario}"

    #FOR RECORRIENDO LAS PARTIDAS
    for p in partidas:
        #AQUÍ MIRAMOS LAS PARTIDAS POR USUARIO EN MEMORIA
        nombre = p["usuario"]
        if nombre in por_usuario:
            por_usuario[nombre] += 1
        else:
            por_usuario[nombre] = 1

        if p['usuario'] == usuario or rol == "admin":
            partidas_jugadas += 1
            #PARTIDAS POR DIFICULTAD
            if p['dificultad'] == 1:
                partidas_facil += 1
            elif p['dificultad'] == 2:
                partidas_medium += 1
            elif p['dificultad'] == 3:
                partidas_hard += 1
            #VICTORIAS POR DIFICULTAD
            if p['estado'] == "Ganada":
                ganadas += 1
                partidas_acabadas += 1
                intentos_wins += p['num_intentos']
                if p['dificultad'] == 1:
                    wins_facil += 1
                elif p['dificultad'] == 2:
                    wins_medium += 1
                elif p['dificultad'] == 3:
                    wins_hard += 1

            #ABANDONADAS
            if p['estado'] == "Abandonada":
                abandonadas += 1
                partidas_acabadas += 1

            #INTENTOS
            total_intentos += p['num_intentos']

            #MUESTRA
    print("========================================")
    print("PARTIDAS POR USUARIO EN LA SESIÓN")
    print("========================================")
    for nombre, cantidad in por_usuario.items():
        print(f"{nombre}: {cantidad}")

    #SI NO HA JUGADO, NO HAY NADA QUE CALCULAR
    if partidas_jugadas == 0:
        print(f"{usuario} todavía no ha jugado ninguna partida")
        input("Pulsa Enter para volver al menú")
        return

    #CÁLCULOS
    if partidas_acabadas > 0:
        winrate = ganadas / partidas_acabadas * 100
        media_intentos = total_intentos / partidas_acabadas
    if ganadas > 0:
        media_intentos_wins = intentos_wins / ganadas

    #MOSTRAMOS LAS STATS
    print("========================================")
    print(f"ESTADÍSTICAS {titulo}")
    print("========================================")
    print(f"PARTIDAS INICIADAS: {partidas_jugadas}")
    print(f"PARTIDAS FINALIZADAS: {partidas_acabadas}")
    print(f"PARTIDAS GANADAS: {ganadas}")
    print(f"PARTIDAS ABANDONADAS: {abandonadas}")
    print(f"PORCENTAJE DE VICTORIAS: {winrate:.2f} %")
    print(f"TOTAL DE INTENTOS: {total_intentos}")
    print(f"MEDIA DE INTENTOS: {media_intentos}")
    print(f"MEDIA DE INTENTOS EN GANADAS: {media_intentos_wins:.2f}")
    print("GANADAS POR DIFICULTAD:")
    print(f"  BÁSICA: {wins_facil}")
    print(f"  MEDIA: {wins_medium}")
    print(f"  AVANZADA: {wins_hard}")
    print("========================================")

    #AQUÍ DIBUJAMOS LOS GRÁFICOS
    dibujar_stats(ganadas, abandonadas, partidas_facil, partidas_medium, partidas_hard, titulo)
    input("Pulsa Enter para volver al menú")


def mostrar_partidas(usuario,rol):
    contador_partidas = 0
    print("========================================")
    if rol == "admin":
        print(f"PARTIDAS DE LA SESIÓN")
    else:
        print(f"PARTIDAS DE {usuario}")
    for p in partidas:
        if p["usuario"] == usuario or rol == "admin":
            contador_partidas += 1
            print("========================================")
            print(f"PARTIDA {contador_partidas} DE {p['usuario']}")
            print(f"DIFICULTAD: {p['dificultad']}")
            print(f"TAMAÑO: {p['tam']} * {p['tam']}")
            if p['estado'] != "Abandonada":
                print(f"POSICIÓN TESORO: FILA: {p['tesoro'][0]} COL: {p['tesoro'][1]}")
            print(f"ESTADO: {p['estado']}")
            print(f"INTENTOS TOTALES: {p['num_intentos']}")
            print("TODOS LOS INTENTOS")
            intentos = 0
            for fila, col in p["intentos"]:
                intentos += 1
                print(f"INTENTO {intentos}: FIL {fila}, COL: {col}")
            if len(p['pistas']) > 0:
                for fila, col, pista in p["pistas"]:
                    print(f"PISTA: {pista} FIL: {fila} COL: {col}")
            juego.escrbirMapa(p["mapa"],p["tam"])
            print("========================================")

def dibujar_stats(ganadas, abandonadas, partidas_facil, partidas_medium, partidas_hard, titulo):
    plt.bar(["Básica", "Media", "Avanzada"], [partidas_facil, partidas_medium, partidas_hard])
    plt.title(f"Partidas por dificultad {titulo}")
    plt.ylabel("Partidas")
    plt.show()

    plt.bar(["Ganadas","Abandonadas"], [ganadas, abandonadas])
    plt.title(f"Partidas totales {titulo}")
    plt.ylabel("Partidas")
    plt.show()