from collections import defaultdict


path = []

def main():
    with open('./data/input.txt') as f:
        lines = f.read().splitlines()
    print(solve(lines))

def solve(lines):
    dir_size = defaultdict(int)
    for line in lines:
        if line.startswith("$ cd"):
            dir = line.split()[2]
            update_path(dir)
        if line[0].isnumeric():
            for p in path:
                dir_size[p] += int(line.split()[0])  
    return calc(dir_size)


def update_path(dir):
    if dir == '..':
        path.pop()
    elif dir == "/":
        path.append(dir)
    else:
        app = path[-1]
        if path[-1] != '/':
            app += '/'
        app += dir
        path.append(app)

def calc(dir_size):
    part_one = sum(n for n in dir_size.values() if n <= 100000)
    part_two = min(n for n in dir_size.values() if n >= (30000000 - (70000000 - dir_size['/'])))
    return part_one, part_two

if __name__ == "__main__":
    main()
