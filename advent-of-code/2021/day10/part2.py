# --- Day 10: Syntax Scoring ---

scoretable = {")": 1, "]": 2, "}": 3, ">": 4}

brackets = {"open": set(["(", "[", "{", "<"]), "close": set([")", "]", "}", ">"])}

map_close_open = {")": "(", "]": "[", "}": "{", ">": "<"}
map_open_close = {"(": ")", "[": "]", "{": "}", "<": ">"}


def solution():
    with open("input.txt") as fr:
        scores = []

        for line in fr.readlines():
            stack = []

            for b in line.strip():
                if b in brackets["open"]:
                    stack.append(b)
                elif b in brackets["close"]:
                    lb = stack.pop()
                    if map_close_open[b] != lb:
                        stack = []
                        break
                else:
                    print(f"Unrecognised character {b}")

            if len(stack) > 0:
                score = 0
                for b in stack[::-1]:
                    cb = map_open_close[b]
                    score *= 5
                    score += scoretable[cb]

                scores.append(score)

    middle_score = sorted(scores)[len(scores) // 2]
    print(f"The middle score is {middle_score}")


if __name__ == "__main__":
    solution()
