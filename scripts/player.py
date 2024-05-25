from main import screen 

import pygame

class Player:
    def __init__(self, color, speed, size, velocity_x, velocity_y):
        self.color = color
        self.size = size
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        
        def create_player():
            rectangle = pygame.rect(size, size, size, size)
            pygame.draw.rect(screen, color, rectangle)



        