import pygame
import gamedisplay

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, tile):
        super().__init__()

        self.sprite_standing = pygame.image.load("assets/sprites/playerstanding.png")
        self.sprite_standing = pygame.transform.scale(self.sprite_standing, (32, 32))

        self.speed = 2
        self.dx, self.dy = 0, 0

        self.rect = self.sprite_standing.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.tile = tile
    
    def movement_controls(self):
        self.dx, self.dy = 0, 0
        controls = pygame.key.get_pressed()
        if controls[pygame.K_d]:
            self.dx = self.speed
        if controls[pygame.K_a]:
            self.dx = -self.speed
        if controls[pygame.K_s]:
            self.dy = self.speed
        if controls[pygame.K_w]:
            self.dy = -self.speed

    def update(self, tilegroup):
        self.movement_controls()
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.check_collision(tilegroup):
            self.rect.x -= self.dx
            self.rect.y -= self.dy
    
    def check_collision(self, tiles):
        for i in tiles:
            if self.rect.colliderect(i) and i.ret_type() == 1:
                return True
        return False

    def playerdraw(self, output):
        output.blit(self.sprite_standing, (self.rect.x, self.rect.y))
            
        