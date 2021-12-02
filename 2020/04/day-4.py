import re


def main():
    with open('./input.txt') as f:
        lines = f.read().split("\n\n")

    print(part_one(lines))
    print(part_two(lines))


def part_one(lines):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = 0
    for line in lines:
        line = line.rstrip("\n")
        if all(code in line for code in fields):
            valid_passports += 1

    return valid_passports


def part_two(lines):
    valid_passports = 0

    for line in lines:
        # robbed RE from stock overflow
        passport = re.split(":| |\n", line)
        passport = {passport[i]: passport[i + 1] for i in range(0, len(passport), 2)}

        if is_valid_passport(passport):
            valid_passports += 1

    return valid_passports


def is_valid_passport(passport):
    if len(passport) not in range(7, 9) or ("cid" in passport and len(passport) == 7):
        return False
    if int(passport["byr"]) not in range(1920, 2003):
        return False
    if int(passport["iyr"]) not in range(2010, 2021):
        return False
    if int(passport["eyr"]) not in range(2020, 2031):
        return False
    if passport["hgt"][-2:] not in ["cm", "in"]:
        return False
    if passport["hgt"][-2:] == "cm" and int(passport["hgt"][:-2]) not in range(150, 194):
        return False
    if passport["hgt"][-2:] == "in" and int(passport["hgt"][:-2]) not in range(59, 77):
        return False
    if passport["hcl"][0] != "#" or len(passport["hcl"]) != 7:
        return False
    # thank you stack overflow for this RE lmaooo
    if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport["hcl"]) is False:
        return False
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if (not passport["pid"].isnumeric()) or len(passport["pid"]) != 9:
        return False

    # congrats you made it through the gauntlet
    return True


main()
