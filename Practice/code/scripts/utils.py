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
    def __init__(self, img, size):
        self.sheet = img
        self.size = size
        
    def get_image(self, column, row, color=(0, 0, 0)):
        surf = pygame.Surface(self.size)
        surf.blit(self.sheet, (0, 0), ((column * self.size[0]), (row * self.size[1]), self.size[0], self.size[1]))
        surf.set_colorkey(color)
        return surf
    
    def get_frames(self, row, frames):
        animation_frames = []
        for x in range(frames):
            animation_frames.append(self.get_image(x, row, (0, 0, 0)))
        return animation_frames
