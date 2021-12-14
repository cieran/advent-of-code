from collections import deque

brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def part_one(data):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    stack = deque()
    score = 0
    for l in data:
        for char in l:
            if char in brackets.values():
                stack.append(char)
                continue
            corrupted = stack.pop()
            if brackets[char] != corrupted:
                score += points[char]

    return score


def part_two(data):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    score = 0
    p2 = []
    for l in data:
        stack = deque()
        valid = True
        for char in l:
            if char in brackets.values():
                stack.append(char)
            else:
                if char == ")" and stack[-1] != "(":
                    valid = False
                    score += points[char]
                    break
                if char == "]" and stack[-1] != "[":
                    valid = False
                    score += points[char]
                    break
                if char == "}" and stack[-1] != "{":
                    valid = False
                    score += points[char]
                    break
                if char == ">" and stack[-1] != "<":
                    valid = False
                    score += points[char]
                    break
                stack.pop()
        if valid:
            p2.append(l)

    scores = []

    for line in p2:
        valid = True
        stack = deque()
        for char in line:
            if char in brackets.values():
                stack.append(char)
            else:
                if ((char == ")" and stack[-1] == "(") or
                    (char == "]" and stack[-1] == "[") or
                    (char == "}" and stack[-1] == "{") or
                        (char == ">" and stack[-1] == "<")):
                    stack.pop()

        score = 0
        stack.reverse()
        for char in stack:
            score = 5 * score
            score += points[list(brackets.keys())
                            [list(brackets.values()).index(char)]]

        scores.append(score)

    scores.sort()
    i = int(len(scores) / 2)

    return scores[i]


if __name__ == "__main__":
    with open('./data/input.txt') as f:
        data = f.read().splitlines()

    print(part_one(data))
    print(part_two(data))
