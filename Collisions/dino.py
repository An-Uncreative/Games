import pygame

class Dino :
    def __init__(self, scale = 1.0):
        self.image = pygame.image.load('dino.png')
        initial_width = self.image.get_width()
        initial_height = self.image.get_height()
        self.image = pygame.transform.smoothscale(self.image, (int(initial_width * scale), int(initial_height * scale)))
        self.position = pygame.Vector2(50, 50)
        self.speed = 5

    def draw(self, window):
        window.blit(self.image, (self.position.x, self.position.y))

    def move(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT] :
            self.position.x += self.speed
        if pygame.key.get_pressed()[pygame.K_LEFT] :
            self.position.x -= self.speed
        if pygame.key.get_pressed()[pygame.K_UP] :
            self.position.y -= self.speed
        if pygame.key.get_pressed()[pygame.K_DOWN] :
            self.position.y += self.speed
