def main():
    with open('./data/input.txt') as f:
        data = f.read()

    sample1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    sample2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    sample3 = "nppdvjthqldpwncqszvftbrmjlhg"
    sample4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    sample5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    assert solve(sample1, 4) == 7 
    assert solve(sample2, 4) == 5
    assert solve(sample3, 4) == 6
    assert solve(sample4, 4) == 10
    assert solve(sample5, 4) == 11

    assert solve(sample1, 14) == 19 
    assert solve(sample2, 14) == 23
    assert solve(sample3, 14) == 23
    assert solve(sample4, 14) == 29
    assert solve(sample5, 14) == 26

    print(solve(data, 4))
    print(solve(data, 14))


def solve(data, num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    seen = {}
    for char in alphabet:
        seen.update({char: 0})
    start = 0
    for idx,chr in enumerate(data):
        val_of_seen = seen[chr]
        if val_of_seen > start:
            start = val_of_seen
        elif (idx+1)-start >= num:
            return idx+1
        seen[chr] = idx+1

if __name__ == "__main__":
    main()
