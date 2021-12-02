def main():
    with open('./data/input.txt') as f:
        lines = f.read().splitlines()

    ints = [int(x) for x in lines]

    print(part_one(ints))
    print(part_two(ints))


def part_one(ints):
    counter = 0
    for x, y in zip(ints, ints[1:]):
        if y > x:
            counter += 1
    return counter


def part_two(ints):
    counter = 0
    previous = 0
    for x, y, z in zip(ints, ints[1:], ints[2:]):
        total = x + y + z
        if (previous != 0) & (total > previous):
            counter += 1
        previous = total

    return counter


if __name__ == "__main__":
    main()
