def main(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    print(part_one(lines))
    print(part_two(lines))

def part_one(lines):
    joltage = []
    for line in lines:
        joltage.append(get_max_joltage(2, line))
    return sum(joltage)

def part_two(lines):
    joltage = []
    for line in lines:
        joltage.append(get_max_joltage(12, line))
    return sum(joltage)

def get_max_joltage(digits, line):
    largest_number = ""
    start = 0
    for i in range(digits, 0, -1):
        max_digit = '0'
        max_pos = start
        for i in range(start, len(line) - i + 1):
            if line[i] > max_digit:
                max_digit = line[i]
                max_pos = i
        largest_number += max_digit
        start = max_pos + 1
    return int(largest_number)

# my original solve for part one which couldn't scale for part two
def original_get_max_joltage(line):
    largest_number = 0
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if int(line[i] + line[j]) > largest_number:
                largest_number = int(line[i] + line[j])
    return largest_number


if __name__ == '__main__':
    main('./test.txt')
    main('./input.txt')