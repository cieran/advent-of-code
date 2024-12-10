import numpy as np

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main():
    with open("input.txt") as f:
        data = f.read()
        map = np.array([[int(char) for char in list(d)] for d in data.split()])

    print(part_one(map))
    print(part_two(map))

def part_one(map):
    trailheads = get_trailheads(map)
    trailhead_scores = {}
    for trailhead in trailheads:
        score = find_trailhead_score(map, trailhead)
        trailhead_scores[trailhead] = score

    return f"part one: {sum(trailhead_scores.values())}"

def part_two(map):
    trailheads = get_trailheads(map)
    all_trails = []
    for trailhead in trailheads:
        trails = get_trails(trailhead, map)

        all_trails.extend(trails)

    distinct_trails = set(tuple(trail) for trail in all_trails)
    return f"part two: {len(distinct_trails)}"

def get_reachable_nines(trailhead, map):
    nines = set()
    traverse(trailhead, 1, map, nines)
    return nines

def get_trails(trailhead, map):
    trails = []
    traverse_trails(trailhead, 1, map, [], trails)
    return trails

def traverse(trailhead, i, map, nines):
    x, y = trailhead
    explore_paths((x, y), i, map, nines)

def traverse_trails(trailhead, i, map, current_trail, trails):
    x, y = trailhead
    explore_trails((x, y), i, map, current_trail, trails)

def explore_paths(position, i, map, nines):
    x, y = position
    for direction in DIRECTIONS:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]):
            if i == 9 and map[new_x][new_y] == 9:
                nines.add((new_x, new_y))
            elif map[new_x][new_y] == i:
                explore_paths((new_x, new_y), i + 1, map, nines)

def explore_trails(position, i, map, current_trail, trails):
    x, y = position
    current_trail.append((x, y))
    for direction in DIRECTIONS:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]):
            if i == 9 and map[new_x][new_y] == 9:
                trails.append(current_trail + [(new_x, new_y)])
            elif map[new_x][new_y] == i:
                explore_trails((new_x, new_y), i + 1, map, current_trail[:], trails)

def get_trailheads(map):
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def find_trailhead_score(map, trailhead):
    nines = get_reachable_nines(trailhead, map)
    return len(nines)

if __name__ == "__main__":
    main()