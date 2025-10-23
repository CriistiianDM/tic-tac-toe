import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi primer juego")

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

jugador = pygame.Rect(375, 275, 50, 50)
velocidad = 5

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, ROJO, jugador)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
