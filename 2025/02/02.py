def main(filename):
    with open(filename) as f:
        lines = f.read().split(',')
        lines = [list(map(int, line.split('-'))) for line in lines]

    part_one(lines)
    part_two(lines)

def part_one(lines):
    invalid = []
    for line in lines:
        for i in range(line[0], line[1]+1):
            if has_repeated_sequence(i):
                invalid.append(i)

    print('part one:\t', sum(invalid))

def part_two(lines):
    invalid = []
    for line in lines:
        for i in range(line[0], line[1]+1):
            if has_repeated_sequence_at_least_twice(i):
                invalid.append(i)

    print('part two:\t', sum(invalid))

def has_repeated_sequence(number):
    number_str = str(number)
    middle = len(number_str) // 2

    if len(number_str) % 2 != 0 or number_str[:middle][0] == '0':
        return False
    
    return number_str[:middle] == number_str[middle:]

def has_repeated_sequence_at_least_twice(number):
    number_str = str(number)
    length = len(number_str)
    
    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:
            pattern = number_str[:pattern_length]
            
            if pattern[0] == '0':
                continue
            
            repetitions = length // pattern_length
            if pattern * repetitions == number_str and repetitions >= 2:
                return True
    
    return False


if __name__ == '__main__':
    main('./test.txt')
    main('./input.txt')