import numpy as np
from functools import cache

def main():
    with open("input.txt") as f:
        line = np.array([int(i) for i in f.read().split()])
    
    print(sum(apply_rules(num, 25) for num in line))
    print(sum(apply_rules(num, 75) for num in line))
  
@cache
def apply_rules(num, blinks):
    num_str = str(num)
    if blinks == 0: return 1
    if num == 0: return apply_rules(1, blinks-1)
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        return apply_rules(int(num_str[:mid]), blinks-1) + apply_rules(int(num_str[mid:]), blinks-1)
    return apply_rules(num * 2024, blinks-1)

if __name__ == "__main__":
    main()