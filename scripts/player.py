
import pygame

class Player:
    def __init__(self, color,  size, velocity_x, velocity_y):
        self.color = color
        self.size = size
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        
    def create_player(self, screen):
        rectangle = pygame.Rect(self.size, self.size, self.size, self.size)
        pygame.draw.rect(screen, self.color, rectangle)



        