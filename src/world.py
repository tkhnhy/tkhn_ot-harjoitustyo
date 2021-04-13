import pygame, csv
from spritesheet import Spritesheet

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.x = x
        self.y = y
    
    def draw_tile(self, output):
        output.blit(self.image, (self.x, self.y))

class Map:
    def __init__(self, filename):
        self.filename = filename

    def create_map(self):
        level = []
        with open(self.filename, newline='') as csvfile:
            level_generate = csv.reader(csvfile)
            for row in level_generate:
                level.append(row)
            return level

