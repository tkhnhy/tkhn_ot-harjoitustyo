import pygame
import gamedisplay

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.sprite_standing = pygame.image.load("assets/sprites/playerstanding.png")
        self.sprite_standing = pygame.transform.scale(self.sprite_standing, (32, 32))
        self.x = x
        self.y = y

        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.xmomentum = 2
        self.ymomentum = 2

        self.rect = self.sprite_standing.get_rect()
        self.rect.x = x
        self.rect.y = y

    def movement(self):
        if self.right:
            if self.x + self.sprite_standing.get_width() >= gamedisplay.display_width:
                pass
            else:
                self.x += self.xmomentum
        if self.left:
            if self.x <= 0:
                pass
            else:
                self.x += -self.xmomentum
        if self.down:
            if self.y + self.sprite_standing.get_height() >= gamedisplay.display_height:
                pass
            else:
                self.y += self.ymomentum
        if self.up:
            if self.y <= 0:
                pass
            else:
                self.y += -(self.ymomentum)

    def playerdraw(self, output):
        self.movement()
        output.blit(self.sprite_standing, (self.x, self.y))
        #pygame.display.update()