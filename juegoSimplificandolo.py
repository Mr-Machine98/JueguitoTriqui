inicio = True
def pintarTablero():
    for f in range(3):
        for c in range(3):
            print("|", tablero[f][c], "|", end=' ')
        print()
    return
while(inicio):

    p1 = p2 = ""
    validacion = True
    match = 1
    tablero = [

        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]


    print("*"*63, "\n Bienvenidos al juego de triqui.")
    print("Escoje 'X' o 'O' para jugar, las 'X' comienzan primero.", "\n Recuerda filas son: 0, 1, 2 y columnas lo mismo", " \n RECUERDA, NO SOBREESCRIBIR ENCIMA DEL OTRO JUGADOR, TRAMPOSO.")
    print("*"*63)

    pintarTablero()

    p1 = input("Escoje ficha jugador número 1: ")
    p2 = input("Escoje ficha jugador número 2: ")

    p1 = p1.upper()
    p2 = p2.upper()

    print("")

    while(validacion):

        if p1 == 'X':

            if p2 == 'X':

                print("!!!! Los dos jugadores no pueden tener X, vuelvan a escoger. ¡¡¡¡", "\n")
                break

            # AQUÍ COMIENZA EL JUEGO
            print("*"*80)
            print("* Jugador 1 comienza con 'X'.                                                  *", "\n" "* Recuerda, para colocar tu ficha ingresas la posición de la fila y la columna.  *")
            print("*"*80)
            print("\n")

            while(match != 6):

                try:

                    # PINTA EL TABLERO
                    pintarTablero()
                    print("")

                    # PIDE AL USUARIO LAS X Y O
                    
                    fila_p1 = input(" Fila[#] Jugador 1: ")
                    colum_p1 = input(" Columna[#] Jugador 1: ")
                    tablero[int(fila_p1)][int(colum_p1)] = p1
                    print("")

                    # VALIDADCIONES JUGADOR 1

                    if match == 5:
                        print("Se acabo el juego, empate.")
                        break

                    if tablero[0][0] == 'X' and tablero[0][1] == 'X' and tablero[0][2] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[1][0] == 'X' and tablero[1][1] == 'X' and tablero[1][2] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'X' and tablero[2][1] == 'X' and tablero[2][2] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'X' and tablero[1][0] == 'X' and tablero[2][0] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break


                    if tablero[0][1] == 'X' and tablero[1][1] == 'X' and tablero[2][1] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][2] == 'X' and tablero[1][2] == 'X' and tablero[2][2] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'X' and tablero[1][1] == 'X' and tablero[0][2] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    # VALIDADCIONES JUGADOR 1 final
                    print("")
                    pintarTablero()
                    print("")
        
                    fila_p2 = input(" Fila[#] Jugador 2: ")
                    colum_p2 = input(" Columna[#] Jugador 2: ")
                    tablero[int(fila_p2)][int(colum_p2)] = p2
                    print("")


                    """
                     Aquídeberia ver validaciones para ganar jug 2

                    """

                    if tablero[0][0] == 'O' and tablero[0][1] == 'O' and tablero[0][2] == 'O':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break


                    """ARRANQUE"""

                    if tablero[1][0] == 'O' and tablero[1][1] == 'O' and tablero[1][2] == 'O':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'O' and tablero[2][1] == 'O' and tablero[2][2] == 'O':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'O' and tablero[1][0] == 'O' and tablero[2][0] == 'O':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break


                    if tablero[0][1] == 'O' and tablero[1][1] == 'O' and tablero[2][1] == 'O':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][2] == 'O' and tablero[1][2] == 'O' and tablero[2][2] == 'O':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'O' and tablero[1][1] == 'O' and tablero[0][2] == 'O': 
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O':                        
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break


                    """TERMINE"""
                    match = match + 1
        
                except:
                    print("Error")
                    break

            inicio = False
            break

        elif p2 == 'X':
            if p1 == 'X':
                print("!!!! Los dos jugadores no pueden tener X, vuelvan a escoger. !!!!" , "\n")
                break

            # AQUÍ COMIENZA EL JUEGO
            print("*"*80)
            print("* Jugador 2 comienza con X.                                                    *", "\n" "* Recuerda, para colcar tu ficha ingresas la posición de la fila y la columna.  *")
            print("*"*80)
            print("\n")

            while(match != 6):

                try:
                    # PINTA EL TABLERO
                    pintarTablero()
                    print("")
                    # PIDE AL USUARIO LAS X Y O
                    fila_p2 = input(" Fila[#] Jugador 2: ")
                    colum_p2 = input(" Columna[#] Jugador 2: ")
                    tablero[int(fila_p2)][int(colum_p2)] = p2

                    if match == 5:
                        print("Se acabo el juego, empate.")
                        break

                    # validaciones p2

                    if tablero[0][0] == 'X' and tablero[0][1] == 'X' and tablero[0][2] == 'X':                       
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    """ARRANQUE"""
                    if tablero[1][0] == 'X' and tablero[1][1] == 'X' and tablero[1][2] == 'X':                        
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'X' and tablero[2][1] == 'X' and tablero[2][2] == 'X':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'X' and tablero[1][0] == 'X' and tablero[2][0] == 'X':                       
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][1] == 'X' and tablero[1][1] == 'X' and tablero[2][1] == 'X':                       
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][2] == 'X' and tablero[1][2] == 'X' and tablero[2][2] == 'X':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'X' and tablero[1][1] == 'X' and tablero[0][2] == 'X':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X':
                        print("El ganador es Jugador 2, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    print("")
                    pintarTablero()
                    print("")
                   
                    fila_p1 = input(" Fila[#] Jugador 1: ")
                    colum_p1 = input(" Columna[#] Jugador 1: ")
                    tablero[int(fila_p1)][int(colum_p1)] = p1
                    print("")

                    """
                     Aquídeberia ver validaciones para ganar p1
                    """              
                    if tablero[0][0] == 'O' and tablero[0][1] == 'O' and tablero[0][2] == 'O':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    """ARRANQUE"""
                    if tablero[1][0] == 'O' and tablero[1][1] == 'O' and tablero[1][2] == 'O':                       
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'O' and tablero[2][1] == 'O' and tablero[2][2] == 'O':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'O' and tablero[1][0] == 'O' and tablero[2][0] == 'O':                        
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        break

                    if tablero[0][1] == 'O' and tablero[1][1] == 'O' and tablero[2][1] == 'O':                       
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][2] == 'O' and tablero[1][2] == 'O' and tablero[2][2] == 'O':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[2][0] == 'O' and tablero[1][1] == 'O' and tablero[0][2] == 'O':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    if tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O':
                        print("El ganador es Jugador 1, !!! Felicitaciones ¡¡¡.")
                        pintarTablero()
                        print("")
                        break

                    """TERMINE"""
                    match = match + 1

                except:
                    print("Error")
                    break

            inicio = False
            break

        else:
            print("!!!! Vuelvan a escoger. !!!!", "\n")
            break
print("Se acabó el juego.")