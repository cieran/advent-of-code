def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    ints = [int(i.strip()) for i in lines]

    print(part_one(ints))
    print(part_two(ints))


def part_one(ints):
    numbers = list()
    for idx, i in enumerate(ints[25:]):
        if not adds_up(i, idx, ints):
            numbers.append(i)
    return numbers


def part_two(ints):
    numbers = part_one(ints)
    for idx, i in enumerate(ints):
        sum = 0
        idx_plus_one = idx
        for j in ints[idx:]:
            sum += j
            idx_plus_one += 1
            if sum == numbers[0]:
                contiguous_range = ints[idx: idx_plus_one]
                return min(contiguous_range) + max(contiguous_range)


def adds_up(i, idx, ints):
    for int in ints[idx:idx + 25]:
        if (i - int) in ints[idx:idx + 25]:
            return True


main()
