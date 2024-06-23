import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.size = (215, 100)
        self.start_btn_img = pygame.image.load("asset/menu/start.png").convert_alpha()
        self.start_btn_img = pygame.transform.scale(self.start_btn_img, self.size)
        self.end_btn_img = pygame.image.load("asset/menu/exit.png").convert_alpha()
        self.end_btn_img = pygame.transform.scale(self.end_btn_img, self.size)
        
       
        self.start_btn_rect = self.start_btn_img.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2 - 60))
        self.end_btn_rect = self.end_btn_img.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2 + 60))
        
       
        self.start_btn_mask = pygame.mask.from_surface(self.start_btn_img)
        self.end_btn_mask = pygame.mask.from_surface(self.end_btn_img)
        
    def menu_layout(self):
        self.screen.blit(self.start_btn_img, self.start_btn_rect.topleft)
        self.screen.blit(self.end_btn_img, self.end_btn_rect.topleft)
    
    # def check_collision(self, pos):
    #     x, y = pos
       
    #     start_btn_pos = (x - self.start_btn_rect.left, y - self.start_btn_rect.top)
    #     if self.start_btn_mask.get_at(start_btn_pos):
    #         print("Start button clicked")
        
       
    #     end_btn_pos = (x - self.end_btn_rect.left, y - self.end_btn_rect.top)
    #     if self.end_btn_mask.get_at(end_btn_pos):
    #         print("End button clicked")
           
      
    def set_cood(self):
           return 

            
        
    def menu_start_btn(self):
            return
        
    def menu_volume_btn(self):
            return
        
    def menu_credit_btnself(self):
            return
        

        
    