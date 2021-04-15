import pygame
def beta_soundtrack():
    pygame.mixer.init()
    pygame.mixer.music.load("src/assets/sound/chiptunebetatheme.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

def stop_music():
    pygame.mixer.music.stop()
    pygame.mixer.quit()