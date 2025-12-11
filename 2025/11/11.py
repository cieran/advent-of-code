from functools import cache

def main(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    data = {}
    for line in lines:
        key, values = line.split(': ')
        data[key] = values.split()

    print(part_one(data))
    print(part_two(data))

def part_one(data):
    def find_all_paths(data, start, end, path=None):
        if path is None:
            path = [start]
        if start == end:
            return [path]
        if start not in data:
            return []
        paths = []
        for node in data[start]:
            if node not in path:
                new_paths = find_all_paths(data, node, end, path + [node])
                paths.extend(new_paths)
        return paths

    return len(find_all_paths(data, 'you', 'out'))

def part_two(data):    
    @cache
    def count_paths(node, seen):
        seen = (seen[0] or node == 'dac', seen[1] or node == 'fft')
        
        if node == 'out':
            return 1 if all(seen) else 0
        if node not in data:
            return 0
        
        return sum(count_paths(next_node, seen) for next_node in data[node])
    
    return count_paths('svr', (False, False))

if __name__ == "__main__":
    main("test.txt")
    main("test-2.txt")
    main("input.txt")