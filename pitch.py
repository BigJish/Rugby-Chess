from imports import *
from player import *

class Pitch:
    def __init__(self):
        self.win = display.get_surface()
        self.image = image.load("Pitch.png").convert_alpha()
        self.visible_sprites = sprite.Group()
        self.player1 = Player(self.visible_sprites, (440, 180),  image.load("No.1.png").convert_alpha())
        self.player2 = Player(self.visible_sprites, (440, 330),  image.load("No.2.png").convert_alpha())
        self.player3 = Player(self.visible_sprites, (440, 480),  image.load("No.3.png").convert_alpha())
        self.player4 = Player(self.visible_sprites, (360, 250),  image.load("No.4.png").convert_alpha())
        self.player5 = Player(self.visible_sprites, (360, 410),  image.load("No.5.png").convert_alpha())
        self.player6 = Player(self.visible_sprites, (280, 120),  image.load("No.6.png").convert_alpha())
        self.player7 = Player(self.visible_sprites, (280, 540),  image.load("No.7.png").convert_alpha())
        self.player8 = Player(self.visible_sprites, (290, 330),  image.load("No.8.png").convert_alpha())
        self.player9 = Player(self.visible_sprites, (320, 190),  image.load("No.9.png").convert_alpha())
        self.player10 = Player(self.visible_sprites, (320, 470),  image.load("No.10.png").convert_alpha())
        self.player11 = Player(self.visible_sprites, (200, 160),  image.load("No.11.png").convert_alpha())
        self.player12 = Player(self.visible_sprites, (260, 230),  image.load("No.12.png").convert_alpha())
        self.player13 = Player(self.visible_sprites, (260, 440),  image.load("No.13.png").convert_alpha())
        self.player14 = Player(self.visible_sprites, (200, 500),  image.load("No.14.png").convert_alpha())
        self.player15 = Player(self.visible_sprites, (160, 330),  image.load("No.15.png").convert_alpha())

    def run(self):
        self.draw()
        for i in self.visible_sprites:
            i.update()
    
    def draw(self):
        self.win.blit(self.image, (0,0))