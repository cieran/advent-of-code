def main():
    with open('./numbers.txt') as f:
        lines = f.read().splitlines()

    ints = [int(x) for x in lines]

    part_one(ints)
    part_two(ints)


def part_one(ints):
    print('part one')
    for x in ints:
        for y in ints:
            if x + y == 2020:
                print(x, y)
                print(x * y)
                return


def part_two(ints):
    print('part two')
    for x in ints:
        for y in ints:
            for z in ints:
                if x + y + z == 2020:
                    print(x, y, z)
                    print(x * y * z)
                    return


main()
