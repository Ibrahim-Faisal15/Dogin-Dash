import pygame
import random


# Screen dimensions
WIDTH = 1300
HEIGHT = WIDTH / 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 40

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)



# Main function
def main():

    #Dynamic properties
    player_pos_x = (WIDTH//2)
    health = 100

    laser_pos_x = random.randrange(0, WIDTH-60)




    from player import Player  
    from lasers import Laser

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        screen.fill(WHITE)

        
        # Create a Player object
        player = Player(GREEN, 50, 20, player_pos_x, (HEIGHT-100), health)
        player.create_player(screen)
       

        #Create a Laser Object
        # laser =  Lasers(RED, 10, 20, 10, 10, laser_pos_x, HEIGHT)
        laser = Laser(RED, 50, 20, laser_pos_x, 23, 5)
        laser.create_laser(screen)

        pygame.display.flip()
     
 

        
        #Control System
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_pos_x < WIDTH-50:
            player_pos_x += player.velocity_x

            
        elif keys[pygame.K_LEFT] and player_pos_x > 0:
             player_pos_x -= player.velocity_x



    
        
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
