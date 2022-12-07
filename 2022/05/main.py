import re

stack1 = ["H", "T", "Z", "D"]
stack2 = ["Q", "R", "W", "T", "G", "C", "S"]
stack3 = ["P", "B", "F", "Q", "N", "R", "C", "H"]
stack4 = ["L", "C", "N", "F", "H", "Z"]
stack5 = ["G", "L", "F", "Q", "S"]
stack6 = ["V", "P", "W", "Z", "B", "R", "C", "S"]
stack7 = ["Z", "F", "J"]
stack8 = ["D", "L", "V", "Z", "R", "H", "Q"]
stack9 = ["B", "H", "G", "N", "F", "Z", "L", "D"]
stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

def main():
    with open('./data/input.txt') as f:
        lines = f.readlines()
    solve(lines, False)
    #solve(lines, True)


def solve(lines, bool):
    for line in lines:
        set_of_nums = [int(s) for s in re.findall(r'\d+', line)]
        q,f,t=set_of_nums
        pop_then_push(t, q, stacks[f-1], bool)          
    print_tops()

def pop_then_push(t, q, stack, reverse):
    crane = []
    for _ in range (0, q):
        crane += stack.pop()
    crane.reverse() if reverse else crane
    stacks[t-1].extend(crane) 

def print_tops():
    print(''.join([item[-1] for item in stacks]))

if __name__ == "__main__":
    main()
