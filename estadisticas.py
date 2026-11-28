import juego
partidas = juego.partidas

#Aqui vamos a mostrar las estadisticas del usuario
#Lo he hecho pasando usuario en caso de que cierren sesion pero no la app, entonces al guardar partidas pueden ser de distintos usuarios

def mostrar_estadisticas(usuario):
    winrate = 0.0
    abandonadas = 0
    ganadas = 0
    partidas_jugadas = 0
    for p in partidas:
        print(("w"))






def mostrar_partidas(usuario):
    contador_partidas = 0
    for p in partidas:
        print("========================================")
        print(f"PARTIDAS DE {usuario}")
        if p["usuario"] == usuario:
            contador_partidas += 1
            print("========================================")
            print(f"PARTIDA {contador_partidas}")
            print(f"DIFICULTAD: {p['dificultad']}")
            print(f"TAMAÑO: {p['tam']} * {p['tam']}")
            print(f"POSICION TESORO: FILA: {p['tesoro'][0]} COL: {p['tesoro'][1]}")
            print(f"ESTADO: {p['estado']}")
            print(f"INTENTOS TOTALES: {p['num_intentos']}")
            print("TODOS LOS INTENTOS")
            intentos = 0
            for fila, col in p["intentos"]:
                intentos += 1
                print(f"INTENTO {intentos}: FIL {fila}, COL: {col}")
            #Faltan añadir las pistas
            juego.escrbirMapa(p["mapa"],p["tam"])
            print("========================================")