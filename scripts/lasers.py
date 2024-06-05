import pygame
import random

class Laser:
    def __init__(self, screen):
        self.color = (255, 0, 0)
        # self.height = random.randrange(50,90)
        # self.width = random.randrange(30,60)
        self.velocity_y = 3
        self.pos_x = random.randrange(0, 1300-60)+100
        self.pos_y = 0
        self.attack = 50
        self.screen = screen
        self.hit = False
        self.laser_size = (100, 170)



        #sprites
        self.laser_sprites = [pygame.image.load("asset/laser_sprite/00_Astroids.png"),
                              pygame.image.load("asset/laser_sprite/01_Astroids.png"),
                              pygame.image.load("asset/laser_sprite/02_Astroids.png")]
        
        for i in range(len(self.laser_sprites)):
            self.laser_sprites[i] = pygame.transform.scale(self.laser_sprites[i], self.laser_size) 

        self.current_frames = 0
        self.total_frames = len(self.laser_sprites)
        self.frame_delay = 7
        self.frame_count = 0

        # laseR_Rect
        self.laser_rect = self.laser_sprites[self.current_frames].get_rect(topleft=(self.pos_x, self.pos_y))

        self.laser_mask = pygame.mask.from_surface(self.laser_sprites[self.current_frames])
        self.mask_img = self.laser_mask.to_surface()
    

    def move(self):        
        if self.pos_y < self.screen.get_height():
            self.pos_y += self.velocity_y
    
    def check_hit(self):
        if self.pos_y >= (self.screen.get_height()):
              return self.hit == True
        
    
    # def random_gen(self):
    #     if(self.hit):
    #         self.pos_x = random.randrange(0, 1300-60)
    #         self.pos_y = 0
    #         self.hit = False


    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.current_frames = (self.current_frames + 1) % self.total_frames
            self.frame_count = 0
           

    def create_laser(self):

        # self.laser_rect = self.laser_sprites[self.current_frames].get_rect(topleft=(self.pos_x, self.pos_y))
     
        self.screen.blit(self.laser_sprites[self.current_frames], (self.pos_x, self.pos_y))
        # self.screen.blit(self.mask_img, (self.pos_x, self.pos_y))
       



    
    
        
            

       
         
        



        































