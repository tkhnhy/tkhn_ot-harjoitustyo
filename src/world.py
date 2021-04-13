import pygame, csv
from spritesheet import Spritesheet

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet, type: int):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        #Types: 0: Background tile, 1: solid tile
    
    def draw_tile(self, output):
            output.blit(self.image, (self.rect.x, self.rect.y))

    def ret_type(self):
        return self.type

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

