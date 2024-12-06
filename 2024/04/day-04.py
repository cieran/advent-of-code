DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
DIAGONALS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
SEQUENCE = ['X', 'M', 'A', 'S']

def main():
    with open('input.txt') as f:
        data = f.read()
        wordsearch = [list(d) for d in data.splitlines()]

    print(part_one(wordsearch))
    print(part_two(wordsearch))

def part_one(wordsearch):
    valid = 0
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == 'X':
                for direction in DIRECTIONS:
                    if find_sequence(i, j, wordsearch, direction):
                        valid += 1
    return valid

def part_two(wordsearch):
    valid = 0
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == 'A':
                if find_x(i, j, wordsearch):
                    valid += 1
    return valid

def find_x(x, y, wordsearch):
    top_left = wordsearch[x-1][y-1] if x > 0 and y > 0 else None
    top_right = wordsearch[x-1][y+1] if x > 0 and y < len(wordsearch[0]) - 1 else None
    bottom_left = wordsearch[x+1][y-1] if x < len(wordsearch) - 1 and y > 0 else None
    bottom_right = wordsearch[x+1][y+1] if x < len(wordsearch) - 1 and y < len(wordsearch[0]) - 1 else None

    if (top_left == 'M' and bottom_left == 'M') and (top_right == 'S' and bottom_right == 'S'):
        return True
    if (top_left == 'S' and bottom_left == 'S') and (top_right == 'M' and bottom_right == 'M'):
        return True
    if (top_left == 'S' and top_right == 'S') and (bottom_left == 'M' and bottom_right == 'M'):
        return True
    if (top_left == 'M' and top_right == 'M') and (bottom_left == 'S' and bottom_right == 'S'):
        return True
    return False


def find_sequence(x, y, wordsearch, direction):
    x_direction, y_direction = direction
    current_x, current_y = x, y
    for letter in SEQUENCE[1:]:
        current_x += x_direction
        current_y += y_direction
        if not (0 <= current_x < len(wordsearch) and 0 <= current_y < len(wordsearch[0])):
            return False
        if wordsearch[current_x][current_y] != letter:
            return False
    return True

if __name__ == '__main__':
    main()