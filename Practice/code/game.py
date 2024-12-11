import pygame, sys

from scripts.utils import load_image



WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Practicing')
        self.clock = pygame.time.Clock()

        self.player_img = load_image('player')
        print(self.player_img)

    def run(self):
        self.run = True
        while self.run:

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Game rendering
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    Game().run()
            
