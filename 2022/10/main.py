def main():
    with open('./data/input.txt') as f:
        lines = f.read().splitlines()
    
    print(part_one(lines))
    part_two(lines)

def part_one(lines):
    signal_strength = 0
    cycles = 1
    x = 1
    for line in lines:
        instruction = line[:4]
        if instruction == 'noop':
            cycles += 1
        else:
            value = int(line[5:])
            cycles += 1
            signal_strength += calc_signal_strength(x, cycles)
            cycles += 1
            x += value
        signal_strength += calc_signal_strength(x, cycles)
    return signal_strength

def part_two(lines):
    cycles = 0
    pos = 0
    r = ''
    for line in lines:
        instruction = line[:4]
        if instruction == 'noop':
            r = draw_row(pos, r, cycles)
            cycles += 1
        else:
            value = int(line[5:])
            r = draw_row(pos, r, cycles)
            cycles += 1
            if cycles % 40 == 0:
                print(r)
                r = ''
            r = draw_row(pos, r, cycles)
            cycles += 1
            pos += value
        if cycles % 40 == 0:
            print(r)
            r = ''


def draw_row(pos, row, cycles):
    lit = '#'
    dark = '.'
    if (cycles % 40 - pos >= 0) and (cycles % 40 - pos < 3):
        row += lit
    else:
        row += dark
    return row


def calc_signal_strength(x, cycles):
    if cycles % 40 == 20:
        return x * cycles
    else: 
        return 0

if __name__ == "__main__":
    main()
