from collections import defaultdict


def search_caves(c, v, g):
    if c.islower():
        v.add(c)

    if c == 'end':
        return 1
    p = 0
    for neighbour in g[c]:
        if neighbour not in v:
            p += search_caves(neighbour, set(v), g)
    return p


def search_caves_twice(c, v, g, vt):
    if c.islower():
        v.add(c)

    if c == 'end':
        return 1

    p = 0
    for neighour in g[c]:
        if neighour not in v:
            p += search_caves_twice(neighour, set(v), g, vt)
        if neighour in v and not vt and neighour.islower() and neighour not in ('start', 'end'):
            p += search_caves_twice(neighour, set(v), g, True)
    return p


def part_one(g):
    return search_caves('start', set(), g)


def part_two(g):
    return search_caves_twice('start', set(), g, False)


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        d = [line.strip() for line in f]

    g = defaultdict(lambda: [])

    for l in d:
        x, y = l.split('-')
        g[x].append(y)
        g[y].append(x)

    print(part_one(g))
    print(part_two(g))
