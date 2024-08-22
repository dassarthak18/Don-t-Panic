import pygame as pg
import cProfile
import sys, time
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from sound import *

intro_images = [
    pg.transform.scale(pg.image.load("assets/titlecards/title.jpg"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/blackscreen.png"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/intro1.jpg"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/blackscreen.png"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/intro2.jpg"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/blackscreen.png"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/intro3.jpg"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/blackscreen.png"), (WIDTH, HEIGHT)),
    pg.transform.scale(pg.image.load("assets/titlecards/intro4.jpg"), (WIDTH, HEIGHT))
]

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        #self.screen = pg.display.set_mode(RES)
        self.screen = pg.display.set_mode(RES, pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.game_intro(intro_images)

    def game_intro(self, images):
        for i in range(len(images)):
            img = images[i]
            if i%2:
                duration = 1
            elif i in [2,4]:
                duration = 7.5
            else:
                duration = 2.5
            self.screen.blit(img, (0, 0))
            pg.display.update()
            start_time = time.time()
            while time.time() - start_time < duration:
                for event in pg.event.get():
                    if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                        pg.quit()
                        sys.exit()
                    if event.type == pg.KEYDOWN:  # Skip intro if any key is pressed
                        return

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        #self.static_sprite = SpriteObject(self)
        self.object_handler = ObjectHandler(self)
        self.sound = Sound(self)
        pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        #pg.display.set_caption(f'Don\'t Panic: {self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        cProfile.runctx('self.game_loop()', globals=globals(), locals=locals())

    def game_loop(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()