def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    # string_split_tester()

    part_one(lines)
    part_two(lines)


def part_one(lines):
    valid = []
    for line in lines:
        split = line.split(":")
        policy = split[0].split(" ")
        password = split[1].strip()
        letter = policy[1]
        min_and_max = policy[0].split("-")
        min, max = int(min_and_max[0]), int(min_and_max[1])
        if (password.count(letter) <= max) and password.count(letter) >= min:
            valid.append(password)
    print('part one:\t', len(valid))


def part_two(lines):
    valid = []
    for line in lines:
        split = line.split(":")
        policy = split[0].split(" ")
        password = split[1].strip()
        letter = policy[1]
        positions = policy[0].split("-")
        x, y = int(positions[0]), int(positions[1])
        is_letter_x_at_position = password[x - 1] == letter
        is_letter_y_at_position = password[y - 1] == letter
        if is_letter_x_at_position != is_letter_y_at_position:
            valid.append(password)
    print('part two:\t', len(valid))


def string_split_tester():
    data = "1-3 a: abcde"
    split = data.split(":")
    policy = split[0].split(" ")
    password = split[1].strip()
    min_and_max = policy[0].split("-")
    letter = policy[1]
    min_occurrences = int(min_and_max[0])
    max_occurrences = int(min_and_max[1])

    print('password:\t', password)
    print('letter:\t\t', letter)
    print('min:\t\t', min_occurrences)
    print('max:\t\t', max_occurrences)
    print('actual:\t\t', password.count(letter))
    # logic for part one
    if (password.count(letter) <= max_occurrences) and password.count(letter) >= min_occurrences:
        print('valid \t\t ✅')
    else:
        print('invalid \t ❌')


main()
