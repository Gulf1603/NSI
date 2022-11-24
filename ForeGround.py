import pygame

class Foreground(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        #create the image of the object
        if type == "M":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_1.png").convert_alpha()
        elif type == "A":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_2.png").convert_alpha()
        elif type == "H":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_3.png").convert_alpha()
        elif type == "I":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_4.png").convert_alpha()
        elif type == "V":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_5.png").convert_alpha()
        elif type == "B":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_6.png").convert_alpha()
        elif type == "W":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_7.png").convert_alpha()
        elif type == "E":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_8.png").convert_alpha()
        elif type == "N":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_9.png").convert_alpha()
        elif type == "Q":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_10.png").convert_alpha()
        elif type == "U":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_11.png").convert_alpha()
        elif type == "X":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_12.png").convert_alpha()
        elif type == "J":
            self.image = pygame.image.load("Graphics/Bloc_foreground/Bloc_13.png").convert_alpha()

        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift, y_shift):
        #move  the object with the world shift
        self.rect.x += x_shift 
        self.rect.y += y_shift