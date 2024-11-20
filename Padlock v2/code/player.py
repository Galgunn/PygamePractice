from settings import *
from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, size, pos, groups) -> None:
        super().__init__(groups)
        self.spritesheet_img = pygame.image.load(join('assets', 'playerSheet.png'))
        self.spritesheet = Spritesheet(self.spritesheet_img)
        self.size = size

        # Movement
        self.direction = pygame.Vector2()
        self.speed = 100

        # Animation
        self.get_frames()
        self.actions = {
            'idle_down': 0,
            'idle_right': 1,
            'idle_left': 2,
            'idle_up': 3,
            'walk_down': 4,
            'walk_right': 5,
            'walk_left': 6,
            'walk_up': 7,
        }

        self.action = self.actions['idle_down'] # Refrences the list in animation list that has said action
        self.last_update = 0
        self.animation_cooldown = 300
        self.frame = 0 # References the Surf in the self.action list 

        # Image and Rect
        self.image = self.animation_list[self.action][self.frame]
        self.rect = self.animation_list[self.action][self.frame].get_frect(center = pos)

    def get_frames(self):
        # Main animation list
        self.animation_list = []

        # List of frames per each action
        self.animation_frames = [2, 2, 2, 2, 4, 4, 4, 4]

        # Strip of animation actions
        strip_counter = 0

        for frames in self.animation_frames:
            temp_list = []
            for x in range(frames):
                temp_list.append(self.spritesheet.get_image(x, self.size[0], self.size[1], strip_counter, (0, 0, 0)))
            strip_counter += 1
            self.animation_list.append(temp_list)

    def update_animation(self, dt):
        # Increment the timer by delta time
        self.last_update += dt * 1000  # Convert seconds to milliseconds

        # Compare accumulated time with the animation cooldown
        if self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update -= self.animation_cooldown  # Subtract cooldown from timer

            # Reset frame and start over again
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0

    def animate(self, dt):
        # Get direction of where player is moving and update the correct action
        if self.direction.x > 0:
            self.action = self.actions['walk_right']
        if self.direction.x < 0:
            self.action = self.actions['walk_left']
        if self.direction.y > 0:
            self.action = self.actions['walk_down']
        if self.direction.y < 0:
            self.action = self.actions['walk_up']

        # Get last action 
        if not self.direction:
            last_action = self.action
            if last_action == self.actions['walk_down']:
                self.action = self.actions['idle_down']
                self.frame = 0
            if last_action == self.actions['walk_up']:
                self.action = self.actions['idle_up']
                self.frame = 0
            if last_action == self.actions['walk_right']:
                self.action = self.actions['idle_right']
                self.frame = 0
            if last_action == self.actions['walk_left']:
                self.action = self.actions['idle_left']
                self.frame = 0

        # Update the image 
        self.update_animation(dt)
        self.image = self.animation_list[self.action][self.frame]

    def input(self):
        # Get recent pressed keys
        keys = pygame.key.get_pressed()

        # Adjust player pos
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        
        if self.direction:
            self.direction = self.direction.normalize()
        else:
            self.direction
        

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)