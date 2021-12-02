import re


def main():
    with open('./input.txt') as f:
        rules = f.read().splitlines()

    part_one(rules)
    part_two(rules)


def part_one(rules):
    rules = organise_bags(1, rules)
    number_of_bags = 0

    for bag in rules:
        if bag != 'shiny gold':
            number_of_bags += bag_in_rules(rules[bag], rules)

    print(number_of_bags)


def part_two(rules):
    rules = organise_bags(2, rules)
    print(rules)
    number_of_bags = contained_bags(rules['shiny gold'], rules)

    print(number_of_bags)


def organise_bags(part, rules):
    organised_rules = {}

    for rule in rules:
        parent_bag = re.compile(r'([a-z ]*) bags? contain').findall(rule)[0]
        child_bag = ""
        if part == 1:
            child_bag = re.compile(r'[0-9] ([a-z]* [a-z]*) bags?').findall(rule)
        if part == 2:
            child_bag = re.compile(r'([0-9]) ([a-z]* [a-z]*) bags?').findall(rule)

        organised_rules[parent_bag] = child_bag

    return organised_rules


def bag_in_rules(bags, rules):
    number_of_bags = 0
    if 'shiny gold' in bags:
        number_of_bags = 1
    else:
        for bag in bags:
            number_of_bags += bag_in_rules(rules[bag], rules)
    if number_of_bags > 0:
        return 1
    else:
        return 0


def contained_bags(bags, rules):
    number_of_bags = 0
    for count, bag in bags:
        number_of_bags += int(count)
        number_of_bags += int(count) * contained_bags(rules[bag], rules)
    return number_of_bags


main()
