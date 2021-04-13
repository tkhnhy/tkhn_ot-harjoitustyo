import pygame
import character, gamedisplay, sound, enemies
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
    for i in slimelist:
        i.slimedraw(screen)
    pygame.display.flip()


overworld1_spritesheet = Spritesheet('assets/temp/texturepack.png')
sheet_names = ['grass0000.png','sand0000.png']

def make_tile_map(file, tilesize, spritesheet):
    map = []
    xloc = 0
    yloc = 0
    for row in file:
        for i in row:
            if i == "0":
                map.append(Tile('grass0000.png', xloc, yloc, spritesheet, 1))
            elif i == "1":
                map.append(Tile('sand0000.png', xloc, yloc, spritesheet, 0))
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

player = character.Player(224, 0, tiles)
slime = enemies.Slime(540, 540)
slime2 = enemies.Slime(400, 780)
slimelist = [slime, slime2]

sound.beta_soundtrack()

while True:
    clock.tick(30)
    for action in pygame.event.get():
        player.player_movement(action)
        if action.type == pygame.QUIT:
            sound.stop_music()
            exit()
    drawscreen()