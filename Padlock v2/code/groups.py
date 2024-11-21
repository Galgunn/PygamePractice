from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pygame.display.get_surface()

    def draw(self, display):
        # Render sprites in sprite group onto display
        for sprite in self:
            display.blit(sprite.image, sprite.rect)
        
        display.fill('white')
        scaled_display = pygame.transform.scale(display, self.screen.get_size())
        self.screen.blit(scaled_display, (0, 0))