def simulate(lanternfish, days):
    fish_dict = dict((i, 0) for i in range(0, 9))
    for fish in lanternfish:
        fish_dict[fish] += 1
    for _ in range(days):
        zero = fish_dict[0]
        for day in range(0, 8):
            fish_dict[day] = fish_dict[day+1]
        fish_dict[6] += zero
        fish_dict[8] = zero
    return sum(fish_dict.values())


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        lanternfish = [int(age) for age in f.read().strip().split(",")]

    print(simulate(lanternfish, 80))
    print(simulate(lanternfish, 256))
