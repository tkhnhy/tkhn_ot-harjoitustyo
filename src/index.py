import pygame
import character, gamedisplay, sound
from world import Map, Tile
from spritesheet import Spritesheet

pygame.init()

screen = pygame.display.set_mode((gamedisplay.display_width, gamedisplay.display_height))
clock = pygame.time.Clock()


def drawscreen():
    screen.fill((173, 173, 173))
    for i in tiles:
        i.draw_tile(screen)
    player.playerdraw(screen)
    pygame.display.flip()
player = character.Player(0, 0)
overworld1_spritesheet = Spritesheet('assets/temp/texturepack.png')
def make_tile_map(file, tilesize, spritesheet):
    map = []
    xloc = 0
    yloc = 0
    for row in file:
        for i in row:
            if i == "0":
                map.append(Tile('grass0000.png', xloc, yloc, spritesheet))
            elif i == "1":
                map.append(Tile('sand0000.png', xloc, yloc, spritesheet))
            else:
                pass
            xloc += tilesize
        xloc = 0
        yloc += tilesize
    return map

#Screen 1
level = Map("assets/temp/level1.csv")
level = level.create_map()
tiles = make_tile_map(level, 32, overworld1_spritesheet)

def player_movement():
    if action.type == pygame.KEYDOWN:
        if action.key == pygame.K_LEFT:
            player.left = True
        if action.key == pygame.K_RIGHT:
            player.right = True
        if action.key == pygame.K_DOWN:
            player.down = True
        if action.key == pygame.K_UP:
            player.up = True        
    if action.type == pygame.KEYUP:
        if action.key == pygame.K_LEFT:
            player.left = False
        if action.key == pygame.K_RIGHT:
            player.right = False
        if action.key == pygame.K_DOWN:
            player.down = False
        if action.key == pygame.K_UP:
            player.up = False
sound.beta_soundtrack()

while True:
    clock.tick(30)
    for action in pygame.event.get():
        player_movement()
        if action.type == pygame.QUIT:
            sound.stop_music()
            exit()
    drawscreen()