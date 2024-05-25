import pygame
import random


          



class Laser:
    def __init__(self, color,  size, velocity_x,  pos_x, pos_y, attack):
        self.color = color
        self.size = size
        self.velocity_x = velocity_x
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = attack
        
    def create_laser(self, screen):
        rectangle = pygame.Rect(self.pos_x, self.pos_y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rectangle)




        































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

            
            

        
        