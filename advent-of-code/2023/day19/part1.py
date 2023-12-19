import re
from operator import lt, gt


def parse_workflows(workflows):
    ops = {"<": lt, ">": gt}
    cond_patt = r"(\w)([<>])(\d+):(\w+)"
    parsed = {}

    for wf in workflows:
        name, conditions = wf.split("{")
        conditions = conditions[:-1].split(",")
        pipeline = []
        for c in conditions:
            m = re.search(cond_patt, c)
            if m:
                key, op, v, next = m.groups()
                record = {
                    "key": key,
                    "op": ops[op],
                    "value": int(v),
                    "next": next,
                    "type": "eval",
                }
                pipeline.append(record)
            else:
                pipeline.append({"key": c, "type": "goto"})

        parsed[name] = pipeline
    return parsed


def parse_ratings(ratings):
    return [
        {k: int(v) for k, v in dict(re.findall(r"(\w)=(\d+)", rating)).items()}
        for rating in ratings
    ]


def process(workflows, name, rating):
    while True:
        if name in {"A", "R"}:
            return name
        for wf in workflows[name]:
            if wf["type"] == "eval":
                if wf["op"](rating[wf["key"]], wf["value"]):
                    name = wf["next"]
                    break
            else:
                name = wf["key"]


def solve():
    with open("input.txt") as fr:
        workflows, ratings = fr.read().strip().split("\n\n")
        workflows = parse_workflows(workflows.split("\n"))
        ratings = parse_ratings(ratings.split("\n"))

    answer = 0
    for rating in ratings:
        name = "in"
        result = process(workflows, name, rating)
        if result == "A":
            answer += sum(rating.values())

    print(f"Answer: {answer}")


if __name__ == "__main__":
    solve()
