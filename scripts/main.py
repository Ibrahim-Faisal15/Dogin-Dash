import pygame
import random

import pygame.locals


# setting up the window
WIDTH = 1050
HEIGHT = WIDTH / 2
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 27

#colors values
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)




# Main function
def main():
    from player import Player  
    from lasers import Laser

    #Dynamic properties
    player_pos_x = (WIDTH//2)
    health = 100
  
    # player sprites
    idle = [pygame.image.load('asset/player_sprite/idle/00_idle.png'), pygame.image.load('asset/player_sprite/idle/01_idle.png'), pygame.image.load('asset/player_sprite/idle/02_idle.png'), pygame.image.load('asset/player_sprite/idle/03_idle.png')]
    walkRight = [pygame.image.load('asset/player_sprite/Walk/00_Walk.png'), pygame.image.load('asset/player_sprite/Walk/01_Walk.png'), pygame.image.load('asset/player_sprite/Walk/02_Walk.png'), pygame.image.load('asset/player_sprite/Walk/03_Walk.png')]
    walkLeft = [pygame.image.load('asset/player_sprite/Walk/00_Walk.png'), pygame.image.load('asset/player_sprite/Walk/01_Walk.png'), pygame.image.load('asset/player_sprite/Walk/02_Walk.png'), pygame.image.load('asset/player_sprite/Walk/03_Walk.png')]
    
    size = (120, 120)

    for i in range(len(idle)):
        idle[i] = pygame.transform.scale(idle[i], size)

    for i in range(len(walkRight)):
        walkRight[i] = pygame.transform.scale(walkRight[i], size) 

    for i in range(len(walkLeft)):
        walkLeft[i] = pygame.transform.scale(walkLeft[i], size)   

    for i in range(len(walkLeft)):
        walkLeft[i] = pygame.transform.flip(walkLeft[i], True, False)
    
   
    # background_img
    background_img = pygame.image.load("asset/background_img.jpg")
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT+90))
    new_lasers = []
    time_interval = 1000
    next_object_time = 0

    # instances
    player = Player(GREEN, 50, 5, player_pos_x, (HEIGHT-100), health, idle, SCREEN, walkRight, walkLeft)
    laser = Laser(SCREEN)

    


   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        current_time = pygame.time.get_ticks()

     
        #Creating player object
        player.create_player()

        
        #Player Control System
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_pos_x < WIDTH-50:
            player.move("RIGHT")
            
        elif keys[pygame.K_LEFT] and player_pos_x > 0:
              player.move("LEFT")
        else:
            player.idle()
            
               

        

        if current_time > next_object_time and len(new_lasers) < 8:
            next_object_time += time_interval
            new_lasers.append(Laser(SCREEN))


        new_lasers = [laser for laser in new_lasers if laser.pos_x <= SCREEN.get_width()-100]

      
      
                              
        for laser in new_lasers:
            laser.create_laser()

            laser.move()
            if len(new_lasers) >= 6 and laser.pos_y >= (SCREEN.get_height()):
                new_lasers.pop(0)
                # print(len(new_lasers))
                
        pygame.display.flip()

        SCREEN.blit(background_img , (0,0))


        
       
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()


