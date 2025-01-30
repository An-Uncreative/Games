import pygame
 
class Button:
    #initialize the button image
    def __init__(self, imagepath, position, scale= 1.0):
        self.image = pygame.image.load(imagepath).convert_alpha()
        initial_width = self.image.get_width()
        initial_height = self.image.get_height()
        self.image = pygame.transform.smoothscreen(self.image, (int(initial_width * scale), int(initial_height * scale)))
        self.rect = self.image.get_rect(topleft = position)
        self.pressed = False

    #draw the button image
    def draw(self, window):
        window.blit(self.image, self.rect)

    #draw the background image
    def draw_background(self, window):
        window.blit(self.image, self.position)

    #check if the button is pressed
    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True
            if not mouse_pressed:
                self.pressed = False

        return False