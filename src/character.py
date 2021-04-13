import pygame
import gamedisplay

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, tile):
        super().__init__()

        self.sprite_standing = pygame.image.load("assets/sprites/playerstanding.png")
        self.sprite_standing = pygame.transform.scale(self.sprite_standing, (32, 32))

        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.xmomentum = 2
        self.ymomentum = 2

        self.rect = self.sprite_standing.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.tile = tile
    def movement(self):
        if self.right:
            if self.rect.x + self.sprite_standing.get_width() >= gamedisplay.display_width:
                pass
            else:
                self.rect.x += self.xmomentum
        if self.left:
            if self.rect.x <= 0:
                pass
            else:
                self.rect.x += -self.xmomentum
        if self.down:
            if self.rect.y + self.sprite_standing.get_height() >= gamedisplay.display_height:
                pass
            else:
                self.rect.y += self.ymomentum
        if self.up:
            if self.rect.y <= 0:
                pass
            else:
                self.rect.y += -(self.ymomentum)
    
    def check_collision(self, tiles):
        for i in tiles:
            if self.rect.colliderect(i) and i.ret_solid() == 1:
                return True
        return False

    def playerdraw(self, output):
        self.movement()
        output.blit(self.sprite_standing, (self.rect.x, self.rect.y))
    
    def player_movement(self, action):
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_a:
                self.left = True
            if action.key == pygame.K_d:
                self.right = True
            if action.key == pygame.K_s:
                self.down = True
            if action.key == pygame.K_w:
                self.up = True        
        if action.type == pygame.KEYUP:
            if action.key == pygame.K_a:
                self.left = False
            if action.key == pygame.K_d:
                self.right = False
            if action.key == pygame.K_s:
                self.down = False
            if action.key == pygame.K_w:
                self.up = False