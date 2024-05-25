import pygame


# Screen dimensions
WIDTH = 1300
HEIGHT = WIDTH / 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 40

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Main function
def main():
    from player import Player  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        
        # Create a Player object
        player = Player(GREEN, 20, 0, 0, 0)
        player.create_player(screen)
        pygame.display.flip()
        
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
