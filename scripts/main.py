import pygame

#Screen
WIDTH = 1300
HEIGHT = WIDTH/2
screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
FPS = 40;

#While Loop
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

      

    clock.tick(FPS)
    



pygame.quit()