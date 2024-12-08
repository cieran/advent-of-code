from itertools import product
from functools import reduce

def main():
    with open('input.txt') as f:
        data = f.read().splitlines()
    equations = [(int(answer), list(map(int, nums.split()))) for d in data for answer, nums in [d.split(":")]]
    
    print(part_one(equations, '+*'))
    print(part_two(equations, '+*|'))

def part_one(equations, operators):
    total = 0
    for eq in equations:
        numbers = eq[1]
        ps = get_operator_permutations(operators, len(numbers))
        for p in ps:
            result = reduce(lambda i, parms: calculate(i, parms[1], parms[0]),
                         zip(p, numbers[1:]),
                         numbers[0]) 
            if result == eq[0]:
                total += result
                break
    return total

def part_two(equations, operators):
    total = 0
    for eq in equations:
        numbers = eq[1]
        ps = get_operator_permutations(operators, len(numbers))
        for p in ps:
            result = reduce(lambda i, parms: calculate(i, parms[1], parms[0]),
                         zip(p, numbers[1:]),
                         numbers[0]) 
            if result == eq[0]:
                total += result
                break
    return total

def calculate(x, y, o):
    match o:
        case '+':
            return x + y
        case '*':
            return x * y
        case '|':
            return int(str(x) + str(y))
        case _:
            return f'unknown operator {o}'

def get_operator_permutations(operators, i):
    return list(product(operators, repeat=i-1))

    
main()