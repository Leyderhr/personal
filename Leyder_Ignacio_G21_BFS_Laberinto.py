#Leyder Ignacio Herrera Bello No.20 G:21

def laberinto(mapa, inicio, fin) :
    colaPrioridad = [(inicio, [])]
    coord = []
    recorrido = []

    while (len(colaPrioridad)) :
        coord = colaPrioridad.pop(0)

        if not(coord[0] in coord[1]):
            coord[1].append(coord[0])

            if coord[0] == fin :
                recorrido = coord[1]
                colaPrioridad = []
            else :
                direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                size = len(direcciones)
                for i in range (size) :
                    x, y = coord[0][0] + direcciones[i][0], coord[0][1] + direcciones[i][1]
                    if (x >= 0 and y >= 0) and (x < len(mapa)) and (y < len(mapa[0])) and (mapa[x][y] != 1) :
                        colaPrioridad.append(((x, y), coord[1].copy()))
    
    return recorrido

mapa = [[0,1,0,0,0],
        [0,0,0,1,0],
        [0,1,0,1,0],
        [1,1,1,1,0],
        [0,0,0,0,0]]

inicio = (2,0)
fin = (4,4)

print(laberinto(mapa, inicio, fin))


