import pygame
from Support import import_folder
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        #all moovement attribute
        self.direction = pygame.math.Vector2(0, 0)
        self.r_speed = 8
        self.speed = self.r_speed
        self.gravity = 0.8
        self.shift_up = 11
        self.r_jump_speed = -13
        self.jump_speed = self.r_jump_speed
        self.speed_boost = False
        self.jump_boost = False
        self.start_time_speed = 0
        self.start_time_jump = 0
        self.new_boost_time = 0

        #animation atribute
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
    
    def import_character_assets(self):
        #import the animation file for the player
        character_path = "Graphics/Player/"
        self.animations = {"idle":[], "run":[], "jump":[], "fall":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        #animate tthe player in fonction of it's status
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        #replace the rect of the player (in case of an animation that change his dimension)
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)



    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0


        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
    
    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def switch_boost(self, start_time):
        #chose randomly  a boost when colliding with a booster
        boost = randint(1, 2)
        self.new_boost_time = start_time
        if boost == 1 and self.new_boost:
            self.start_time_speed = start_time
            self.speed_boost = True
            self.new_boost = False
        elif boost == 2 and self.new_boost:
            self.start_time_jump = start_time
            self.jump_boost = True
            self.new_boost = False

    def apply_boost(self, current_time):
        #apply the boost
        if self.speed_boost and current_time - self.start_time_speed < 5:
            self.r_speed = 12
        else:
            self.r_speed = 8
        
        if self.jump_boost and current_time - self.start_time_jump < 5:
            self.r_jump_speed = -20
            self.shift_up = 18
        else:
            self.r_jump_speed = -13
            self.shift_up = 11

        if current_time - self.new_boost_time > 1:
            self.new_boost = True

    def update(self, world_shift):
        self.get_input()
        self.get_status()
        self.animate()
        self.rect.y += world_shift