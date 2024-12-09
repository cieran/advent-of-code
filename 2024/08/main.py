import numpy as np
import copy
import itertools
from collections import Counter

def main():
    with open('./input.txt') as f:
        data = f.read()
        map = np.array([list(d) for d in data.splitlines()])

    map_copy = copy.deepcopy(map)
    print(part_one(map))
    print(part_two(map_copy))

def part_one(map):
    antennae = find_antennae(map)
    unique_coords = set()
    for key in antennae.keys():
        values = antennae[key]
        perms = [(a, b) for idx, a in enumerate(values) for b in values[idx + 1:]]
        new_antinodes = set()
        for c1, c2 in perms:
            x1, y1 = c1
            x2, y2 = c2
            x = x2 - x1
            y = y2 - y1

            x0 = x1 - x
            y0 = y1 - y
            x3 = x2 + x
            y3 = y2 + y

            c0 = (x0, y0)
            c3 = (x3, y3)
            if in_map(c0, map) and (c0 not in new_antinodes):
                map[x0][y0] = '#' if map[x0][y0] not in antennae else map[x0][y0]
                unique_coords.add(c0)
                new_antinodes.add(c0)
            if in_map(c3, map) and (c3 not in new_antinodes):
                map[x3][y3] = '#' if map[x3][y3] not in antennae else map[x3][y3]
                unique_coords.add(c3)
                new_antinodes.add(c3)
    return len(unique_coords)

def part_two(map):
    antennae = find_antennae(map)
    valid = set()
    for key in antennae.keys():
        values = antennae[key]
        perms = [(a, b) for idx, a in enumerate(values) for b in values[idx + 1:]]
        for c1, c2 in perms:
            valid.update(get_valid_coords_in_line(c1, c2, map))
            for v in valid:
                if in_map(v, map):
                    map[v[0]][v[1]] = '#' if map[v[0]][v[1]] not in antennae else map[v[0]][v[1]]
    total = Counter(i for i in list(itertools.chain.from_iterable(map)))
    return abs((len(map)*len(map[0]))- total['.'])

def get_valid_coords_in_line(c1, c2, map):
    valid_coords_above = []
    valid_coords_below = []
    
    x1, y1 = c1
    x2, y2 = c2
    x = x2 - x1
    y = y2 - y1

    valid_coords_below += get_coords((x,y), c1, 'sub', map)
    valid_coords_above += get_coords((x,y), c2, 'add', map)

    return valid_coords_above + valid_coords_below

def get_coords(diff, c, op, map, valid=None):
    if valid is None:
        valid = []
    
    if not in_map(c, map):
        return valid

    x, y = c
    i, j = diff

    match op:
        case 'add':
            next_c = (x + i, y + j)
        case 'sub':
            next_c = (x - i, y - j)
        case _:
            print('somethings wrong')
    
    if in_map(next_c, map):
        valid.append(next_c)
        return get_coords(diff, next_c, op, map, valid)
    
    return valid

def find_antennae(map):
    antennae = {}
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell != '.':
                coords = (i,j)
                symbol = str(map[i][j])
                if symbol not in antennae:
                    antennae[symbol] = []
                antennae[symbol].append(coords)
    return antennae

def in_map(coord, map):
    x, y = coord
    rows = len(map)        
    cols = len(map[0])
    return not (x < 0 or x >= rows or y < 0 or y >= cols)

def print_map(map):
    print('\n')
    return print('\n'.join(''.join(row) for row in map))


main()
