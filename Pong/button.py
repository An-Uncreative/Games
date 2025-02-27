import pygame

class Button:
    def __init__(self, imagepath, position, scale = 1.0):
        self.image = pygame.image.load(imagepath)
        initial_width = self.image.get_width()
        initial_height = self.image.get_height()
        self.image = pygame.transform.smoothscale(self.image, (int(initial_width * scale), int(initial_height * scale)))
        self.rec = self.image.get_rect(topleft=position)
        self.pressed = False

    def draw(self, window):
        window.blit(self.image, self.rec)

    def draw_backgroune(self, window):
        window.blit(self.image, self.position)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if self.rec.collidepoint(mouse_pos):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True
            if not mouse_pressed:
                self.pressed = False
            
        return False