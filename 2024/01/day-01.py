def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    left = []
    right = []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()
    part_one(left, right)
    part_two(left, right)
    

def part_one(left, right):
    sum = 0
    for i in range(0,len(left)):
        diff = abs(left[i] - right[i])
        sum += diff
    print('part one:\t', sum)


def part_two(left, right):
    sum = 0
    for i in range(0, len(left)):
        num = left[i]
        sum += (num * right.count(num))
    print('part two:\t', sum)


main()
