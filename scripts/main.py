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

    player = Player(GREEN, 50, 20, player_pos_x, (HEIGHT-100), health)
    laser = Laser(SCREEN)
    new_lasers = []
    time_interval = 100
    
    next_object_time = 0
    
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(WHITE)
        
        current_time = pygame.time.get_ticks()

     
        #Creating player object
        player.create_player(SCREEN)
        


       
           
        #Player Control System
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_pos_x < WIDTH-50:
            player.move("RIGHT")
            
        elif keys[pygame.K_LEFT] and player_pos_x > 0:
              player.move("LEFT")
               
        #Create a Laser Object 
        # laser.create_laser()
       
        # laser.move()
        # laser.check_hit()
        

        if current_time > next_object_time:
            next_object_time += time_interval
            new_lasers.append(Laser(SCREEN))
            print(new_lasers)
            
    
                                     
        for laser in new_lasers:
            laser.create_laser()
            laser.move()
            if len(new_lasers) >= 2 and laser.check_hit() == True:
                new_lasers.pop(0)

           

        







                 
        pygame.display.flip()

        
       
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()


