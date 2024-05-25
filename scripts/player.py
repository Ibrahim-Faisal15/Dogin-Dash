
import pygame

class Player:
    def __init__(self, color,  size, velocity_x,  pos_x, pos_y):
        self.color = color
        self.size = size
        self.velocity_x = velocity_x
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def create_player(self, screen):
        rectangle = pygame.Rect(self.pos_x, self.pos_y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rectangle)




        



        