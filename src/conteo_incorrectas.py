import random as rd


estado = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#1->x
#2->o

#de forma aleatoria empieza el juego

#se definen las soluciones
#los dos primeros numeros nos indican la ubicacion, mientras que el tercero que jugador lo ocupo 1 o 2
meta = {
    1: [[0,0,0],[0,1,0],[0,2,0]],
    2: [[1,0,0],[1,1,0],[1,2,0]],
    3: [[2,0,0],[2,1,0],[2,2,0]],
    4: [[0,0,0],[1,0,0],[2,0,0]],
    5: [[0,1,0],[1,1,0],[2,1,0]],
    6: [[0,2,0],[1,2,0],[2,2,0]],
    7: [[0,0,0],[1,1,0],[2,2,0]],
    8: [[0,2,0],[1,1,0],[2,0,0]]
}

#heuristicas
#se van reduciendo segun la meta que se escoja, pero si se ve interrumpida por el otro jugador, esta aumenta a 100,
#de esta manera se excluye y se miran otras rutas
heuristicas = {
    1: [3,3,3,3,3,3,3,3], #jugador 1
    2: [3,3,3,3,3,3,3,3] #jugador 2
}


def change_heuristica(ruta,player): #indice escogido en meta
    data = []
    conjunto = {0}

    for i in range(0,3):
        data.append(meta[ruta][i][2])
        conjunto.add(meta[ruta][i][2])
    
    if(len(conjunto)==3):
        heuristicas[player][ruta-1] = 100
    else:
        heuristicas[player][ruta-1] = 3 - data.count(player)
    



#se guardan las marcaciones (ruta)

visitados = {
    1: [],
    2: []
} 

def addVisit(a,b,player):
    visitados[player].append([a,b])



#revisar si alguien gano
def check_winner(player): 
    if(heuristicas[player].count(0)):
        print(f"gano el jugador {player}")
        return True 
    else:
        print("nadie ha ganado aún")
    
    return False




#se repiten posiciones en diferentes rutas en meta, se deben marcar todos y evaluar las heuristicas de forma consecutiva
#esto es mas sencillo de hacer si se guarda la opcion antes para buscar los iguales
#al retornar true cambia de turno en el juego
def sweep_data(a,b,player):
    if(estado[a][b]==0):
        for key in range(1,9):
            try:
                ind = meta[key].index([a,b,0])
            except:
                ind = -1
            
            if(ind != -1):
                meta[key][ind] = [a,b,player]
        
        for key in range(1,9):
            change_heuristica(key,player)
        
        addVisit(a,b,player)

        return True
    
    return False
        
        



#inicio del juego
winner_exist = False #verificar si hay un ganador

turno = int(input("Si escoges 1 empieza la maquina, si escoges 2 empiezas tu: \n"))

while(not winner_exist): #mientras no exista un ganador

    for fila in estado:
        print(" | ".join(str(x) for x in fila))
    print(heuristicas)
    print(meta)
    print(visitados)

    change_turno = False

    if(turno == 1):
        #es necesario saber cual es la opcion con el menor valor de la heuristica
        #ya que esto nos indica la mejor ruta que debe tomar nuestro algoritmo
        ind = heuristicas[1].index(min(heuristicas[1]))
        ruta = ind + 1

        for j in range(0,3):
            if(meta[ruta][j][2]==0):
                a = meta[ruta][j][0]
                b = meta[ruta][j][1]
                break
        
        change_turno = sweep_data(a,b,1)

        if(change_turno):
            estado[a][b] = 1
            winner_exist = check_winner(1)
    else:
        a = int(input("elige la fila 0<=a<=2: \n"))
        b = int(input("elige la columna 0<=b<=2: \n"))

        change_turno = sweep_data(a,b,2)

        if(change_turno):
            estado[a][b] = 2
            winner_exist = check_winner(2)
    
    if(change_turno):
        if(turno == 1):
            turno = 2
        else:
            turno = 1