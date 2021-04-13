import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.x = x
        self.y = y