import monkeys
import math

def main():
    # Open the input file and read its contents
    with open('./data/sample.txt', 'r') as f:
        data = f.read().split('\n')

    ms = monkeys.get_monkeys(data)

    for i in range(0,20):           
        simulate(i,ms)

    total_inspected = []
    for k,v in ms.items():
        total_inspected.append(v['total_items'])
    
    total_inspected.sort(reverse=True)
    x,y = total_inspected[:2]
    print(x*y)


def simulate(i,ms):
    for m in ms.values():
        for _ in range(0, len(m['starting_items'])):
            item = m['starting_items'].pop(0)
            worry = calculate_worry(item, m['operation'])
            new_worry, throw_to = test(worry,m)
            ms[throw_to]['starting_items'].append(new_worry)
            m['total_items'] += 1
        
def calculate_worry(i, operation):
    operator = operation[0]
    operand = operation[1]

    if operand.isnumeric():
        return calc(i, int(operand), operator)
    else:
        return calc(i, i, operator)
    
def test(worry, m):
    new_worry = bored(worry)
    #new_worry = worry
    if new_worry % int(m['test'].split()[2]) == 0:
        return new_worry, m['if_true']
    else:
        return new_worry, m['if_false']

def bored(worry):
    return math.floor(worry/3)

def calc(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2




if __name__ == "__main__":
    main()