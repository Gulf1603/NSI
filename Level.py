import pygame
from Leaderboard import Leaderboard
from Portal import Portal
from Player import Player
from Tile import Tile
from ForeGround import Foreground
from Spike import Spike
from Speed import Speed

pygame.init()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.current_x = 0
        self.current_time = 0

    def setup_level(self, layout):
        #create all sprite group
        self.tiles = pygame.sprite.Group()
        self.foregrounds = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.speeds = pygame.sprite.Group()
        self.portal = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()

        #cycle in the layout given
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                y = row_index * 50
                x = col_index * 50

                if cell == "X":
                    if x == 0 or row_index == 0:
                        type = "M"
                    #checks the block on all four side and eventually the block on the corner
                    elif row[col_index-1] == "X" and row[col_index+1] == "X" and layout[row_index-1][col_index] == "X" and layout[row_index+1][col_index] == "X":
                        if layout[row_index-1][col_index-1] != "X":
                            type = "J"
                        elif layout[row_index-1][col_index+1] != "X":
                            type = "X"
                        elif layout[row_index+1][col_index+1] != "X":
                            type = "Q"
                        elif layout[row_index+1][col_index-1] != "X":
                            type = "U"
                        else:
                            type = "M"
                    elif row[col_index-1] == "X" and row[col_index+1] == "X" and layout[row_index-1][col_index] != "X" and layout[row_index+1][col_index] == "X":
                        type = "H"
                    elif row[col_index-1] == "X" and row[col_index+1] == "X" and layout[row_index-1][col_index] == "X" and layout[row_index+1][col_index] != "X":
                        type = "E"
                    elif row[col_index-1] != "X" and row[col_index+1] == "X" and layout[row_index-1][col_index] == "X" and layout[row_index+1][col_index] == "X":
                        type = "V"
                    elif row[col_index-1] != "X" and row[col_index+1] == "X" and layout[row_index-1][col_index] != "X" and layout[row_index+1][col_index] == "X":
                        type = "A"
                    elif row[col_index-1] != "X" and row[col_index+1] == "X" and layout[row_index-1][col_index] == "X" and layout[row_index+1][col_index] != "X":
                        type = "W"
                    elif row[col_index-1] == "X" and row[col_index+1] != "X" and layout[row_index-1][col_index] == "X" and layout[row_index+1][col_index] == "X":
                        type = "B"
                    elif row[col_index-1] == "X" and row[col_index+1] != "X" and layout[row_index-1][col_index] != "X" and layout[row_index+1][col_index] == "X":
                        type = "I"
                    elif row[col_index-1] == "X" and row[col_index+1] != "X" and layout[row_index-1][col_index] == "X" and layout[row_index+1][col_index] != "X":
                        type = "N"
                    else:
                        pass
                    
                    tile = Tile((x, y), type)
                    self.tiles.add(tile)

                elif cell == "Y":
                    if x == 0 or row_index == 0:
                        type = "M"
                    #same as the basic tile
                    elif row[col_index-1] == "Y" and row[col_index+1] == "Y" and layout[row_index-1][col_index] == "Y" and layout[row_index+1][col_index] == "Y":
                        if layout[row_index-1][col_index-1] != "Y":
                            type = "J"
                        elif layout[row_index-1][col_index+1] != "Y":
                            type = "Y"
                        elif layout[row_index+1][col_index+1] != "Y":
                            type = "Q"
                        elif layout[row_index+1][col_index-1] != "Y":
                            type = "U"
                        else:
                            type = "M"
                    elif row[col_index-1] == "Y" and row[col_index+1] == "Y" and layout[row_index-1][col_index] != "Y" and layout[row_index+1][col_index] == "Y":
                        type = "H"
                    elif row[col_index-1] == "Y" and row[col_index+1] == "Y" and layout[row_index-1][col_index] == "Y" and layout[row_index+1][col_index] != "Y":
                        type = "E"
                    elif row[col_index-1] != "Y" and row[col_index+1] == "Y" and layout[row_index-1][col_index] == "Y" and layout[row_index+1][col_index] == "Y":
                        type = "V"
                    elif row[col_index-1] != "Y" and row[col_index+1] == "Y" and layout[row_index-1][col_index] != "Y" and layout[row_index+1][col_index] == "Y":
                        type = "A"
                    elif row[col_index-1] != "Y" and row[col_index+1] == "Y" and layout[row_index-1][col_index] == "Y" and layout[row_index+1][col_index] != "Y":
                        type = "W"
                    elif row[col_index-1] == "Y" and row[col_index+1] != "Y" and layout[row_index-1][col_index] == "Y" and layout[row_index+1][col_index] == "Y":
                        type = "B"
                    elif row[col_index-1] == "Y" and row[col_index+1] != "Y" and layout[row_index-1][col_index] != "Y" and layout[row_index+1][col_index] == "Y":
                        type = "I"
                    elif row[col_index-1] == "Y" and row[col_index+1] != "Y" and layout[row_index-1][col_index] == "Y" and layout[row_index+1][col_index] != "Y":
                        type = "N"
                    
                    tile = Foreground((x, y), type)
                    self.foregrounds.add(tile)

                elif cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif cell == "O":
                    portal_sprite = Portal((x, y))
                    self.portal.add(portal_sprite)
                elif cell == "S":
                    spike_sprite = Spike((x, y))
                    self.spikes.add(spike_sprite)
                elif cell == "B":
                    speed_sprite = Speed((x, y))
                    self.speeds.add(speed_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        #allows the player to move freely in the whole level
        if player_x < 300 and direction_x < 0:
            self.world_shift_x = player.r_speed
            player.speed = 0
        elif player_x > 700 and direction_x > 0:
            self.world_shift_x = -player.r_speed
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = player.r_speed

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < 100 and direction_y < 0:
            self.world_shift_y = player.shift_up
            player.jump_speed = 0
        elif player_y > 400 and direction_y > 0:
            self.world_shift_y = -25
            player.jump_speed = 0
        else:
            self.world_shift_y = 0
            player.jump_speed = player.r_jump_speed

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
            
            if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
                player.on_left = False
            if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
                player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False
                    
    def game_over(self):
        player = self.player.sprite

        if player.rect.top > 500:
            fall_out = True
        else :
            fall_out = False

        for sprite in self.spikes.sprites():
            if sprite.rect.colliderect(player.rect):
                spiked = True
                break
            else:
                spiked = False

        return(fall_out or spiked)

    def portal_out(self):
        player = self.player.sprite
        portal = self.portal.sprite
        if player.rect.colliderect(portal.rect):
            return(True)
        else:
            return(False)

    def boost(self):
        player = self.player.sprite
        for sprite in self.speeds.sprites():
            if sprite.rect.colliderect(player.rect):
                player.switch_boost(self.current_time)

    def display_score(self, start_time):
        self.start_time = start_time
        self.current_time = float(int((pygame.time.get_ticks()/1000 - start_time)*10)/10)
        self.timer = float(int((pygame.time.get_ticks()/1000 - start_time)*1000)/1000)
        self.timer_surf = font.render(f"{self.current_time}", False, "White")
        self.timer_rect = self.timer_surf.get_rect(center = (500, 50))
        self.display_surface.blit(self.timer_surf, self.timer_rect) 
        return(self.timer)

    def run(self):
        player = self.player.sprite
        self.boost()
        player.apply_boost(self.current_time)
        self.scroll_x()
        self.scroll_y()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.foregrounds.update(self.world_shift_x, self.world_shift_y)
        self.portal.update(self.world_shift_x, self.world_shift_y)
        self.spikes.update(self.world_shift_x, self.world_shift_y)
        self.speeds.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)
        self.foregrounds.draw(self.display_surface)
        self.portal.draw(self.display_surface)
        self.spikes.draw(self.display_surface)
        self.speeds.draw(self.display_surface)
        self.player.update(self.world_shift_y)
        self.player.draw(self.display_surface)