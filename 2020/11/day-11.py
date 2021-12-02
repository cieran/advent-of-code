from collections import defaultdict

with open('input.txt') as f:
    ls = [line.strip() for line in f.readlines()]

state = {}
floor = set()
for row, line in enumerate(ls):
    for col, char in enumerate(line):
        z = row + col * 1j
        if char == 'L':
            state[z] = False
        else:
            floor.add(z)

dirs = {x + y * 1j for x in (-1, 0, 1) for y in (-1, 0, 1)} - {0}


def eq(state, adjacent, limit):
    while True:
        new_state = {}
        for z, v in state.items():
            adj = [state[a] for a in adjacent[z]]
            new_state[z] = sum(adj) < limit if v else not any(adj)
        if (sum(state.values())) == sum(new_state.values()):
            return sum(state.values())
        state = new_state


# Part 1
adjacent = {z: [z + d for d in dirs if z + d in state] for z in state}
print(eq(state, adjacent, 4))

# Part 2
adjacent = defaultdict(list)
for z, v in state.items():
    for d in dirs:
        loc = z
        while True:
            loc += d
            if loc not in floor:
                if loc in state:
                    adjacent[z].append(loc)
                break

print(eq(state, adjacent, 5))
