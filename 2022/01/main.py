def main():
    with open('./data/input.txt') as f:
        lines = f.readlines()

    print(part_one(lines))
    print(part_two(lines))


def part_one(lines):
    return max(generate_calories(lines))   

def part_two(lines):
    calories = generate_calories(lines)
    calories.sort(reverse=True)
    return sum(calories[0:3])

def generate_calories(lines):
    calories = []
    elf = 0
    for line in lines:
        if line == '\n':
            calories.append(elf)
            elf = 0
            continue
        elf += int(line)
    return calories
    
if __name__ == "__main__":
    main()
