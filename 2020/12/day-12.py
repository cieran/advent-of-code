def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()
    instructions = []
    for line in lines:
        instructions.append((line[0], int(line[1:])))

    print(part_one(instructions))
    print(part_two(instructions))


def part_one(instructions):
    h = 'E'
    hs = ['N', 'E', 'S', 'W']
    dx = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
    dy = {'N': 1, 'S': -1, 'W': 0, 'E': 0}
    x, y = 0, 0

    for m, v in instructions:
        if m == 'N':
            y += 1 * v
        elif m == 'S':
            y -= 1 * v
        elif m == 'E':
            x += 1 * v
        elif m == 'W':
            x -= 1 * v
        elif m == 'F':
            x += dx[h] * v
            y += dy[h] * v
        elif m == 'L':
            dir = hs.index(h)
            for _ in range(v // 90):
                dir = (dir + 3) % 4
            h = hs[dir]
        elif m == 'R':
            dir = hs.index(h)
            for _ in range(v // 90):
                dir = (dir + 1) % 4
            h = hs[dir]

    return abs(x) + abs(y)


def part_two(instructions):
    wp_x, wp_y = 10, 1
    x, y = 0, 0

    for m, v in instructions:
        if m == 'N':
            wp_y += 1 * v
        elif m == 'S':
            wp_y -= 1 * v
        elif m == 'E':
            wp_x += 1 * v
        elif m == 'W':
            wp_x -= 1 * v
        elif m == 'F':
            x += wp_x * v
            y += wp_y * v
        elif m == 'L':
            for _ in range(v // 90):
                wp_x, wp_y = -wp_y, wp_x
        elif m == 'R':
            for _ in range(v // 90):
                wp_x, wp_y = wp_y, -wp_x

    return abs(x) + abs(y)


main()
