import pygame, sys

pygame.init()

height= 600
width = 800
posx = 400
posy = 300
leftright_displacement = 0
updown_displacement = 0
background_visible = True

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("move the ball on the screen")

#set the refresh rate
clock = pygame.time.Clock()
# background = pygame.image.load("background.png").convert()

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            background_visible = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftright_displacement = -3
            elif event.key == pygame.K_RIGHT:
                leftright_displacement = 3
            elif event.key == pygame.K_UP:
                updown_displacement = -3
            elif event.key == pygame.K_DOWN:
                updown_displacement = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                leftright_displacement = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                updown_displacement = 0
    
    posx += leftright_displacement
    posy += updown_displacement

    window.fill((10,100,100))
    pygame.draw.circle(window, pygame.Color('white'), (posx, posy), 15)
    if background_visible:
        window.blit(pygame.image.load("graphics/background.png").convert(), (0,0))

    pygame.display.update()
    clock.tick(60)