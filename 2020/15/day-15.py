def main():
    print(number_game([0, 14, 1, 3, 7, 9]))
    print(number_game([0, 14, 1, 3, 7, 9], 30000000))


def number_game(initial, stop=2020):
    last = 0
    numbers = {v: i + 1 for i, v in enumerate(initial)}
    for turn in range(len(initial) + 1, stop):
        v = numbers.setdefault(last, 0)
        numbers[last] = turn
        last = 0 if v == 0 else turn - v
    return last


main()