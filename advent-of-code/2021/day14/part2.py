# --- Day 14: Extended Polymerization ---

from collections import defaultdict


def solution():
    with open("input.txt") as fr:
        polymer, rules = fr.read().split("\n\n")
        rules_lookup = {}
        for rule in rules.split("\n"):
            a, b = rule.split(" -> ")
            rules_lookup[a] = b

    n_steps = 40
    polymers = {polymer[i - 1 : i + 1]: 1 for i in range(1, len(polymer))}

    for _ in range(n_steps):
        p = defaultdict(int)
        for k, v in polymers.items():
            el = rules_lookup[k]
            p[k[0] + el] += v
            p[el + k[1]] += v
        polymers = p

    elements = defaultdict(int)
    for k, v in polymers.items():
        elements[k[0]] += v
        elements[k[1]] += v

    elements = sorted(elements.items(), key=lambda t: t[1])
    least, most = elements[0][1], elements[-1][1]
    print(most / 2 - least / 2)


if __name__ == "__main__":
    solution()
