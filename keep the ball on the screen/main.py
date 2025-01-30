import pygame, sys
from button import Button

pygame.init()

#Variables
height= 600
width = 800
posx = 400
posy = 350
leftright_displacement = 0
updown_displacement = 0
game_started = False

#The game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("keep the ball on the screen")

#buttons and image
background = Button("graphics/background.png", (0,0))
start_button = Button("graphics/start_button.png", (300, 150), 0.65)
exit_button = Button("graphics/exit_button.png", (300, 300), 0.65)

#set the refresh rate
clock = pygame.time.Clock()

#Game loop
while True :
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Check if the start button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_pressed():
                game_started = True
            #Check if the exit button is pressed
            if exit_button.is_pressed():
                 pygame.quit()
                 sys.exit()
        #Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftright_displacement = -3
            elif event.key == pygame.K_RIGHT:
                leftright_displacement = 3
            elif event.key == pygame.K_UP:
                updown_displacement = -3
            elif event.key == pygame.K_DOWN:
                updown_displacement = 3
    #start or quit  the game when the right buttons are clicked on
    if game_started:
            posx += leftright_displacement
            posy += updown_displacement

            window.fill((10, 100, 100))
            pygame.draw.circle(window, pygame.Color('white'), (posx, posy), 15)
    else:
            # window.blit(pygame.image.load("graphics/background.png").convert(), (0, 0))
            background.draw(window)
            start_button.draw(window)
            exit_button.draw(window)

    pygame.display.update()
    clock.tick(60)