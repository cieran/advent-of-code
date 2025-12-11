def main(filename):
    with open(filename) as f:
        lines = [list(map(int, line.split(','))) for line in f.read().splitlines()]
    
    print(part_one(lines))

def part_one(lines):
    max_area = 0
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            x1, y1 = lines[i]
            x2, y2 = lines[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area
    return max_area
    n = len(polygon)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside

if __name__ == "__main__":
    main("test.txt")
    main("input.txt")