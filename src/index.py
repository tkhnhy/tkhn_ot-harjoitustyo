import pygame
import character, gamedisplay, sound, enemies
from world import Map, Tile, make_tile_map
from spritesheet import Spritesheet

pygame.init()

screen = pygame.display.set_mode((gamedisplay.display_width, gamedisplay.display_height))
clock = pygame.time.Clock()


def drawscreen():
    screen.fill((173, 173, 173))
    for tile in level:
        tile.draw_tile(screen)
    player.playerdraw(screen)
    for i in slimelist:
        i.draw(screen)
    pygame.display.flip()

#Screen 1
overworld1_spritesheet = Spritesheet('src/assets/temp/texturepack.png')
sheet_items = [('grass0000.png', 1),('sand0000.png', 0)]

level = Map("src/assets/temp/level1.csv")
level = level.create_map()
level = make_tile_map(level, 32, overworld1_spritesheet,sheet_items)

player = character.Player(224, 0)
slimelist = [enemies.BlueSlime(540, 540), enemies.BlueSlime(400, 780)]

#sound.beta_soundtrack()

while True:
    clock.tick(30)
    pygame.display.set_caption(f"{player.rect.x}, {player.rect.y} - {player.health}")
    player.update(level)
    player.check_collision_enemy(slimelist)
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            #sound.stop_music()
            exit()
    drawscreen()