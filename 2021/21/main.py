def no_winner(score):
    return score[0] < 1000 and score[1] < 1000

def change_turn(turn):
    return 1 - turn

def part_one(position):
    score = [0, 0]
    player_turn = 0
    used = 0

    while no_winner(score):
        position[player_turn] = (position[player_turn] + 3 * (used + 2)) % 10
        score[player_turn] += 1 + position[player_turn]
        used += 3
        player_turn = change_turn(player_turn)

    return used * score[player_turn]

if __name__ == "__main__":
    position = [9, 2]
    print(part_one(position))
    