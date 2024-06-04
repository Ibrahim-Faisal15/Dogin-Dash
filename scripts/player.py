import pygame

class Player:
    def __init__(self, color,  size, velocity_x,  pos_x, pos_y, health, screen):
        self.color = color
        self.size = size
        self.velocity_x = velocity_x
        self.pos_x = pos_x
        self.pos_y = (pos_y-70)
        self.health = health
        self.walk_count = 0
        self.left = False
        self.right = False
        self.screen = screen
        self.player_size = (120, 120)
      

        # player sprites
        self.player_idle = [pygame.image.load('asset/player_sprite/idle/00_idle.png'),
                             pygame.image.load('asset/player_sprite/idle/01_idle.png'),
                             pygame.image.load('asset/player_sprite/idle/02_idle.png'),
                               pygame.image.load('asset/player_sprite/idle/03_idle.png')]
        
        self.walkRight = [pygame.image.load('asset/player_sprite/Walk/00_Walk.png'),
                           pygame.image.load('asset/player_sprite/Walk/01_Walk.png'),
                             pygame.image.load('asset/player_sprite/Walk/02_Walk.png'),
                               pygame.image.load('asset/player_sprite/Walk/03_Walk.png')]
        
        self.walkLeft = [pygame.image.load('asset/player_sprite/Walk/00_Walk.png'),
                          pygame.image.load('asset/player_sprite/Walk/01_Walk.png'), 
                          pygame.image.load('asset/player_sprite/Walk/02_Walk.png'),
                            pygame.image.load('asset/player_sprite/Walk/03_Walk.png')]


        self.current_frames = 0
        self.total_frames = len(self.player_idle)
        self.frame_delay = 7
        self.frame_count = 0




        for i in range(len(self.player_idle)):
          self.player_idle[i] = pygame.transform.scale(self.player_idle[i], self.player_size)

        for i in range(len(self.walkRight)):
          self.walkRight[i] = pygame.transform.scale(self.walkRight[i], self.player_size) 

        for i in range(len(self.walkLeft)):
          self.walkLeft[i] = pygame.transform.scale(self.walkLeft[i], self.player_size)   

        for i in range(len(self.walkLeft)):
         self.walkLeft[i] = pygame.transform.flip(self.walkLeft[i], True, False)
      

    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.current_frames = (self.current_frames + 1) % self.total_frames
            self.frame_count = 0

    def move(self, KEY):
            
            if self.walk_count + 1 >= 4:
                self.walk_count = 0

            if KEY == "RIGHT":
                self.pos_x += self.velocity_x
                self.right = True
                self.left = False

                self.screen.blit(self.walkRight[self.current_frames], (self.pos_x, self.pos_y))
                        
            elif KEY == "LEFT":
                self.pos_x -= self.velocity_x
                self.left = True
                self.right = False
                self.screen.blit(self.walkLeft[self.current_frames], (self.pos_x, self.pos_y))


            else:
                self.left = False
                self.right = False
                self.walk_count = 0

 
    def idle(self):        
        self.screen.blit(self.player_idle[self.current_frames], (self.pos_x, self.pos_y))
          
          


                      
                 
                 
                 
            




        



        