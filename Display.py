import pygame
import Person
import Track

class Display:
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.tracks = []
        self.me = None

    def setup(self, total=3):
        self.me = Person.Person()
        for i in range(total):
            self.tracks.append(Track.Track((self.size[0]/total*i, 0), (self.size[0]/total, self.size[1])))  #TODO check int or float
            if i == 1:
                self.tracks[i].set_color((155, 155, 155))
                self.tracks[i].update_track()

    def draw(self):
        def pos(num):
            return self.me.get_re_pos()[num]\
                   *self.tracks[self.me.get_track_num()].get_size()[num]-(self.me.get_view_size(num))/2

        pygame.draw.rect(self.tracks[self.me.get_track_num()].get_track(),
                         self.me.color, pygame.Rect((pos(0), 640), self.me.get_view_size()))

        for track in self.tracks:
            self.screen.blit(track.get_track(), track.get_pos())



if __name__ == '__main__':
    pygame.init()
    display = Display((540, 800))
    display.setup()
    display.draw()
    running = True
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

