def main():
    with open('./data/input.txt') as f:
        lines = [[int(n) for n in list(line)] for line in f.read().splitlines()]

    w = len(lines[0])
    h = len(lines)

    print(part_one(lines, w, h))
    print(part_two(lines, w, h))
    
def part_one(lines, w, h):
    visible = 0
    for i in range(0, w):
        for j in range(0, h):
            if is_edge(i,j,w,h) or is_taller(i,j,w,h,lines): 
                visible += 1
    return visible

def part_two(lines, w, h):
    scores = []
    for i in range(0, w):
        for j in range(0, h):
            if is_edge(i, j, w, h):
                continue
            else:
                scores.append(get_scenic_score(i, j, w, h, lines))
    return max(scores)


def get_scenic_score(i, j, w, h, lines):
    l = 0
    r = 0
    u = 0
    d = 0
    tree_height = lines[i][j]
    left = [] 
    right = [] 
    up = []
    down = []
    for x in range(0, j):
        left.append(lines[i][x])
    for x in range(i+1, w):
        down.append(lines[x][j])
    for y in range(0, i):
        up.append(lines[y][j])
    for y in range(j+1, h):
        right.append(lines[i][y]) 

    left.reverse()
    up.reverse()
    for i in up:
        if i < tree_height:
            u += 1
        if i >= tree_height:
            u += 1
            break
    
    for i in down:
        if i < tree_height:
            d += 1
        if i >= tree_height:
            d += 1
            break
    
    for i in right:
        if i < tree_height:
            r += 1
        if i >= tree_height:
            r += 1
            break

    for i in left:
        if i < tree_height:
            l += 1
        if i >= tree_height:
            l += 1
            break

    return u*d*l*r


def is_edge(i, j, w, h):
    return True if i==0 or j==0 or i==w-1 or j==w-1 else False

def is_taller(i, j, w, h, lines):
    tree_height = lines[i][j]
    left = [] 
    right = [] 
    up = []
    down = []
    for x in range(0, j):
        left.append(lines[i][x])
    for x in range(i+1, w):
        down.append(lines[x][j])
    for y in range(0, i):
        up.append(lines[y][j])
    for y in range(j+1, h):
        right.append(lines[i][y])   


    if max(left) < tree_height:
        return True
    if max(right) < tree_height:
        return True
    if max(up) < tree_height:
        return True
    if max(down) < tree_height:
        return True
    return False

if __name__ == "__main__":
    main()
