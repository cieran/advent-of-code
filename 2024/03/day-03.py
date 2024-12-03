import re

def main():
    with open('input.txt') as f:
        corrupted = f.read()

    print(part_one(corrupted))
    print(part_two(corrupted))

def part_one(corrupted):
    test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, corrupted)
    multiplied = [int(x) * int(y) for x, y in matches]
    return sum(multiplied)

def part_two(corrupted):
    test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    chunks = re.split(r"(do\(\)|don't\(\))", corrupted)

    enabled = True
    matches = []

    for chunk in chunks:
        if chunk in {"do()", "don't()"}:
            enabled = chunk == "do()"
        elif enabled:
            matches.extend(re.findall(pattern, chunk))

    multiplied = [int(x) * int(y) for x, y in matches]
    return sum(multiplied)

main()