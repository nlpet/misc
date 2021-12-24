# --- Day 14: Extended Polymerization ---

from collections import Counter


def solution():
    with open("input.txt") as fr:
        polymer, rules = fr.read().split("\n\n")
        rules_lookup = {}
        for rule in rules.split("\n"):
            a, b = rule.split(" -> ")
            rules_lookup[a] = b

    n_steps = 10
    for _ in range(n_steps):
        p = [polymer[0]]
        for i in range(1, len(polymer)):
            a = polymer[i - 1 : i + 1]
            b = rules_lookup["".join(a)]
            p.extend([b, a[1]])
        polymer = p

    c = Counter(polymer).most_common()
    most, least = c[0][1], c[-1][1]
    print(most - least)


if __name__ == "__main__":
    solution()
