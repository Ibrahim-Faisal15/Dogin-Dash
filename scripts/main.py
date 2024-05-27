import pygame
import random


# setting up the window
WIDTH = 1300
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
    laser_pos_y = 0
    laser_width = random.randrange(30,60)
    laser_height = random.randrange(50,90)
    attack = 10

    player = Player(GREEN, 50, 10, player_pos_x, (HEIGHT-100), health)
    laser = Laser(RED, laser_height, laser_width, 5,  laser_pos_y, attack, SCREEN)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(WHITE)

     
        #Creating player object
        player.create_player(SCREEN)
       
           
        #Player Control System
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_pos_x < WIDTH-50:
            player.move("RIGHT")
            
        elif keys[pygame.K_LEFT] and player_pos_x > 0:
              player.move("LEFT")
               
        #Create a Laser Object 
        laser.create_laser()
        laser.move()
        laser.check_hit()

        if(laser.hit):
                laser.pos_y = 0
                laser.random_gen()
                laser.hit = False
                 
        pygame.display.flip()
       
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()


