def main(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    part_one(lines)
    part_two(lines)
    

def part_one(lines):
    dial = 50
    count_zero = 0
    for line in lines:
        char, num = line[0], int(line[1:])
        if char == 'L':
            dial -= num
        elif char == 'R':
            dial += num
        # the dial wraps around from 0 to 99
        dial %= 100
        if dial == 0:
            count_zero += 1
    print('part one:\t', count_zero)


def part_two(lines):
    dial = 50
    count_zero = 0
    for line in lines:
        char, num = line[0], int(line[1:])
        if char == 'L':
            for _ in range(num):
                dial -= 1
                if dial < 0:
                    dial = 99
                if dial == 0:
                    count_zero += 1
        elif char == 'R':
            for _ in range(num):
                dial += 1
                if dial > 99:
                    dial = 0
                if dial == 0:
                    count_zero += 1
    print('part two:\t', count_zero)


if __name__ == '__main__':
    main('./test.txt')
    main('./input.txt')
