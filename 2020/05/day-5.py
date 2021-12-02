import re


# test data from advent of code
#
# BFFFBBFRRR    row 70   column 7   seat 567
# FFFBBBFRRR    row 14   column 7   seat 119
# BBFFBBFRLL    row 102  column 4   seat 820

def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    part_one(lines)
    part_two(lines)


def part_one(lines):
    print(max(get_seat_ids(lines)))


def part_two(lines):
    seat_ids = set(sorted(get_seat_ids(lines)))
    all_seats = set(range(1024))
    empty_seats = all_seats - seat_ids

    maybe_my_seat = []

    for seat in empty_seats:
        if 128 < seat < (128 * 7):
            maybe_my_seat.append(seat)

    print(maybe_my_seat[0])


def get_seat_ids(lines):
    seat_ids = []
    for boarding_pass in lines:
        row = get_seat_row(boarding_pass)
        col = get_seat_column(boarding_pass)

        seat_id = (int(row, 2) * 8) + int(col, 2)
        seat_ids.append(seat_id)

    return seat_ids


def get_seat_row(boarding_pass):
    return boarding_pass[:-3].replace('F', '0').replace('B', '1')


def get_seat_column(boarding_pass):
    return boarding_pass[-3:].replace('L', '0').replace('R', '1')


main()
