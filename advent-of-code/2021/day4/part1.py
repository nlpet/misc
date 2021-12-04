# --- Day 4: Giant Squid ---


def format_board(s):
    return [row.split() for row in s.split("\n")]


def score_winner(board, number):
    unmarked_numbers = 0

    for n, is_marked in board.items():
        if is_marked is not True:
            unmarked_numbers += int(n)

    print(f"Final score: {unmarked_numbers * int(number)}")


def mark_boards(numbers, mappings, scores, size):
    for number in numbers:
        for n in range(len(scores)):
            if mappings[n].get(number):
                row, col = mappings[n].get(number)
                mappings[n][number] = True
                scores[n]["rows"][row] += 1
                scores[n]["cols"][col] += 1

                if scores[n]["rows"][row] == size or scores[n]["cols"][col] == size:
                    score_winner(mappings[n], number)
                    return


def solution():
    size = 5

    with open("input.txt") as fr:
        numbers = fr.readline().strip().split(",")
        boards = [format_board(s) for s in fr.read().strip().split("\n\n")]
        mappings, scores = [], []

        # Format boards for easy scoring
        for board in boards:
            mapping = {
                board[row][col]: (row, col)
                for row in range(size)
                for col in range(size)
            }
            mappings.append(mapping)
            scores.append({"rows": [0] * size, "cols": [0] * size})

        # Mark boards and find winner
        mark_boards(numbers, mappings, scores, size)


if __name__ == "__main__":
    solution()
