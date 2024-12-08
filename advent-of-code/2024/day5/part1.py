def check_rules(rules, page_numbers):
    for i in range(len(page_numbers)):
        current = page_numbers[i]
        before = page_numbers[:i]
        after = page_numbers[i + 1 :]

        before_rule = len(rules[current]["before"].intersection(before)) == len(before)
        after_rule = len(rules[current]["after"].intersection(after)) == len(after)

        if not before_rule or not after_rule:
            return False

    return True


def solve():
    with open("input.txt") as fr:
        page_ordering_rules, updates = fr.read().strip().split("\n\n")

    rules = {}

    for rule in page_ordering_rules.split("\n"):
        x, y = map(int, rule.split("|"))

        if not rules.get(x):
            rules[x] = {"before": set(), "after": set()}
        if not rules.get(y):
            rules[y] = {"before": set(), "after": set()}

        rules[x]["after"].add(y)
        rules[y]["before"].add(x)

    answer = 0

    for update in updates.split("\n"):
        page_numbers = [int(x) for x in update.split(",")]
        passes_rules = check_rules(rules, page_numbers)
        if passes_rules:
            answer += page_numbers[len(page_numbers) // 2]

    print(f"Answer: {answer}")


if __name__ == "__main__":
    solve()
