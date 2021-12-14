from collections import Counter, defaultdict


def simulate(p, ir, steps):
    polymers = defaultdict(lambda: 0)
    for i in range(0, len(p)-1):
        pair = p[i:i+2]
        polymers[pair] += 1

    for _ in range(steps):
        polymers = step(polymers, ir)

    letters = defaultdict(lambda: 0)
    letters[p[-1]] = 1

    for pair, count in polymers.items():
        letters[pair[0]] += count

    return max(letters.values()) - min(letters.values())


def step(polymers, ir):
    new = defaultdict(lambda: 0)
    for p, c in polymers.items():
        x = p[0] + ir[p]
        y = ir[p] + p[-1]
        new[x] += c
        new[y] += c
    return new


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        data = f.read().split('\n\n')

    ir = {}
    p = data[0]
    for r in data[1].splitlines():
        x, y = r.strip().split(' -> ')
        ir[x] = y

    print(simulate(p, ir, 10))
    print(simulate(p, ir, 40))
