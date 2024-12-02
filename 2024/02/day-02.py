import itertools

def main():
    with open('input.txt') as f:
        reports = [[int(x) for x in line.split()] for line in f]
    part_one(reports)
    part_two(reports)

def part_one(reports):
    safe = 0
    for report in reports:
        is_safe, bad_levels = check_report(report)
        if is_safe:
            safe += 1
    print('part one:\t', safe)


def part_two(reports):
    safe = 0
    for report in reports:
        subset = []
        is_safe, bad_levels = check_report(report)
        if bad_levels <= 1: 
            is_safe, subset = check_subset_report(report)
        if is_safe: 
            safe += 1               
    print('part two:\t', safe)

def check_report(report):
    bad_levels = 0
    is_safe = True

    for i in range(0, len(report)-1):
        if is_report_sorted(report):
            if is_adjacent_unsafe(i, report):
                is_safe = False
                bad_levels += 1
        else:
            is_safe = False
    return is_safe, bad_levels

def check_subset_report(report):
    combinations = list_combs(report, len(report)-1)
    for subset in combinations:
        is_safe, _ = check_report(subset)
        if is_safe:
            return True, subset
    return False, -1

def is_adjacent_unsafe(i, report):
   return (abs(report[i] - report[i+1]) > 3) or (abs(report[i] - report[i+1] == 0)) 

def is_report_sorted(report):
    return (report == sorted(report, reverse=True)) or (report == sorted(report))

def list_combs(iterable, k): 
    return map(list, itertools.combinations(iterable, k))

main()
