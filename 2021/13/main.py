def part_one(dots, f):
    vh = int(f.split('=')[-1])
    print(vh)
    if 'x' in f:
        dots = set((x-(x-vh)*2, y) if x >= vh else (x, y) for x, y in dots)
    else:
        dots = set((x, y-(y-vh)*2) if y >= vh else (x, y) for x, y in dots)
    return len(ds)


def part_two(dots, fs):
    for f in fs.split('\n'):
        vh = int(f.split('=')[-1])
        if 'x' in f:
            dots = set((x-(x-vh)*2, y) if x >= vh else (x, y) for x, y in dots)
        else:
            dots = set((x, y-(y-vh)*2) if y >= vh else (x, y) for x, y in dots)
    for y in range(7):
        for x in range(40):
            print('X' if (x, y) in dots else ' ', end='')
        print()


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        ds, fs = f.read().split('\n\n')

    dots = set(tuple(int(c) for c in d.split(',')) for d in ds.split('\n'))

    print(part_one(dots, fs.split('\n')[0]))
    part_two(dots, fs)
