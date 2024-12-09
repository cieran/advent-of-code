import math 
from collections import Counter
from copy import deepcopy

def main():
    with open('input.txt') as f:
        disk_map = [int(i) for i in f.readline().rstrip()]

    output = []

    for index, num in enumerate(disk_map):
        for _ in range(num):
            output.append(".") if (index % 2 != 0) else output.append(math.ceil(index / 2))

    copy_output = deepcopy(output)
    print(part_one(output))
    print(part_two(copy_output))

def part_one(output):
    left = 0
    right = len(output) - 1

    while left < right:
        if isinstance(output[right], int):
            while left < right and isinstance(output[left], int):
                left += 1
            output[left], output[right] = output[right], output[left]
        right -= 1

    return calculate_checksum(output)

def part_two(output):
    highest = find_highest_digits(output)

    for digit, count, start_index in highest:
        output = move_block(digit, count, start_index, output)

    return calculate_checksum(output)

def find_highest_digits(output):
    highest_digits = []
    i = len(output) - 1

    while i >= 0:
        if isinstance(output[i], int):
            current_digit = output[i]
            count = 1
            start_index = i

            while i - 1 >= 0 and output[i - 1] == current_digit:
                count += 1
                i -= 1

            start_index = i
            highest_digits.append((current_digit, count, start_index))

        i -= 1

    return highest_digits

def move_block(integer, count, starting_index, output):
    dots = 0
    for i in range(len(output)):
        value = output[i]
        if value == '.':
            dots += 1
        else:
            dots = 0

        if dots == count:
            if i < starting_index:
                output[i-dots+1:i+1] = [integer] * count
                output[starting_index:starting_index+count] = ['.'] * count
            break

    return output

def calculate_checksum(output):
    checksum = 0
    for index, num in enumerate(output):
        if isinstance(num, int):
            checksum += (index * num)
    return checksum

if __name__ == '__main__':
    main()