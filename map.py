import pygame as pg
from map_generator import generate_maze, replace_random
from settings import *

w = WIDTH*img_scale // 100
h = HEIGHT*img_scale // 100
if w % 2 == 0:
    w -= 1
if h % 2 == 0:
    h -= 1

_ = False
mini_map = generate_maze(w,h)
for _ in range(w*h // 50):
    mini_map = replace_random(mini_map, 2)

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_world_map_dict(self):
        return {tuple(key): value for key, value in self.world_map.items()}

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        modifier = 100
        [pg.draw.rect(self.game.screen, 'white', (pos[0] * modifier, pos[1] * modifier, modifier, modifier), 2)
         for pos in self.world_map]