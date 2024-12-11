import pygame, os

BASE_IMG_PATH = 'Practice/assets/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

class Spritesheet():
    def __init__(self, spritesheet):
        self.sheet = spritesheet
        
    def get_images(self, frame, w, h, strip, color=(0, 0, 0)):
        img = pygame.Surface((w, h))
        img.blit(self.sheet, (0, 0), ((frame * w, ), (strip * h), w, h))
        img.set_colorkey(color)
        return img
    
    def get_frames(self, action_frames):
        self.animation_frames = []
        self.action_frames = action_frames
        strip_counter = 0
        for frames in self.action_frames:
            temp_list = []
            for x in range(frames):
                temp_list.append(self.get_images(x, 32, 32, strip_counter, (0, 0, 0)))
            strip_counter += 1
            self.animation_frames.append(temp_list)
        return self.animation_frames
