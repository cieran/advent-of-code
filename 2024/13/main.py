import re

def main():
    with open('test.txt') as f:
        list = f.read().split("\n\n")
    
    part_one = 0
    part_two = 0

    for buttons in list:
        ax, ay, bx, by, px, py = map(int, re.findall(r'\d+', buttons))
        part_one += solve(ax, bx, ay, by, px, py)
        part_two += solve(ax, bx, ay, by, px+10000000000000, py+10000000000000)

    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")


def solve(ax, bx, ay, by, px, py):

    d = (ax * by) - (bx * ay)
    a = (px * by / d) - (py * bx / d)
    b = (-px * ay / d) + (py * ax / d)

    print(a, b, d)
    
    return (3 * round(a)) + round(b) if close_enough(a, round(a)) and close_enough(b, round(b)) else 0

def close_enough(n, nr):
        return abs(n - nr) < 0.001

if __name__ == '__main__':
    main()