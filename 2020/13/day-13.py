def get_input() -> list:
    with open('input.txt') as f:
        return [l.strip() for l in f.readlines()]


def format_input(lines: list) -> dict:
    obj = {
        "timestamp": int(lines[0]),
        "buses": [(idx, int(val))
                  for idx, val in enumerate(lines[1].split(",")) if val != "x"]
    }
    return obj


def part1(val: dict) -> int:
    wait, bus = min((bus - (val["timestamp"] % bus), bus)
                    for _, bus in val["buses"])
    return wait * bus


def part2(val: dict) -> int:
    size = len(val["buses"])
    inc = val["buses"][0][1]
    result = inc
    next_bus_idx = 1
    while True:
        if all((result + i) % bus == 0 for i, bus in val["buses"][1:next_bus_idx + 1]):
            if next_bus_idx + 1 == size:
                break
            inc *= val["buses"][next_bus_idx][1]
            next_bus_idx += 1
        result += inc
    return result


def main():
    file_input = format_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = format_input([
        "939",
        "7,13,x,x,59,x,31,19"
    ])
    assert part1(test_input) == 295
    assert part2(test_input) == 1068781


if __name__ == "__main__":
    test()
    main()
