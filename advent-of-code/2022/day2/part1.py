def solve():
    guide = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    wins = {(2, 1), (3, 2), (1, 3)}

    score = 0

    with open("input.txt") as fr:
        for line in fr.readlines():
            opponent, me = line.strip().split(" ")
            opponent = guide[opponent]
            me = guide[me]
            if (me, opponent) in wins:
                score += 6 + me
            elif me == opponent:
                score += 3 + opponent
            else:
                score += me

    print(score)


if __name__ == "__main__":
    solve()
