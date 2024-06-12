import pygame
import random
import math
import time

import pygame.locals


# setting up the window
WIDTH = 1050
HEIGHT = WIDTH / 2
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 27

# colors values
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

current_time = 0
game_score = 0

# text
pygame.font.init()
font =  pygame.font.SysFont('Comic Sans MS', 45)
# text_surface = font.render(str(game_score), False, (0, 0, 0))


def gameOver_func():
    main()


# Main function
def main():
    from player import Player
    from lasers import Laser
    from menu import Menu


    global laser, player, current_time, game_score

    # Dynamic properties
    player_pos_x = WIDTH // 2
    health = 100

    # background_img
    background_img = pygame.image.load("asset/background_img.jpg")
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT + 90))
    gameOver_img = pygame.image.load("asset/game_over_screen.png")
    gameOver_img = pygame.transform.scale(gameOver_img, (WIDTH, HEIGHT))
    game_over = False

    new_lasers = []
    time_interval = 15
    next_object_time = 0

    # instances
    player = Player(GREEN, 50, 5, player_pos_x, (HEIGHT - 100), health, SCREEN)
    laser = Laser(SCREEN)
    menu = Menu(SCREEN)



    running = True
    while running:
      
         SCREEN.blit(background_img, (0, 0))
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pos = pygame.mouse.get_pos()
                relative_pos_startBtn = pos[0] - menu.start_btn_rect.left, pos[1] - menu.start_btn_rect.top
                relative_pos_endBtn = pos[0] - menu.end_btn_rect.left, pos[1] - menu.end_btn_rect.top
                if event.type == pygame.MOUSEBUTTONDOWN:
                     if menu.start_btn_rect.collidepoint(*pos) and menu.start_btn_mask.get_at(relative_pos_startBtn):
                      game_score = 0
                   
                      while running:
                        game_score += 1
                      
                        text_surface = font.render(str(game_score), True, (0, 0, 0))
                        SCREEN.blit(text_surface, (0, 0))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            
                        
                        if game_over:
                            SCREEN.blit(gameOver_img, (0, 0))
                            pygame.display.update()

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_BACKSPACE:   
                                        SCREEN.blit(background_img, (0, 0))
                                        game_over = False

                                        current_time = 0
                                       
                                        gameOver_func()

                        else:
                            current_time += 1

                            player.update()
                            laser.update()

                            # Player Control System
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_RIGHT] and player_pos_x <= WIDTH - 90:
                                player.move("RIGHT")

                            elif keys[pygame.K_LEFT] and player_pos_x > 0:
                                player.move("LEFT")
                            else:
                                player.idle()

                            if current_time > next_object_time and len(new_lasers) < 15:
                                next_object_time += time_interval
                                new_lasers.append(Laser(SCREEN))

                            new_lasers = [
                                laser for laser in new_lasers if laser.pos_x <= SCREEN.get_width() - 100
                            ]

                            for laser in new_lasers:
                                laser.create_laser()
                                laser.move()

                                if player.idle_mask.overlap(
                                    laser.laser_mask,
                                    (laser.pos_x - player.pos_x, laser.pos_y - player.pos_y),
                                ):
                                    current_time = 0
                                    game_over = True

                                if laser.pos_y >= (SCREEN.get_height()):
                                    new_lasers.pop(0)

                            pygame.display.update()

                            SCREEN.blit(background_img, (0, 0))

                            clock.tick(FPS)
                            # print(current_time)

                        print(game_score)


                     
                     if menu.end_btn_rect.collidepoint(*pos) and menu.end_btn_mask.get_at(relative_pos_endBtn):                       
                        running = False

                    
       
         menu.menu_layout()

                   

         pygame.display.update()



    pygame.quit()


if __name__ == "__main__":

    main()
