import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("Graphics/Portal.png")
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift