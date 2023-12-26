def solve():
    # A - Rock, B - Paper, C - Scissors
    guide = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    losses = {"A": "C", "B": "A", "C": "B"}
    wins = {v: k for k, v in losses.items()}
    score = 0

    with open("input.txt") as fr:
        for line in fr.readlines():
            opponent, outcome = line.strip().split(" ")

            if outcome == "X":  # lose
                score += guide[losses[opponent]]
            elif outcome == "Z":  # win
                score += 6 + guide[wins[opponent]]
            else:
                score += 3 + guide[opponent]

    print(score)


if __name__ == "__main__":
    solve()
