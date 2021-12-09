def part_one(lines):
    w = len(lines[0])
    h = [[9] * (w + 2)]

    for l in lines:
        h.append([9] + l + [9])
    h.append([9] * (w + 2))

    lp = []
    for i in range(1, len(h) - 1):
        for j in range(1, len(h[0]) - 1):
            if h[i][j - 1] > h[i][j]:
                if h[i][j + 1] > h[i][j]:
                    if h[i - 1][j] > h[i][j]:
                        if h[i + 1][j] > h[i][j]:
                            lp.append(h[i][j])

    return sum(lp) + len(lp)


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        lines = [[int(n) for n in list(line)] for line in f.read().splitlines()]

    print(part_one(lines))
