import pygame

class Player:
    def __init__(self, color,  size, velocity_x,  pos_x, pos_y, health, arr, screen):
        self.color = color
        self.size = size
        self.velocity_x = velocity_x
        self.pos_x = pos_x
        self.pos_y = (pos_y-70)
        self.health = health
        self.walk_count = 0
        self.left = False
        self.right = False
        self.sprite_arr = arr
        self.screen = screen
        
    def create_player(self):
        # rectangle = pygame.Rect(self.pos_x, self.pos_y, self.size, self.size)
        # pygame.draw.rect(screen, self.color, rectangle)
        self.screen.blit(self.sprite_arr[2], (self.pos_x, self.pos_y))

    def move(self, KEY):
            if KEY == "RIGHT":
                self.pos_x += self.velocity_x
                self.right = True
                self.left = False
                        
            elif KEY == "LEFT":
                self.pos_x -= self.velocity_x
                self.left = True
                self.right = False
  
    def idle(self):
        
         if self.left == False and self.right == False:
            for i in range(len(self.sprite_arr)):
                self.screen.blit(self.sprite_arr[i], (self.pos_x, self.pos_y))
                # print(i)

                      
                 
                 
                 
            




        



        