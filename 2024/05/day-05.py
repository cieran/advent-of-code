import math 

def main():
    with open('input.txt') as f:
        data = f.read().splitlines()
    
    ordering_rules = {}
    pages_to_produce = []

    for d in data:
        if d.__contains__('|'):
            key, value = [int(rule) for rule in d.split('|')]
            if ordering_rules.__contains__(key):
                ordering_rules[key].append(value)
            else:
                ordering_rules[key] = [value]
        elif d.__contains__(','):
            pages = [int(page) for page in d.split(',')]
            pages_to_produce.append(pages)

    for key in ordering_rules:
        ordering_rules[key].sort()
    
    correct_order = []
    incorrect_order = []
    for pages in pages_to_produce:
        if is_correct_order(ordering_rules, pages):
            correct_order.append(pages)
        else:
            incorrect_order.append(pages)

    print(part_one(correct_order))
    print(part_two(incorrect_order, ordering_rules, []))

def part_one(correct_order):
    return sum_middle_pages(correct_order)

def part_two(incorrect_order, ordering_rules, correct_order):
    while incorrect_order:
        pages = incorrect_order.pop(0)
        if is_correct_order(ordering_rules, pages):
            correct_order.append(pages)
        else:
            for page in pages:
                page_index = pages.index(page)
                behind = pages[:page_index]
                pages_to_come_before = ordering_rules.get(page)
                if pages_to_come_before is not None and len(behind) > 0:
                    pages_that_are_before = [p for p in pages_to_come_before if p in behind]
                    if pages_that_are_before:
                        indices = [pages.index(p) for p in pages_that_are_before]
                        value_at_min_index = pages[min(indices)]
                        pages[min(indices)] = page
                        pages[page_index] = value_at_min_index
                        incorrect_order.append(pages)
                        break
            else:
                correct_order.append(pages)

    return sum_middle_pages(correct_order)

def is_correct_order(ordering_rules, pages):
    for page in pages:
        behind = pages[:pages.index(page)]
        pages_to_come_before = ordering_rules.get(page)
        if pages_to_come_before is not None and len(behind) > 0:
            if any(p in behind for p in pages_to_come_before):
                return False
    return True
        
def is_correct_order(ordering_rules, pages):
    for page in pages:
        behind = pages[:pages.index(page)]
        pages_to_come_before = ordering_rules.get(page)
        if pages_to_come_before is not None and len(behind) > 0:
            if any(p in behind for p in pages_to_come_before):
                return False
    return True

def sum_middle_pages(pages):
    middle_sum = 0
    for page in pages:
        middle_index = math.ceil(len(page) // 2)
        middle_sum += page[middle_index]
    return middle_sum
       

if __name__ == '__main__':
    main()