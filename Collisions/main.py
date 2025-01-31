import pygame, sys
from dino import Dino

pygame.init()

#variables
width = 800
height = 700
dino = Dino(0.65)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Playing with a dinosaur")

timing = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dino.move()
    window.fill((10, 100,100 ))
    dino.draw(window)
    pygame.display.flip()
    timing.tick(60)