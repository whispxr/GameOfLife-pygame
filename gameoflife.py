import os
import random
import pygame
clear = lambda: os.system('cls')

def grid(x,y):
    mapa = []
    for i in range(x):
        mapa.append([])
        for j in range(y):
            mapa[i].append(random.randint(0,1))
    return mapa


def showmap(grid): #mapa en consola
    for i in grid:
        print(i)


def neighbors(x, y, map):
    rows = len(map)
    cols = len(map[0])
    vecinos = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        #  posición no salga de los límites
        if 0 <= nx < rows and 0 <= ny < cols and map[nx][ny] == 1:
            vecinos += 1
    
    return vecinos



# Reglas:
# Each cell with one or no neighbors dies, as if by solitude.
# Each cell with four or more neighbors dies, as if by overpopulation.
# Each cell with two or three neighbors survives.
# For a space that is empty or unpopulated:
# Each cell with three neighbors becomes populated


def status(x, y, vecinos, map):
    if map[x][y] == 1:
        if vecinos < 2 or vecinos > 3:
            map[x][y] = 0  # Muere por soledad o sobrepoblación
    else:
        if vecinos == 3:
            map[x][y] = 1  #  nueva celula
    return map


def actualizarmapa(mapa):
    new_mapa = [fila[:] for fila in mapa]
    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):
            vecinos = neighbors(fila, columna, mapa)
            new_mapa = status(fila, columna, vecinos, new_mapa)

    return new_mapa



def mostrar_mapa(mapa):
    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):
            x = columna * TAMAÑO_CELDA
            y = fila * TAMAÑO_CELDA

            color = blanco if mapa[fila][columna] == 1 else negro
            pygame.draw.rect(pantalla, color, (x, y, TAMAÑO_CELDA, TAMAÑO_CELDA))
            # borde
            pygame.draw.rect(pantalla, (255, 255, 255), (x, y, TAMAÑO_CELDA, TAMAÑO_CELDA), 1)




#====================================================================


mapa = grid(100,100)


pygame.init()
ancho, alto = 1000, 1000
TAMAÑO_CELDA = 10
COLOR_FONDO = (30, 30, 30)
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Matriz en Pygame")
blanco = (255, 255, 255)  # Color para el 1
negro = (0, 0, 0)      # Color para el 0
ejecutando = True
# Configuración de FPS
FPS = 20
reloj = pygame.time.Clock()



while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    pantalla.fill((0, 0, 0))  


    mapa = actualizarmapa(mapa)
    mostrar_mapa(mapa)


    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()

