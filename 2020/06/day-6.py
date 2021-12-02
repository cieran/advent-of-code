def main():
    with open('./input.txt') as f:
        lines = f.read().strip().split("\n\n")

    part_one(lines)
    part_two(lines)


def part_one(lines):
    count = 0

    for line in lines:
        letter_set = set()
        line = line.replace('\n', '')
        for letter in line:
            letter_set.add(letter)
        count += len(letter_set)

    print(count)


# i need to stop referring to things as line
# my brain is vibrating
# refactored variable names..
#
# ga = group answers
# pa = person answers
# a = answer
#
def part_two(lines):
    count = 0

    for line in lines:
        line = line.split('\n')
        ga = []
        for pa in line:
            pa_arr = []
            for a in pa:
                pa_arr.append(a)
            ga.append(set(pa_arr))
        count += len(set.intersection(*ga))

    print(count)


main()
