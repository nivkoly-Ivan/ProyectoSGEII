import random as ra

#Requisito 002 - Ismael

#Funcion para escoger una dificultad
def escogerDif():

    try:
        #Escoger la dificultad
        print("=== Dificultad de la partida ===")
        print("1 - Básica (5x5)")
        print("2 - Media (8x8)")
        print("3 - Avanzada (10x10)")

        respuesta = int(input())

        juego(respuesta)

    except ValueError as VE:
        print("Error de valor en juego.py")
        print(VE)
    except Exception as E:
        print("Error en juego.py")
        print(E)


def juego(dif):

    ha_ganado = False
    #Segun la dif que se escoja, cambiará el valor de la variable *tam*
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

    mapa = crearMapa(tam)

    escrbirMapa(mapa,tam)

    while not ha_ganado:
        print("=== Dime las coordenadas ===")
        fila = int(input("Fila: "))
        col = int(input("Columna: "))

        if fila < 0 or fila >= tam or col < 0 or col >= tam:
            print(f"Las coordenadas deben de estar entre el 0 y {tam - 1}")
        else:
            if fila == tesoroFila and col == tesoroCol:
                ha_ganado = True
                print("¡Lo has encontrado!")
                print(f"El tesoro 💎 estaba en {fila}, {col}")
                mapa[tesoroFila][tesoroCol] = tesoro
                escrbirMapa(mapa, tam)
            else:
                mapa[fila][col] = "-"
                escrbirMapa(mapa, tam)




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


