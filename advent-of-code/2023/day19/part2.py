import re
from operator import mul
from functools import reduce


def parse_workflows(workflows):
    cond_patt = r"(\w)([<>])(\d+):(\w+)"
    parsed = {}

    for wf in workflows:
        name, conditions = wf.split("{")
        conditions = conditions[:-1].split(",")
        rules, fallback = [], None
        for c in conditions:
            m = re.search(cond_patt, c)
            if m:
                key, op, v, next = m.groups()
                rules.append((key, op, int(v), next))
            else:
                fallback = c

        parsed[name] = (rules, fallback)
    return parsed


def possible(workflows, ranges, name="in"):
    if name == "R":
        return 0

    if name == "A":
        return reduce(mul, [h - l + 1 for l, h in ranges.values()], 1)

    rules, fallback = workflows[name]
    count = 0

    for key, cmp, n, next in rules:
        l, h = ranges[key]
        if cmp == "<":
            true_branch = (l, n - 1)
            false_branch = (n, h)
        else:
            true_branch = (n + 1, h)
            false_branch = (l, n)

        if true_branch[0] <= true_branch[1]:
            mod_ranges = dict(ranges)
            mod_ranges[key] = true_branch
            count += possible(workflows, mod_ranges, next)

        if false_branch[0] <= false_branch[1]:
            ranges = dict(ranges)
            ranges[key] = false_branch
        else:
            break
    else:
        count += possible(workflows, ranges, fallback)

    return count


def solve():
    with open("input.txt") as fr:
        workflows, _ = fr.read().strip().split("\n\n")
        workflows = parse_workflows(workflows.split("\n"))

    ranges = {k: (1, 4000) for k in "xmas"}
    answer = possible(workflows, ranges)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    solve()
