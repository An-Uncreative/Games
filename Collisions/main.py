import pygame, sys
from dino import Dino

pygame.init()

#variables
width = 800
height = 700
dino = Dino(0.65)
block = pygame.Rect(550,200,150,100)
is_collided = False

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Playing with a dinosaur")

timing = pygame.time.Clock()

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dino.move()
    window.fill((10, 100,100 ))
    pygame.draw.rect(window, 'black', block, 5)
    dino.draw(window)
    if dino.hitbox().colliderect(block):
        is_collided = True
    else :
        is_collided = False

    dino.collision(window, is_collided)
    pygame.display.flip()
    timing.tick(60)