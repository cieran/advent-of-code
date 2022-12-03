def main():
    with open('./data/input.txt') as f:
        lines = f.read().splitlines()
    print(part_one(lines))
    print(part_two(lines))

def part_one(lines):
    total_score = 0
    for line in lines:
        char = get_common_char(line)
        char_score = get_char_score(char)
        total_score += char_score
    return total_score

def part_two(lines):
    total_score = 0
    for i in range(0,len(lines),3):
        total_score += get_char_score(get_badge(lines[i], lines[i+1], lines[i+2]))
    return total_score

def get_char_score(c):
    ascii = ord(c)
    if ascii > 90: return ascii - 96
    else: return ascii - 38
    
def get_common_char(l):
    half = len(l) // 2
    first = l[:half]
    second = l[half:]
    return ''.join(set(first).intersection(second))

def get_badge(l1, l2, l3):
    return ''.join(set(l1).intersection(set(l2)).intersection(set(l3)))

if __name__ == "__main__":
    main()
