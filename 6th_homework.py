import pygame
import time
import math
x = 2560
y = 1080
print(pygame.init())
logo = pygame.image.load('images.jpg')
pygame.display.set_icon(logo)
size = logo.get_rect().size
pygame.display.set_caption('Pokemon')
screen = pygame.display.set_mode((x, y))
running = True
x0 = x/2 - size[0]/2
y0 = y/2 - size[1]/2


class Circle:
    def __init__(self, q, a, b):
        self.q = q
        self.a = a
        self.b = b
        self.typ = 0

    def circle(self, r):
        if self.typ == 0:
            w = math.sqrt(r**2 - (self.q-self.a)**2) + self.b
            if self.q == x0+r:
                self.typ = 1
        else:
            w = self.b - math.sqrt(r**2 - (self.q-self.a)**2)
            if self.q == x0-r:
                self.typ = 0
        return w

    def circlerun(self):
        if self.typ == 0:
            self.q += 1
        else:
            self.q -= 1
        time.sleep(0.01)
        screen.fill((0, 0, 0))
        return self.circle(250)


shape = Circle(x0 - 100, x0, y0)
logo.set_colorkey((255, 255, 255))
logo.set_alpha(100)
text = pygame.font.SysFont('monospace', 65)
# point = text.render("Time:" + str(q), 1, (100, 100, 100))
# screen.blit(point, (1080, 720))
# screen.blit(logo, (q, shape.circle(q, x0, y0)))
# pygame.display.flip()
while running:
    screen.blit(logo, (shape.q, shape.circlerun()))
    pygame.display.update()
    print(shape.q, shape.circle(250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
