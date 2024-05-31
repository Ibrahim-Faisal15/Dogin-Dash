import pygame
import random

class Laser:
    def __init__(self, screen):
        self.color = (255, 0, 0)
        self.height = random.randrange(50,90)
        self.width = random.randrange(30,60)
        self.velocity_y = 3
        self.pos_x = random.randrange(0, 1300-60)+100
        self.pos_y = 0
        self.attack = 50
        self.screen = screen
        self.hit = False
      
    def create_laser(self):
        rectangle = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rectangle)
   

    def move(self):        
        if self.pos_y < self.screen.get_height():
            self.pos_y += self.velocity_y
    
    def check_hit(self):
        if self.pos_y >= (self.screen.get_height()):
              return self.hit == True
        
    
    def random_gen(self):
        if(self.hit):
            self.pos_x = random.randrange(0, 1300-60)
            self.pos_y = 0
            self.hit = False




    
    
        
            

       
         
        



        































# class Lasers:
#         def __init__(self, colour, vel, height, width, attack, pos_x, pos_y):
#             self.colour = colour    
#             self.vel = vel           
#             self.height = height
#             self.width = width      
#             self.attack = attack   
#             self.pos_x = pos_x   
#             self.pos_y = pos_y  

#         def randomPosGen(self):
#                 self.pos_x = random.randrange(0, self.pos_x)
    
            
            
#         def randomSize(self):
#                 self.height = random.randrange((self.height-20), (self.height+20))
#                 self.width = random.randrange((self.width-20), (self.width+20))

#                 return [self.width, self.height]

            
#         def attacking(self):
#                 return 
            
            
#         def Yaxis_dec(self):
#                 self.pos_y +- 1 
            
            
#         def randomSpawn(self, screen):
#                 width, height = self.randomSize()  
#                 self.randomPosGen()  
#                 rectangle = pygame.Rect(self.pos_x, self.pos_y, width, height)  
#                 pygame.draw.rect(screen, self.colour, rectangle)  

            
            

        
        