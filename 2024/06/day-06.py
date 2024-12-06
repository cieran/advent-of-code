import copy 
import numpy as np

DIRECTIONS: dict = {
    'UP': (-1, 0),
    'RIGHT': (0, 1),
    'DOWN': (1, 0),
    'LEFT': (0, -1)
}

GUARD_DIRECTIONS: dict = {
    'UP': '^',
    'RIGHT': '>',
    'DOWN': 'v',
    'LEFT': '<'
}

NEXT_DIRECTION: dict = {
    'UP': 'RIGHT',
    'RIGHT': 'DOWN',
    'DOWN': 'LEFT',
    'LEFT': 'UP'
}

def main():
    with open('./input.txt') as f:
        data = f.read()
        lab = np.array([list(d) for d in data.splitlines()])

    distinct_positions = part_one(lab)
    print(f"part one: {len(distinct_positions)}")
    print(f"part two: {part_two(distinct_positions, lab)}")

def part_one(lab):
    current_position = find_start(lab)
    edges = get_edges(lab)

    distinct_positions = set()
    distinct_positions.add(current_position)
    
    direction = 'UP'
    while current_position not in edges:
        lab, new_position, new_direction = move(lab, current_position, direction)
        distinct_positions.add(new_position)
        current_position = new_position
        direction = new_direction

    return distinct_positions

def part_two(distinct_positions, lab):
    loops = 0
    start = find_start(lab)
    distinct_positions.discard(start)
    i = 1
    for p in distinct_positions:
        print(f"sim {i}/{len(distinct_positions)}, loops {loops}")
        updated_lab = update_lab(copy.deepcopy(lab), p, '#')
        can_escape = simulate(updated_lab, start)
        if not can_escape:
            loops += 1
        i += 1
    return loops

def simulate(lab, start):
    edges = get_edges(lab)
    direction = 'UP'
    escaped = False
    current_position = start
    visited = set((current_position, 'UP'))
    while not escaped:
        new_lab, new_position, new_direction = move_and_update(lab, current_position, direction)
        if (new_position, new_direction) in visited:
            break
        lab = new_lab
        current_position = new_position
        direction = new_direction
        if current_position in edges:
            escaped = True
        visited.add((current_position, direction))

    return escaped


def update_lab(lab, position, symbol):
    i, j = position
    if lab[i][j] == '.':
        lab[i][j] = symbol
    return lab

def move(lab, position, direction):
    i, j = position
    x, y = DIRECTIONS[direction]
    if lab[i + x][j + y] == '#':
        next_direction = NEXT_DIRECTION[direction]
        return lab, (i, j), next_direction
    else:
        return lab, (i + x, j + y), direction

def move_and_update(lab, position, direction):
    i, j = position
    x, y = DIRECTIONS[direction]
    lab[i][j] = GUARD_DIRECTIONS[direction]
    new_lab = copy.deepcopy(lab)

    if lab[i + x][j + y] == '#':
        next_direction = NEXT_DIRECTION[direction]
        return new_lab, (i, j), next_direction
    else:
        return new_lab, (i + x, j + y), direction

def find_start(lab):
    for i, row in enumerate(lab):
        for j, cell in enumerate(row):
            if cell == '^':
                return (i, j)
            
def find_symbol_in_direction(lab, position, direction):
    symbol = '#'
    i, j = position
    x, y = DIRECTIONS[direction]
    return lab[i + x][j + y]

def get_edges(lab):
    edges = []
    for i, row in enumerate(lab):
        for j, cell in enumerate(row):
            if cell == '.':
                if i == 0 or i == len(lab) - 1 or j == 0 or j == len(row) - 1:
                    edges.append((i, j))
    return edges

def get_coordinates_of_all_dots(lab):
    dots = []
    for i, row in enumerate(lab):
        for j, cell in enumerate(row):
            if cell == '.':
                dots.append((i, j))
    return dots

def print_lab(lab):
    print('\n')
    return print('\n'.join(''.join(row) for row in lab))

if __name__ == '__main__':
    main()