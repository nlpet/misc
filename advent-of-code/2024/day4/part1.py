def is_valid(letters):
    allowed = ["X", "M", "A", "S"]
    return letters == allowed or letters[::-1] == allowed


def solve():
    with open("input.txt") as fr:
        wordsearch = [list(line.strip()) for line in fr.readlines()]

    size = len(wordsearch)
    count = 0

    for row in range(size):
        for col in range(size):
            if wordsearch[row][col] == "X" or wordsearch[row][col] == "S":
                # try horizontal forward
                letters = wordsearch[row][col : col + 4]
                if is_valid(letters):
                    count += 1

                # try vertical downwards
                if row < size - 3:
                    letters = [wordsearch[row + r][col] for r in range(4)]
                    if is_valid(letters):
                        count += 1

                # try diagonal down right
                if row < size - 3 and col < size - 3:
                    dirs = [(0, 0), (1, 1), (2, 2), (3, 3)]
                    letters = [wordsearch[row + r][col + c] for r, c in dirs]
                    if is_valid(letters):
                        count += 1

                # try diagonal down left
                if row < size - 3 and col >= 3:
                    dirs = [(0, 0), (1, -1), (2, -2), (3, -3)]
                    letters = [wordsearch[row + r][col + c] for r, c in dirs]
                    if is_valid(letters):
                        count += 1

    print(f"Answer: {count}")


if __name__ == "__main__":
    solve()
