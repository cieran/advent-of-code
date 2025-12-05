def main(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    fresh = lines[:lines.index('')]
    fresh = [list(map(int, line.split('-'))) for line in fresh]
    ingredients = lines[lines.index('')+1:]

    print(part_one(fresh, ingredients))
    print(part_two(fresh))

def part_one(fresh, ingredients):
    count = 0
    for ingredient in ingredients:
        for f in fresh:
            if int(ingredient) in range(f[0], f[1]+1):
                count += 1
                break
    return count

def part_two(fresh):
    count = 0
    sorted_ranges = sorted(fresh)
    merged = [sorted_ranges[0][:]]

    for start, end in sorted_ranges:
        _, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    
    for start, end in merged:
        count += end - start + 1
    return count

if __name__ == '__main__':
    main('./test.txt')
    main('./input.txt')