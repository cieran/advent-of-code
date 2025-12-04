adjacent = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def main(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    print(part_one(lines))
    print(part_two(lines))

def part_one(lines):
    count_rolls = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                if is_adjacent_less_than_four(lines, i, j):
                    count_rolls += 1 
    return count_rolls


def part_two(lines):
    total_count = 0
    current_lines = [list(row) for row in lines]
    while True:
        count, current_lines = sim(current_lines)
        if count == 0:
            break
        total_count += count

    return total_count

def sim(lines):
    count_rolls = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '@':
                if is_adjacent_less_than_four(lines, i, j):
                    count_rolls += 1 
                    lines[i][j] = 'x' 
    return count_rolls, lines

def is_adjacent_less_than_four(lines, i, j):
    count = 0
    for ai, aj in adjacent:
        ni, nj = i + ai, j + aj
        if in_bounds(lines, ni, nj) and lines[ni][nj] == '@':
            count += 1
    return count < 4

def in_bounds(lines, i, j):
    return 0 <= i < len(lines) and 0 <= j < len(lines[i])

if __name__ == '__main__':
    main('./test.txt')
    main('./input.txt')