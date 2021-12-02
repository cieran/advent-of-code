def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    print(part_one(lines))


def part_one(data):
    section = 0
    ranges = []
    ans = 0
    for line in data:
        if line == "":
            section += 1
            continue
        if section == 0:
            line = line.split(": ")
            line_ranges = line[1].split(" or ")
            lower_range = [int(n) for n in line_ranges[0].split("-")]
            upper_range = [int(n) for n in line_ranges[1].split("-")]

            ranges.append((lower_range, upper_range))
        if section == 1:
            continue
        if section == 2 and line != "nearby tickets:":
            values = [int(n) for n in line.split(",")]
            for value in values:
                valid = False
                for r in ranges:
                    r1, r2 = r
                    if r1[0] <= value <= r1[1] or r2[0] <= value <= r2[1]:
                        valid = True
                        break
                if not valid:
                    ans += value

    return ans


main()