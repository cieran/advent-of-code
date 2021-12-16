from queue import PriorityQueue
from collections import defaultdict
import sys

START = (0,0)

DIRECTIONS = {
    'UP': [0,1],
    'DOWN': [0,-1],
    'LEFT': [-1,0],
    'RIGHT': [1,0]
}

def neighbours(size, i, j):
    return [[y, x] for a, b in DIRECTIONS.values()
     if not ((x := a + j) < 0  or 
             (y := b + i) < 0  or 
              x >= size[0] + 1 or
              y >= size[1] + 1 )]

def dijkstras(g):
    size = end = (len(g)-1, len(g[0])-1)
    d = defaultdict(lambda: sys.maxsize)
    d[START] = 0
    q = PriorityQueue()
    q.put((0, START))
    
    while not q.empty():
        _, (y1,x1) = q.get()
        if (y1,x1) == end:
            return d[end]
        
        for y2,x2 in neighbours(size, y1, x1):
            nd = d[(y1,x1)] + g[y2][x2]
            if nd < d[(y2,x2)]:
                d[(y2,x2)] = nd
                q.put((nd, (y2,x2)))

def part_one(g):
    return dijkstras(g)

def part_two(g):
    bg = [line[:] for line in g]

    for i in range(len(g)):
        for j in range(1, 5):
            bg[i] += [ v + j if (v + j) <= 9 else (v + j) % 9 for v in g[i] ]
    for i in range(1,5):
        for j in range(len(g)):
            bg.append([v + i if (v + i) <= 9 else (v + i) % 9 for v in bg[j]])

    return dijkstras(bg)


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        g = [list(map(int, r)) for r in f.read().splitlines()]

    print(part_one(g))
    print(part_two(g))