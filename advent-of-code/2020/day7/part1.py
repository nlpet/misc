import re
from collections import defaultdict


def main():
    rules = defaultdict(set)
    qualifying_bags = set([])
    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            source, target = line.strip().split(" bags contain ")
            if target == "no other bags.":
                continue

            bags = re.findall(r"(\w+\s\w+)(?:\sbag|bags)", target)
            for bag in bags:
                rules[bag].add(source)

    candidates = rules["shiny gold"]

    while candidates:
        candidate = candidates.pop()
        qualifying_bags.add(candidate)
        candidates.update(rules.get(candidate, set([])))

    print(f"Number of bag colours is {len(qualifying_bags)}")


if __name__ == "__main__":
    main()
