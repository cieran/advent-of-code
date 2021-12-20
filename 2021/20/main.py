def sim(lights, bounds, x):
    min_i, max_i, min_j, max_j = bounds
    newlights = set()
    for i in range(min_i-1, max_i+1):
        for j in range(min_j-1, max_j+1):
            g = grid(lights, i, j, bounds, x)
            if alg[g] == '#':
                newlights.add((i,j))
                
    return newlights, (min_i-1, max_i+1, min_j-1, max_j+1)

def grid(lights, i, j, bounds, x):
    min_i, max_i, min_j, max_j = bounds
    binary = []

    # theres gotta be a smarter way to do this
    g = [(i-1, j-1), (i-1, j), (i-1, j+1), 
    (i, j-1), (i, j), (i, j+1), 
    (i+1, j-1), (i+1, j), (i+1, j+1)]

    for pos in g:
        if min_i <= pos[0] < max_i and min_j <= pos[1] < max_j:
            if pos in lights:
                binary.append('1')
            else:
                binary.append('0')
        else:
            binary.append(x)
    binary = ''.join(binary)
    return int(binary, 2)

def solve(alg, img):
    min_i, min_j = 0, 0
    max_i, max_j = len(img), len(img[0])

    lights = set()
    for i in range(max_i):
        for j in range(max_j):
            if img[i][j] == '#':
                lights.add((i,j))

    bounds = (min_i, max_i, min_j, max_j)

    # for the edge
    x = ['0', '0'] if alg[0] == '.' else ['0', '1']

    for i in range(50):
        lights, bounds = sim(lights, bounds, x[i % 2])
        if i == 1:
            # part one
            print(len(lights))
    # part two
    print(len(lights))


if __name__ == "__main__":
    with open ('./data/input.txt') as f:
        alg, img = f.read().split('\n\n')
        alg = alg.strip().replace('\n', '').replace(' ', '')
        img = [l for l in img.split('\n')]

    solve(alg, img)
