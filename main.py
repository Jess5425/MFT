import pygame, sys
from pygame.locals import *
pygame.init()

#Definición de colores
white= (255,255,255)
#Crear la ventana
sizeVentana= (800,500)
Pantalla= pygame.display.set_mode(sizeVentana)
pygame.display.set_caption("Pantalla Principal")

while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()

    Pantalla.fill(white)
    pygame.display.flip()