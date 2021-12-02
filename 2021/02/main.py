def main():
    with open('./data/input.txt') as f:
        ls = f.read().splitlines()

    d = 0
    h = 0
    a = 0
    print(part_one(ls, d, h))
    print(part_two(ls, d, h, a))


def part_one(ls, d, h):
    for l in ls:
        command = l.split()
        if command[0] == 'up':
            d -= int(command[1])
        if command[0] == 'down':
            d += int(command[1])
        if command[0] == 'forward':
            h += int(command[1])

    return d * h


def part_two(ls, d, h, a):
    for l in ls:
        command = l.split()
        if command[0] == 'up':
            a -= int(command[1])
        if command[0] == 'down':
            a += int(command[1])
        if command[0] == 'forward':
            h += int(command[1])
            d += a * int(command[1])

    return d * h


if __name__ == "__main__":
    main()
