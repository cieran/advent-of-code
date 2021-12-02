

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    print(part_one(lines))


def part_one(lines):
    memory = {}
    for line in lines:
        parts = line.split()
        if parts[0] == 'mask':
            mask = parts[2]
            continue

        address = int(parts[0][4:-1])
        value_bin = format(int(parts[2]), "b").zfill(len(mask))
        value_bin = "".join(
            b if mask[i] == "X" else mask[i] for i, b in enumerate(value_bin)
        )

        memory[address] = int(value_bin, 2)

    return sum(memory.values())


def part_two(lines): return


main()