import pygame as pg
from map_generator import generate_maze

_ = False
mini_map = generate_maze(15,9)

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'white', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]