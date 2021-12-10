# --- Day 10: Syntax Scoring ---

scoretable = {")": 3, "]": 57, "}": 1197, ">": 25137}

brackets = {"open": set(["(", "[", "{", "<"]), "close": set([")", "]", "}", ">"])}

mapping = {")": "(", "]": "[", "}": "{", ">": "<"}


def solution():
    with open("input.txt") as fr:
        score = []

        for line in fr.readlines():
            stack = []

            for b in line.strip():
                if b in brackets["open"]:
                    stack.append(b)
                elif b in brackets["close"]:
                    lb = stack.pop()
                    if mapping[b] != lb:
                        score.append(b)
                else:
                    print(f"Unrecognised character {b}")

    score = sum([scoretable[s] for s in score])
    print(f"Total syntax error score is {score}")


if __name__ == "__main__":
    solution()
