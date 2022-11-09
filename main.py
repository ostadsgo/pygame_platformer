import pygame as pg

from settings import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.running = True
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.run()
    
    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # update
        self.all_sprites.update()

    def events(self):
        # keep loop running at the right speed
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.running = False
                # close game while playing if user quit
                if self.playing:
                    self.playing = False

    
    def draw(self):
        # Draw / render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_splash_screen(self):
        pass

    def show_game_over_screen(self):
        pass


game = Game()
game.show_splash_screen()
while game.running:
    game.new()
    game.show_game_over_screen()

pg.quit()




