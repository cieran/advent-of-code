def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    print(part_one(lines, 3, 1))
    print(part_two(lines))


def part_one(map_of_slopes, right, down):
    trees = 0
    height, width = len(map_of_slopes), len(map_of_slopes[0])

    # range(x,y,z) - x (start), y (stop), z (step)
    # enumerate the range
    for i, row in enumerate(range(0, height, down)):
        col = (right * i) % width
        if map_of_slopes[row][col] == '#':
            trees += 1

    return trees


def part_two(map_of_slopes):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for right, down in slopes:
        product *= part_one(map_of_slopes, right, down)

    return product

main()
