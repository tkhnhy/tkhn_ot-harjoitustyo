import pygame

class Slime(pygame.sprite.Sprite):
    def __init__(self, x, y):
        
        self.sprite = pygame.image.load("assets/temp/blueslime0000.png")
        self.sprite = pygame.transform.scale(self.sprite, (48, 32))

        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y

    def slime_movement_horizonal(self, counter):
        pass

    def slimedraw(self, output):
        output.blit(self.sprite, (self.rect.x, self.rect.y))
