shape_scores = {"A": 1, "B": 2, "C": 3}
outcome_scores = {"win": 6, "lose": 0, "draw": 3}
winning_combinations = {"A": "C", "B": "A", "C": "B"}
moves = {"X": "A", "Y": "B", "Z": "C"}

def main():
    with open('./data/input.txt') as f:
        lines = f.read().splitlines()

    data = [x.split() for x in lines]
    print(part_one(data))
    print(part_two(data))


def part_one(data):
    total_score = 0
    for x,y in data:
        round_score = 0
        my_move = moves[y]
        shape_score = shape_scores[my_move]
        if x == my_move:
            round_score = outcome_scores["draw"] + shape_score
        elif x == winning_combinations[my_move]:
            round_score = outcome_scores["win"] + shape_score
        else:
            round_score = outcome_scores["lose"] + shape_score
        total_score += round_score
    return total_score

def part_two(data):
    total_score = 0
    desired_outcome = {"X": "lose", "Y": "draw", "Z": "win"}
    for x,y in data:
        round_score = 0
        outcome = desired_outcome[y]
        my_move = generate_move(x, outcome)
        shape_score = shape_scores[my_move]
        outcome_score = outcome_scores[outcome]
        round_score = shape_score + outcome_score
        total_score += round_score
    return total_score

def generate_move(opp_move, outcome):
    if outcome == "draw":
        return opp_move
    if outcome == "win":
        return get_key(opp_move)
    if outcome == "lose":
        return winning_combinations[opp_move]

def get_key(val):
    for key, value in winning_combinations.items():
        if val == value:
            return key

if __name__ == "__main__":
    main()
