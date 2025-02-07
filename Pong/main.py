import pygame, sys

pygame.init()

#Functions
def ball_movement():
    global ball_speedx, ball_speedy
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0 or ball.bottom >= window_height :
        ball_speedy *= -1
    if ball.left <= 0 or ball.right >= window_width :
        ball_speedx *= -1
    
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle) :
        ball_speedx *= -1

def player_paddle_movement():
    player_paddle.y += player_paddlespeed
    if player_paddle.top <= 0 :
        player_paddle.top = 0
    if player_paddle.bottom >= window_height :
        player_paddle.bottom = window_height

def computer_paddle_movement():
    global computer_paddlespeed
    computer_paddle.y += computer_paddlespeed

    # if computer_paddle.centery == ball.centery :
    #     computer_paddlespeed = 0
    if ball.centery <= computer_paddle.centery :
        computer_paddlespeed = -6
    if ball.centery >= computer_paddle.centery :
        computer_paddlespeed = 6

    if computer_paddle.top <= 0 :
        computer_paddle.top = 0
    if computer_paddle.bottom >= window_height :
        computer_paddle.bottom = window_height
#variables
window_width = 1100
window_height = 700
ball_speedx = 0
ball_speedy = 0
player_paddlespeed = 0
computer_paddlespeed = 0
game_started = False

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

#object properties
ball = pygame.Rect(0, 0, 20, 20)
ball.center = (window_width // 2, window_height // 2)
computer_paddle = pygame.Rect(0, 0, 20, 100)
computer_paddle.midleft = (0, window_height // 2)
player_paddle = pygame.Rect(0, 0, 20, 100)
player_paddle.midright = (window_width, window_height // 2)

#Timing
timing = pygame.time.Clock()

#Game loop
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN :
                game_started = True
                ball_speedx = 6
                ball_speedy = 6
            if event.key == pygame.K_DOWN :
                player_paddlespeed = 7
            if event.key == pygame.K_UP :
                player_paddlespeed = -7
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP :
                player_paddlespeed = 0

    player_paddle_movement()
    if game_started :
        ball_movement()
        computer_paddle_movement()

    window.fill('black')
    #Draw the shapes
    pygame.draw.aaline(window, 'white', (window_width // 2, 0), (window_width // 2, window_height))
    pygame.draw.ellipse(window, (255, 255, 255), ball)
    pygame.draw.rect(window, 'white', computer_paddle)
    pygame.draw.rect(window, (255, 255, 255), player_paddle)
    pygame.display.flip()
    timing.tick(60)