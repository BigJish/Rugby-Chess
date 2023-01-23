from imports import *
from pitch import *

class Main:
    def __init__(self):
        init()
        self.clock = time.Clock()
        self.win = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen = 1
        self.pitch = Pitch()
        self.end = False
    
    def run(self):
        while self.end == False:
            for i in event.get():
                if i.type == QUIT:
                    self.end = True
                    
            if self.screen == 1:
                self.pitch.run()
            
            self.clock.tick(FPS)
            display.flip()
        quit()

main = Main()
main.run()
