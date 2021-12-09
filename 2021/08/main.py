def part_one(data):
    count = 0
    for d in data:
        for t in d:
            if len(t) in [2, 4, 3, 7]:
                count += 1
    return count

def part_two(data):
    t = 0
    for l in data:
        combinations = {}
        uniques = set(l[0])

        combinations[1] = [c for c in uniques if len(c) == 2][0]
        combinations[4] = [c for c in uniques if len(c) == 4][0]
        combinations[7] = [c for c in uniques if len(c) == 3][0]
        combinations[8] = [c for c in uniques if len(c) == 7][0]

        len_6 = [comb for comb in uniques if len(comb) == 6]

        for n in len_6:
            if len(set(n).intersection(set(combinations[1]))) == 1: combinations[6] = n
            elif len(set(n).difference(set(combinations[4]))) == 2: combinations[9] = n
            else: combinations[0] = n

        len_5 = [comb for comb in uniques if len(comb) == 5]

        for n in len_5:
            if len(set(n).difference(set(combinations[1]))) == 3: combinations[3] = n
            elif len(set(n).difference(set(combinations[4]))) == 2: combinations[5] = n
            else: combinations[2] = n

        digits = ""
        for num in l[1]:
            for key, value in combinations.items():
                if set(value) == set(num):
                    digits += str(key)
        t += int(digits)

    return t

if __name__ == "__main__":
    with open('./data/input.txt') as f:
        lines = [line for line in f.readlines()]
        part_one_data = [line.split("|")[1].strip().split() for line in lines]
        part_two_data = [[line.split("|")[0].split(), line.split(" | ")[1].rstrip().split()] for line in lines]

    print(part_one(part_one_data))
    print(part_two(part_two_data))
