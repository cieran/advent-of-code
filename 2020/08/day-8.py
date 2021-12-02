import re


def main():
    with open('./input.txt') as f:
        lines = f.read().splitlines()

    ins = []
    for line in lines:
        idx = re.match(r"([\w]{3}) ([+\-\d]+)", line.strip())
        ins.append((idx[1], int(idx[2])))

    print(part_one(ins))
    print(part_two(ins))


def part_one(ins):
    accumulator = 0
    done = set()
    idx = 0

    while idx not in done and idx < len(ins):
        done.add(idx)
        instruction = ins[idx]

        if instruction[0] == 'acc':
            accumulator += instruction[1]
            idx += 1
        elif instruction[0] == 'jmp':
            idx += instruction[1]
        elif instruction[0] == 'nop':
            idx += 1

    return accumulator, idx == len(ins)


def part_two(ins):
    the_ole_switcheroo = {'nop': 'jmp', 'jmp': 'nop'}

    for i in range(len(ins)):
        instruction = ins[i]
        if instruction[0] in the_ole_switcheroo:
            ins[i] = (the_ole_switcheroo[instruction[0]], instruction[1])
            result = part_one(ins)
            if result[1]:
                print(result)

        ins[i] = instruction


main()
