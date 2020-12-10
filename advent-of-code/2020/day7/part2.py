import re
from collections import defaultdict


def count_bags(bags, bag):
    count = 1
    for nested_bag in bags[bag]:
        m = bags[bag][nested_bag]
        count += m * count_bags(bags, nested_bag)
    return count


def main():
    bags = defaultdict(dict)

    with open("input.txt", "r") as fr:
        for line in fr.readlines():
            source, target = line.strip().split(" bags contain ")
            if target == "no other bags.":
                continue

            for count, c in re.findall(r"(?:(\d+\s)(\w+\s\w+))(?:\sbag|bags)", target):
                bags[source][c] = int(count)

    print("Answer: {}".format(count_bags(bags, "shiny gold") - 1))


if __name__ == "__main__":
    main()
