import pygame

class Player:
    def __init__(self, color,  size, velocity_x,  pos_x, pos_y, health, arr, screen, arr1, arr2):
        self.color = color
        self.size = size
        self.velocity_x = velocity_x
        self.pos_x = pos_x
        self.pos_y = (pos_y-70)
        self.health = health
        self.walk_count = 0
        self.left = False
        self.right = False
        self.idle_arr = arr
        self.screen = screen
        self.walkRight_Arr = arr1
        self.walkLeft_Arr = arr2
        
    def create_player(self):
          for i in range(len(self.idle_arr)):
                self.screen.blit(self.idle_arr[i], (self.pos_x, self.pos_y))

    def move(self, KEY):
            
            if self.walk_count + 1 >= 4:
                self.walk_count = 0

            if KEY == "RIGHT":
                self.pos_x += self.velocity_x
                self.right = True
                self.left = False
                self.walk_count += 1
                self.screen.blit(self.walkRight_Arr[self.walk_count], (self.pos_x, self.pos_y))
                print(self.walk_count)
                
                        
            elif KEY == "LEFT":
                self.pos_x -= self.velocity_x
                self.left = True
                self.right = False
                self.walk_count += 1
                self.screen.blit(self.walkLeft_Arr[self.walk_count], (self.pos_x, self.pos_y))


            else:
                self.left = False
                self.right = False
                self.walk_count = 0
  
    def idle(self):        
         if self.left == False and self.right == False:
          
                print("")



                      
                 
                 
                 
            




        



        