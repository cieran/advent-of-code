def part_one(data):
    list_of_burn = []
    for i in range(min(data), max(data)):
        burn = 0
        for h in data:
            diff = abs(i - h)
            burn += diff
        list_of_burn.append(burn)
    return min(list_of_burn)


def part_two(data):
    list_of_burn = []
    for i in range(min(data), max(data)):
        burn = 0
        for h in data:
            diff = abs(i - h)
            for cost_of_move in range(1, diff + 1):
                burn += cost_of_move
        list_of_burn.append(burn)
    return min(list_of_burn)


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        data = f.read().strip().split(',')
        data = map(int, data)
        data = list(data)
        data.sort()

        print(part_one(data))
        print(part_two(data))
