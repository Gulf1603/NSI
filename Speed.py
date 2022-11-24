import pygame

class Speed(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("Graphics/Speed.png")
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift