###
# 1 -> 2 wires
# 4 -> 4 wires
# 7 -> 3 wires
# 8 -> 7 wires
###
def part_one(data):
    count = 0
    for d in data:
        for t in d:
            if len(t) in [2, 4, 3, 7]:
                count += 1
    return count


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        lines = [line for line in f.readlines()]
        data = [line.split("|")[1].strip().split() for line in lines]

    print(part_one(data))
