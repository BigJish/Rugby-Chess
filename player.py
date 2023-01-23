from imports import *

class Player(sprite.Sprite):
    def __init__(self, groups, pos, image):
        self.win = display.get_surface()
        super().__init__(groups)
        self.image = image
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
        self.points = []
        self.point = 0
        self.moving = False
        self.selected = False
        self.x_move = False
        self.y_move = False
        self.location = False
        self.plathig = False
        self.speed = 1

    def select(self):
        p = mouse.get_pos()
        m = mouse.get_pressed()
        if self.moving  == False and self.selected == False and self.rect.collidepoint(p) and m[0]:
            self.selected = True
            self.pathing = True
    
    def path(self):
        p = mouse.get_pos()
        m = mouse.get_pressed()
        if self.selected and self.pathing and m[0]:
            if p[0] >= 150 and p[0] <= 1050 and p[1] >= 100 and p[1] <= 600:
                self.points.append(p)
        else:
            self.pathing = False

    def start(self):
        k = key.get_pressed()
        if self.selected and self.pathing == False and k[K_SPACE]:
            self.point = 0
            self.moving  = True
            self.selected  = False
            self.x_move = True
            self.y_move = True
    
    def move(self):
        if self.moving and len(self.points) > self.point:
            if self.rect.center[0]-1 > round(self.points[self.point][0],0):
                self.rect.x -= self.speed

            elif self.rect.center[0]+1 < round(self.points[self.point][0],0):
                self.rect.x += self.speed
                
            else:
                self.x_move = False
                
            if self.rect.center[1]-1 > round(self.points[self.point][1],0):
                self.rect.y -= self.speed
                
            elif self.rect.center[1]+1 < round(self.points[self.point][1],0):
                self.rect.y += self.speed
            
            else:
                self.y_move = False
            
            if self.x_move == False and self.y_move == False:
                self.point += 1
                self.x_move = True
                self.y_move = True

        elif len(self.points) == self.point:
            self.point = 0
            self.points = []
            self.moving = False

        else:
            self.moving = False
    
    def draw(self):
        self.win.blit(self.image, self.rect)

    def dot(self):
        if self.moving == False:
            for i in self.points:
                draw.ellipse(self.win, (220,220,30),(i[0]-10, i[1]-10, 20, 20))

    def update(self):
        self.select()
        self.path()
        self.start()
        self.move()
        self.draw()
        self.dot()