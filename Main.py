import pygame, sys
from Settings import *
from Level import Level
from Leaderboard import Leaderboard, LeaderboardSprite

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_over = True
menu = "level"
start_time = 0
end_time = 0
level_run = 1
level1 = Level(level_map_1, screen)
level2 = Level(level_map_2, screen)
level3 = Level(level_map_3, screen)
level4 = Level(level_map_4, screen)
level5 = Level(level_map_5, screen)
level6 = Level(level_map_6, screen)
level7 = Level(level_map_7, screen)
level8 = Level(level_map_8, screen)
level9 = Level(level_map_9, screen)

menu_text_surf = font.render("Choose your level !", False , "White")
menu_text_rect = menu_text_surf.get_rect(center = (500, 50))
sky_menu_surf = pygame.image.load("Graphics/Sky_tempo.png")
sky_menu_rect = sky_menu_surf.get_rect(topleft = (0 , 0))


#create all surf and rect of the button and the text
button1_surf = pygame.image.load("Graphics/Button.png")
button1_rect = button1_surf.get_rect(center = (300 , 150))
button1_text_surf = font.render("Niveau 1", False, "White")
button1_text_rect = button1_text_surf.get_rect(center = (300, 150))
button2_surf = pygame.image.load("Graphics/Button.png")
button2_rect = button2_surf.get_rect(center = (300 , 250))
button2_text_surf = font.render("Niveau 2", False, "White")
button2_text_rect = button2_text_surf.get_rect(center = (300, 250))
button3_surf = pygame.image.load("Graphics/Button.png")
button3_rect = button3_surf.get_rect(center = (300 , 350))
button3_text_surf = font.render("Niveau 3", False, "White")
button3_text_rect = button3_text_surf.get_rect(center = (300, 350))

button4_surf = pygame.image.load("Graphics/Button.png")
button4_rect = button4_surf.get_rect(center = (500 , 150))
button4_text_surf = font.render("Niveau 4", False, "White")
button4_text_rect = button4_text_surf.get_rect(center = (500, 150))
button5_surf = pygame.image.load("Graphics/Button.png")
button5_rect = button5_surf.get_rect(center = (500 , 250))
button5_text_surf = font.render("Niveau 5", False, "White")
button5_text_rect = button5_text_surf.get_rect(center = (500, 250))
button6_surf = pygame.image.load("Graphics/Button.png")
button6_rect = button6_surf.get_rect(center = (500 , 350))
button6_text_surf = font.render("Niveau 6", False, "White")
button6_text_rect = button6_text_surf.get_rect(center = (500, 350))

button7_surf = pygame.image.load("Graphics/Button.png")
button7_rect = button7_surf.get_rect(center = (700 , 150))
button7_text_surf = font.render("Niveau 7", False, "White")
button7_text_rect = button7_text_surf.get_rect(center = (700, 150))
button8_surf = pygame.image.load("Graphics/Button.png")
button8_rect = button8_surf.get_rect(center = (700 , 250))
button8_text_surf = font.render("Niveau 8", False, "White")
button8_text_rect = button8_text_surf.get_rect(center = (700, 250))
button9_surf = pygame.image.load("Graphics/Button.png")
button9_rect = button9_surf.get_rect(center = (700 , 350))
button9_text_surf = font.render("Niveau 9", False, "White")
button9_text_rect = button9_text_surf.get_rect(center = (700, 350))

sky_surf = pygame.image.load("Graphics/Sky_tempo.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = "level"
                    game_over = True
        else:
            if menu == "level":
                #check which buttton tthe user is clicking on and redirect to the level chosen
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1_rect.collidepoint(event.pos):
                        level_run = 1
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button2_rect.collidepoint(event.pos):
                        level_run = 2
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button3_rect.collidepoint(event.pos):
                        level_run = 3
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button4_rect.collidepoint(event.pos):
                        level_run = 4
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button5_rect.collidepoint(event.pos):
                        level_run = 5
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button6_rect.collidepoint(event.pos):
                        level_run = 6
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button7_rect.collidepoint(event.pos):
                        level_run = 7
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button8_rect.collidepoint(event.pos):
                        level_run = 8
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
                    elif button9_rect.collidepoint(event.pos):
                        level_run = 9
                        start_time = pygame.time.get_ticks()/1000
                        game_over = False
            elif menu == "leaderboard":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = "level"
                    
                    

    if game_over == False:
        #Check which  level is beeing run and display it
        if level_run == 1:
            screen.blit(sky_surf, (0, 0))
            level1.run()
            end_time = level1.display_score(start_time)
            end_time = int(end_time*1000)
            if level1.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level1.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 2:
            screen.blit(sky_surf, (0, 0))
            level2.run()
            end_time = level2.display_score(start_time)
            end_time = int(end_time*1000)
            if level2.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level2.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 3:
            screen.blit(sky_surf, (0, 0))
            level3.run()
            end_time = level3.display_score(start_time)
            end_time = int(end_time*1000)
            if level3.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level3.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 4:
            screen.blit(sky_surf, (0, 0))
            level4.run()
            end_time = level4.display_score(start_time)
            end_time = int(end_time*1000)
            if level4.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level4.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 5:
            screen.blit(sky_surf, (0, 0))
            level5.run()
            end_time = level5.display_score(start_time)
            end_time = int(end_time*1000)
            if level5.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level5.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 6:
            screen.blit(sky_surf, (0, 0))
            level6.run()
            end_time = level6.display_score(start_time)
            end_time = int(end_time*1000)
            if level6.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level6.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 7:
            screen.blit(sky_surf, (0, 0))
            level7.run()
            end_time = level7.display_score(start_time)
            end_time = int(end_time*1000)
            if level7.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level7.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 8:
            screen.blit(sky_surf, (0, 0))
            level8.run()
            end_time = level8.display_score(start_time)
            end_time = int(end_time*1000)
            if level8.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level8.game_over() == True:
                menu = "level"
                game_over = True
        elif level_run == 9:
            screen.blit(sky_surf, (0, 0))
            level9.run()
            end_time = level9.display_score(start_time)
            end_time = int(end_time*1000)
            if level9.portal_out() == True:
                menu = "leaderboard"
                game_over = True
            elif level9.game_over() == True:
                menu = "level"
                game_over = True
        
        
    else:
        if level_run == 1:
            level1 = Level(level_map_1, screen)
        if level_run == 2:
            level2 = Level(level_map_2, screen)
        if level_run == 3:
            level3 = Level(level_map_3, screen)
        if level_run == 4:
            level4 = Level(level_map_4, screen)
        if level_run == 5:
            level5 = Level(level_map_5, screen)
        if level_run == 6:
            level6 = Level(level_map_6, screen)
        if level_run == 7:
            level7 = Level(level_map_7, screen)
        if level_run == 8:
            level8 = Level(level_map_8, screen)
        if level_run == 9:
            level9 = Level(level_map_9, screen)

        if menu == "level":
            leaderboard1 = Leaderboard(leaderboard_level_1, 1, screen)
            leaderboard2 = Leaderboard(leaderboard_level_2, 2, screen)
            leaderboard3 = Leaderboard(leaderboard_level_3, 3, screen)
            screen.blit(sky_surf, (0, 0))
            screen.blit(menu_text_surf, menu_text_rect)
            screen.blit(sky_menu_surf, sky_menu_rect)
            screen.blit(menu_text_surf, menu_text_rect)
            screen.blit(button1_surf, button1_rect)
            screen.blit(button2_surf, button2_rect)
            screen.blit(button3_surf, button3_rect)
            screen.blit(button4_surf, button4_rect)
            screen.blit(button5_surf, button5_rect)
            screen.blit(button6_surf, button6_rect)
            screen.blit(button7_surf, button7_rect)
            screen.blit(button8_surf, button8_rect)
            screen.blit(button9_surf, button9_rect)
            screen.blit(button1_text_surf, button1_text_rect)
            screen.blit(button2_text_surf, button2_text_rect)
            screen.blit(button3_text_surf, button3_text_rect)
            screen.blit(button4_text_surf, button4_text_rect)
            screen.blit(button5_text_surf, button5_text_rect)
            screen.blit(button6_text_surf, button6_text_rect)
            screen.blit(button7_text_surf, button7_text_rect)
            screen.blit(button8_text_surf, button8_text_rect)
            screen.blit(button9_text_surf, button9_text_rect)
        elif menu == "leaderboard":
            if len(str(end_time)) < 6:
                end_time = (6-int(len(str(end_time))))*"0" + str(end_time)
            else:
                end_time = str(end_time)
            if level_run == 1:
                leaderboard1.display_leaderboard(end_time)
                menu = leaderboard1.menu()
            elif level_run == 2:
                leaderboard2.display_leaderboard(end_time)
                menu = leaderboard2.menu()
            elif level_run == 3:
                leaderboard3.display_leaderboard(end_time)
                menu = leaderboard3.menu()

    pygame.display.update()
    clock.tick(60)