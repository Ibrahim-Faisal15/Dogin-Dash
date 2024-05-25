import pygame
import random

class Lasers:
    def __init__(self, colour, vel, height, width, attack, pos_x, pos_y):
        self.colour = colour    
        self.vel = vel           
        self.height = height
        self.width = width      
        self.attack = attack   
        self.pos_x = pos_x   
        self.pos_y = pos_y  

        def randomSpawn(self):
            self.pos_x = random.randrange((0, self.pos_x))
 
        
        
        def randomSize(self):
            self.height = random.randrange((self.height-20), (self.height+20))
            self.width = random.randrange((self.width-20), (self.width+20))

            return [self.witdh, self.height]

        
        def attacking(self):
            return 
        
        
        def Yaxis_dec(self):
            self.pos_y +- 1 
        
          
        def randomSpawn(self):


            width, height = randomSize()
            rectangle = pygame.rect(randomSpawn, self.pos_y, width, height)

        
        