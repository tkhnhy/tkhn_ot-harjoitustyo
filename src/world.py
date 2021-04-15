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

def make_tile_map(file, tilesize, spritesheet, sheetitems):
    sheetitems = sheetitems
    map = []
    xloc = 0
    yloc = 0
    for row in file:
        for i in row:
            if i == "0":
                map.append(Tile(sheetitems[0][0], xloc, yloc, spritesheet, sheetitems[0][1]))
            elif i == "1":
                map.append(Tile(sheetitems[1][0], xloc, yloc, spritesheet, sheetitems[1][1]))
            else:
                pass
            xloc += tilesize
        xloc = 0
        yloc += tilesize
    return map