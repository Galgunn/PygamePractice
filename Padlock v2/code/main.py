from settings import *
from player import Player
from groups import AllSprites
from sprites import *

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display = pygame.Surface((WINDOW_WIDTH / 3, WINDOW_HEIGHT / 3))
        self.clock = pygame.time.Clock()

        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        # Create Sprites
        self.obj = CollisionSprite((100, 100), (50, 50), (self.all_sprites, self.collision_sprites))
        self.player = Player((10, 14), (50, 50), self.all_sprites, self.collision_sprites)

    def run(self) -> None:
        self.run = True
        while self.run:
            # Delta time
            dt = self.clock.tick(60) / 1000 # return in seconds

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Update
            self.all_sprites.update(dt)

            # Draw
            self.all_sprites.draw(self.display)
            pygame.display.flip()

if __name__ == '__main__':
    Game().run()