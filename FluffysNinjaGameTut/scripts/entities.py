import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    '''
    Dynamicly create a rect to not update it each time

    Returns: 
        A rect
    '''
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        # Handle x movement and collision
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        # Check to see if there are any rects in list
        for rect in tilemap.physics_rects_around(self.pos):
            # Check for collision
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0: # collision e_rect moving right
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0: # collision e_rect moving left
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x # update players pos after collision

        # Handle y movement and collision
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        # Check to see if there are any rects in list
        for rect in tilemap.physics_rects_around(self.pos):
            # Check for collision
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0: # collision e_rect moving down
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0: # collision e_rect moving up
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y # update players pos after collision

        # Gravity and thermal velocity
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        # Stop player if rect collides with down or up direction
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
        
    def render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets['player'], (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        