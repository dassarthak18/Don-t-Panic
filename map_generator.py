from random import choice, seed, randint
from datetime import datetime

def replace_random(lst, num):
  while True:
    seed(datetime.now().timestamp())
    i = randint(0, len(lst) - 1)
    j = randint(0, len(lst[0]) - 1)
    if lst[i][j] == 1:
        lst[i][j] = num
        return lst

def visit(x, y, maze, hasVisited, HEIGHT, WIDTH):
    maze[(x, y)] = 0
    while True:
        unvisitedNeighbors = []
        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append('n')
        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append('s')
        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append('w')
        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append('e')
        if len(unvisitedNeighbors) == 0:
            return
        else:
            nextIntersection = choice(unvisitedNeighbors)
            if nextIntersection == 'n':
                nextX = x
                nextY = y - 2
                maze[(x, y - 1)] = 0
            elif nextIntersection == 's':
                nextX = x
                nextY = y + 2
                maze[(x, y + 1)] = 0
            elif nextIntersection == 'w':
                nextX = x - 2
                nextY = y
                maze[(x - 1, y)] = 0
            elif nextIntersection == 'e':
                nextX = x + 2
                nextY = y
                maze[(x + 1, y)] = 0
            hasVisited.append((nextX, nextY))
            visit(nextX, nextY, maze, hasVisited, HEIGHT, WIDTH)

def generate_maze(WIDTH, HEIGHT): # HEIGHT, WIDTH should be odd and > 3 to ensure bounded maze
  seed(datetime.now().timestamp())
  maze = {}
  for x in range(WIDTH):
      for y in range(HEIGHT):
          maze[(x, y)] = 1
  hasVisited = [(1, 1)]
  visit(1, 1, maze, hasVisited, HEIGHT, WIDTH)
  map = []
  for y in range(HEIGHT):
      row = []
      for x in range(WIDTH):
          row.append(maze[(x, y)])
      map.append(row)
  return map
