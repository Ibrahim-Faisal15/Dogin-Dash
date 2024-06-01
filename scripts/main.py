import pygame
import random

import pygame.locals


# setting up the window
WIDTH = 1050
HEIGHT = WIDTH / 2
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 40

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

    player = Player(GREEN, 50, 5, player_pos_x, (HEIGHT-100), health)
    laser = Laser(SCREEN)
    new_lasers = []
    time_interval = 1000
    next_object_time = 0

    #Images
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        current_time = pygame.time.get_ticks()

     
        #Creating player object
        player.create_player(SCREEN)

        # image
        background_img = pygame.image.load("asset/background_img.jpg")
        background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT+90))
        

        
         
        #Player Control System
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_pos_x < WIDTH-50:
            player.move("RIGHT")
            
        elif keys[pygame.K_LEFT] and player_pos_x > 0:
              player.move("LEFT")
               

        

        if current_time > next_object_time and len(new_lasers) < 6:
            next_object_time += time_interval
            new_lasers.append(Laser(SCREEN))


        new_lasers = [laser for laser in new_lasers if laser.pos_x <= SCREEN.get_width()-100]

      
      
                              
        for laser in new_lasers:
            laser.create_laser()

            laser.move()
            if len(new_lasers) >= 5 and laser.pos_y >= (SCREEN.get_height()):
                new_lasers.pop(0)
                print(len(new_lasers))
                
        pygame.display.flip()

        SCREEN.blit(background_img , (0,0))


        
       
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()


