import pygame, sys

from scripts.utils import load_image, load_images, Animation, Spritesheet
from scripts.entities import Entity, Player
from scripts.tilemap import Tilemap

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Practicing')
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.player_spritesheet = Spritesheet(load_image(''))

        self.assets = {
            'player': load_image('player/idle/right/0.png'),
            'brick': load_image('tiles/brick/0.png'),
            'wall': load_image('tiles/wall/0.png'),
            'player/idle/down': Animation(load_images('player/idle/down'), frame_dur=10),
            'player/idle/right': Animation(load_images('player/idle/right'), frame_dur=10),
            'player/idle/up': Animation(load_images('player/idle/up'), frame_dur=10),
            'player/walk/down': Animation(load_images('player/walk/down'), frame_dur=6),
            'player/walk/right': Animation(load_images('player/walk/right'), frame_dur=6),
            'player/walk/up': Animation(load_images('player/walk/up'), frame_dur=6),
        }

        self.player = Player(self, (0, 0), (5, 14))
        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, 16)

        self.scroll = [0, 0]

    def run(self):
        self.run = True
        while self.run:
            self.display.fill((0, 20, 50))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]))
            self.player.render(self.display, offset=render_scroll)

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
            
