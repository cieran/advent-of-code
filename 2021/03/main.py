from collections import Counter


def part_one(list_of_bits):
    number_of_bits = len(list_of_bits[0])
    split_bits_vertically = [[list_of_bits[j][i] for j in range(len(list_of_bits))] for i in range(number_of_bits)]

    g_as_binary = [max(set(i), key=i.count) for i in split_bits_vertically]
    g = int(''.join(g_as_binary), base=2)

    e_as_binary = [min(set(i), key=i.count) for i in split_bits_vertically]
    e = int(''.join(e_as_binary), base=2)

    return g * e


def part_two(lines):
    number_of_bits = len(list_of_bits[0])
    oxy = get_oxygen_generator_rating(lines, number_of_bits)
    co2 = get_co2_generator_rating(lines, number_of_bits)

    return get_life_support_rating(oxy, co2)


def get_oxygen_generator_rating(lines, number_of_bits):
    for i in range(number_of_bits):
        if len(lines) == 1:
            break

        count = Counter(list(zip(*lines))[i])
        important_bit = "1" if count["1"] >= count["0"] else "0"
        lines = [line for line in lines if line[i] == important_bit]

    return lines[0]


def get_co2_generator_rating(lines, number_of_bits):
    for i in range(number_of_bits):
        if len(lines) == 1:
            break

        count = Counter(list(zip(*lines))[i])
        important_bit = "0" if count["1"] >= count["0"] else "1"
        lines = [line for line in lines if line[i] == important_bit]

    return lines[0]


def get_life_support_rating(oxygen_generator_rating, co2_scrubber_rating):
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == "__main__":
    with open('./data/sample.txt') as f:
        list_of_bits = f.read().splitlines()

    print(part_one(list_of_bits))
    print(part_two(list_of_bits))
