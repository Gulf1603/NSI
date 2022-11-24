import pygame, shelve

pygame.init()
font = pygame.font.Font("font/Pixeltype.ttf", 25)
font_big = pygame.font.Font("font/Pixeltype.ttf", 50)

leaderboard_background = pygame.image.load("Graphics/Leaderboard_background.png")
leaderboard_background_rect = leaderboard_background.get_rect(topleft = (200, 100))
leaderboard_text = pygame.image.load("Graphics/Leaderboard_text.png")
leaderboard_text_rect = leaderboard_text.get_rect(topleft = (300, 320))
sky_surf = pygame.image.load("Graphics/Sky_tempo.png")

class LeaderboardSprite(pygame.sprite.Sprite):
    def __init__(self, string, pos):
        super().__init__()
        self.image = font.render(string, False, "Black")
        self.rect = self.image.get_rect(topleft = pos)

class Leaderboard(pygame.sprite.Sprite):
    def __init__(self, leaderboard_list, leaderboard_number, surface):
        self.display_surface = surface
        self.index = str(leaderboard_number)
        self.leaderboard = leaderboard_list
        self.setup_leaderboard(leaderboard_list)

        self.menu_input = False
        self.user_input = False
        self.username = ""
        self.end_time = 0
        self.score_slice = slice(-7, -1)
        self.player_slice = slice(11, -22)

    def setup_leaderboard(self, leaderboard):
        self.leaderboard_sprite = pygame.sprite.Group()
        compteur = 0

        for string in leaderboard:
            leaderboard_sprite = LeaderboardSprite(string, (310, compteur*25+160))
            self.leaderboard_sprite.add(leaderboard_sprite)
            compteur += 1

    def get_name(self):
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            if leaderboard_text_rect.collidepoint(pygame.mouse.get_pos()):
                self.user_input = True
            elif leaderboard_background_rect.collidepoint(pygame.mouse.get_pos()):
                self.user_input = False

        keys = pygame.key.get_pressed()

        if self.user_input:
            if keys[pygame.K_RETURN]:
                self.check_leaderboard()
                self.save_leaderboard()
                self.menu_input = True
            elif keys[pygame.K_BACKSPACE]:
                self.username = self.username[:-1]
            elif keys[pygame.K_a]:
                self.username += "a"
            elif keys[pygame.K_b]:
                self.username += "b"
            elif keys[pygame.K_c]:
                self.username += "c"
            elif keys[pygame.K_d]:
                self.username += "d"
            elif keys[pygame.K_e]:
                self.username += "e"
            elif keys[pygame.K_f]:
                self.username += "f"
            elif keys[pygame.K_g]:
                self.username += "g"
            elif keys[pygame.K_h]:
                self.username += "h"
            elif keys[pygame.K_i]:
                self.username += "i"
            elif keys[pygame.K_j]:
                self.username += "j"
            elif keys[pygame.K_k]:
                self.username += "k"
            elif keys[pygame.K_l]:
                self.username += "l"
            elif keys[pygame.K_m]:
                self.username += "m"
            elif keys[pygame.K_n]:
                self.username += "n"
            elif keys[pygame.K_o]:
                self.username += "o"
            elif keys[pygame.K_p]:
                self.username += "p"
            elif keys[pygame.K_q]:
                self.username += "q"
            elif keys[pygame.K_r]:
                self.username += "r"
            elif keys[pygame.K_s]:
                self.username += "s"
            elif keys[pygame.K_t]:
                self.username += "t"
            elif keys[pygame.K_u]:
                self.username += "u"
            elif keys[pygame.K_v]:
                self.username += "v"
            elif keys[pygame.K_w]:
                self.username += "w"
            elif keys[pygame.K_x]:
                self.username += "x"
            elif keys[pygame.K_y]:
                self.username += "y"
            elif keys[pygame.K_z]:
                self.username += "z"
            elif keys[pygame.K_8]:
                self.username += "_"


        self.username_sprite = font_big.render(self.username, False, "Black")
        self.display_surface.blit(self.username_sprite, (310, 330))

    def check_leaderboard(self):
        if self.username == self.leaderboard[0][self.player_slice] and self.end_time < int(self.leaderboard[0][self.score_slice]):
            self.leaderboard[0] =f"#1 :       {self.username}       -       {self.true_end_time} "
        elif self.username == self.leaderboard[1][self.player_slice] and self.end_time < int(self.leaderboard[1][self.score_slice]):
            self.leaderboard[1] =f"#2 :       {self.username}       -       {self.true_end_time} "
        elif self.username == self.leaderboard[2][self.player_slice] and self.end_time < int(self.leaderboard[2][self.score_slice]):
            self.leaderboard[2] =f"#3 :       {self.username}       -       {self.true_end_time} "
        elif self.username == self.leaderboard[3][self.player_slice] and self.end_time < int(self.leaderboard[3][self.score_slice]):
            self.leaderboard[3] =f"#4 :       {self.username}       -       {self.true_end_time} "
        elif self.username == self.leaderboard[4][self.player_slice] and self.end_time < int(self.leaderboard[4][self.score_slice]):
            self.leaderboard[4] =f"#5 :       {self.username}       -       {self.true_end_time} "
        elif self.end_time < int(self.leaderboard[4][self.score_slice]):
            if self.end_time < int(self.leaderboard[3][self.score_slice]):
                if self.end_time < int(self.leaderboard[2][self.score_slice]):
                    if self.end_time < int(self.leaderboard[1][self.score_slice]):
                        if self.end_time < int(self.leaderboard[0][self.score_slice]):
                            self.leaderboard[4] =f"#5 :       {self.leaderboard[3][self.player_slice]}       -       {self.leaderboard[3][self.score_slice]} "
                            self.leaderboard[3] =f"#4 :       {self.leaderboard[2][self.player_slice]}       -       {self.leaderboard[2][self.score_slice]} "
                            self.leaderboard[2] =f"#3 :       {self.leaderboard[1][self.player_slice]}       -       {self.leaderboard[1][self.score_slice]} "
                            self.leaderboard[1] =f"#2 :       {self.leaderboard[0][self.player_slice]}       -       {self.leaderboard[0][self.score_slice]} "
                            self.leaderboard[0] =f"#1 :       {self.username}       -       {self.true_end_time} "
                        else:
                            self.leaderboard[4] =f"#5 :       {self.leaderboard[3][self.player_slice]}       -       {self.leaderboard[3][self.score_slice]} "
                            self.leaderboard[3] =f"#4 :       {self.leaderboard[2][self.player_slice]}       -       {self.leaderboard[2][self.score_slice]} "
                            self.leaderboard[2] =f"#3 :       {self.leaderboard[1][self.player_slice]}       -       {self.leaderboard[1][self.score_slice]} "
                            self.leaderboard[1] =f"#2 :       {self.username}       -       {self.true_end_time} "
                    else:
                        self.leaderboard[4] =f"#5 :       {self.leaderboard[3][self.player_slice]}       -       {self.leaderboard[3][self.score_slice]} "
                        self.leaderboard[3] =f"#4 :       {self.leaderboard[2][self.player_slice]}       -       {self.leaderboard[2][self.score_slice]} "
                        self.leaderboard[2] =f"#3 :       {self.username}       -       {self.true_end_time} "
                else:
                    self.leaderboard[4] =f"#5 :       {self.leaderboard[3][self.player_slice]}       -       {self.leaderboard[3][self.score_slice]} "
                    self.leaderboard[3] =f"#4 :       {self.username}       -       {self.true_end_time} "
            else:
                self.leaderboard[4] =f"#5 :       {self.username}       -       {self.true_end_time} "

    def menu(self):
        if self.menu_input:
            return("level")
        else:
            return("leaderboard")

    def save_leaderboard(self):
        leaderboard = shelve.open("leaderboard.db")
        leaderboard[f"{self.index}"] = self.leaderboard

    def display_leaderboard(self, end_time):
        self.display_surface.blit(sky_surf, (0, 0))
        self.display_surface.blit(leaderboard_background, leaderboard_background_rect)
        self.display_surface.blit(leaderboard_text, leaderboard_text_rect)
        score_surface = font_big.render(f'{self.end_time}', False, "White")
        score_rect = score_surface.get_rect(center = (500, 50))
        self.display_surface.blit(score_surface, score_rect)
        self.leaderboard_sprite.update()
        self.leaderboard_sprite.draw(self.display_surface)
        self.get_name()
        self.end_time = int(end_time)
        if len(str(end_time)) < 6:
            self.true_end_time = str((6-int(len(str(end_time))))*"0" + str(end_time))
        else:
            self.true_end_time = str(end_time)