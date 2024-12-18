import pygame, sys

from scripts.utils import load_image, Spritesheet
from scripts.entities import Entity
from scripts.tilemap import Tilemap

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Practicing')
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.player_sheet = Spritesheet(load_image('player/playerSheet.png'), (16, 16))
        self.tile_sheet = Spritesheet(load_image('tiles/tiles.png'), (16, 16))

        self.assets = {
            'player': self.player_sheet.get_frames(0, 2),
            'brick': self.tile_sheet.get_image(0, 0, (0, 0, 0)),
            'wall': self.tile_sheet.get_image(1, 0, (0, 0, 0))
        }

        self.player = Entity(self, 'player', (0, 0), (12, 14))
        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, 16)

    def run(self):
        self.run = True
        while self.run:
            self.display.fill((0, 20, 50))

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]))
            self.player.render(self.display)

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False

            

            # Game rendering
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    Game().run()
            
