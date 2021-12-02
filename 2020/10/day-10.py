from collections import Counter


def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    unit_tests()
    print(part_one(lines))
    print(part_two(lines))


def part_one(lines):
    ints = sorted([int(i) for i in lines])

    ints.append(ints[-1] + 3)
    ints.insert(0, 0)
    d = [ints[i + 1] - ints[i] for i in range(len(ints) - 1)]

    c = Counter(d)
    return c[1] * c[3]


def part_two(lines):
    ints = sorted([int(i) for i in lines])

    ints.append(ints[-1] + 3)
    ints.insert(0, 0)
    d = [ints[i + 1] - ints[i] for i in range(len(ints) - 1)]

    streak = []
    length = 0
    for i in d:
        if i == 1:
            length += 1
        else:
            if length > 1:
                streak.append(length)
            length = 0

    combinations = {2: 2, 3: 4, 4: 7, 5: 13}

    p = 1
    for i in streak:
        p *= combinations[i]

    return p


def unit_tests():
    with open('./test-input.txt') as f:
        lines = f.read().splitlines()

    print(part_one(lines))
    assert part_one(lines) == 220


main()
