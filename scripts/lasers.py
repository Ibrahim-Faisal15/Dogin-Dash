import pygame
import random


          



class Laser:
    def __init__(self, color, height, width, velocity_y, pos_x, pos_y, attack, screen):
        self.color = color
        self.height = height
        self.width = width
        self.velocity_y = velocity_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.attack = attack
        self.screen = screen
        self.hit = False

        
    def create_laser(self):
        rectangle = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rectangle)
   

    def move(self):        
        if self.pos_y < 300:
            self.pos_y += self.velocity_y
    
    def check_hit(self):
        if self.pos_y > 300:
            self.hit = True
            # self.pos_y = 0
            

       
         
        



        































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

            
            

        
        