from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.display = pygame.Surface((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def draw(self):
        for sprite in self:
            self.display.blit(sprite.image, sprite.rect)
        scaled_display = pygame.transform.scale(self.display, self.screen.get_size())
        self.display.fill('white')
        self.screen.blit(scaled_display, (0, 0))