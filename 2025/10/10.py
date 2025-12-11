import re
from itertools import combinations

def main(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    indicators = []
    buttons = []
    joltage = {}

    for line in lines:
        start = line.find('[')
        end = line.find(']')
        if start != -1 and end != -1:
            indicators.append([1 if c == '#' else 0 for c in line[start+1:end]])
        
        matches = re.findall(r'\(([^)]+)\)', line)
        buttons.append([[int(i) for i in m.split(',')] for m in matches])
        
        jolt_match = re.search(r'\{([^}]+)\}', line)
        if jolt_match:
            joltage[len(joltage)] = jolt_match.group(1)
    
    print(part_one(indicators, buttons))

def part_one(indicators, buttons):
    fewest = []
    
    for target, btns in zip(indicators, buttons):
        n = len(target)
        num_buttons = len(btns)
        valid = []
        
        for presses in range(num_buttons + 1):
            for c in combinations(range(num_buttons), presses):
                state = [0] * n
                for i in c:
                    for pos in btns[i]:
                        state[pos] += 1
                
                if [s % 2 for s in state] == target:
                    valid.append(presses)
        
        fewest.append(min(valid))
    
    return sum(fewest)

if __name__ == "__main__":
    main("test.txt")
    main("input.txt")