# --- Day 18: Snailfish ---

import re
from math import ceil, floor
from collections import defaultdict


pair_patt = re.compile(r"(\[\d+,\d+\])")
single_patt = re.compile(r"\d+")


def parse(number):
    parsed, level, i = [], 0, 0

    while i < len(number):
        if number[i] in {",", " "}:
            i += 1
            continue

        match = re.match(pair_patt, number[i : i + 7])
        if match:
            pair = [int(n) for n in match.group()[1:-1].split(",")]
            parsed.append([level, pair])
            i += len(match.group())
            continue

        match = re.match(single_patt, number[i : i + 2])
        if match:
            parsed.append([level, int(match.group())])
            i += len(match.group())

        if number[i] in {"[", "]"}:
            level += 1 if number[i] == "[" else -1
            i += 1
            continue

    return parsed


def split(n):
    return [int(floor(n / 2)), int(ceil(n / 2))]


def frmt(number):
    result, slevel = [], 0

    for level, n in number:
        if slevel != level:
            if slevel < level:
                last = result[-1] if len(result) > 0 else None

                if last and last != "[":
                    result.append(",")
                result.extend("[" * (level - slevel))
                slevel = level

            else:
                result.extend("]" * (slevel - level))
                slevel = level

        if result[-1] != "[":
            result.append(",")

        if isinstance(n, list):
            n = str(n).replace(" ", "")

        result.append(n)

    result.extend("]" * slevel)

    return "".join(map(str, result))


def explode(number, i, l):
    n1, n2 = number[i][1]

    # explode to the left
    if i > 0:
        j = i - 1
        while j > 0:
            if isinstance(number[j][1], int):
                number[j][1] = number[j][1] + n1
                break
            j -= 1

    # explode to the right
    if i < l - 1:
        j = i + 1
        while j < l - 1:
            if isinstance(number[j][1], int):
                number[j] = [number[j][0] - 1, [0, number[j][1] + n2]]
                number = number[:i] + number[i + 1 :]
                break
            j += 1

    return number


def sreduce(number):
    i, l = 0, len(number)

    while 1:
        level, n = number[i]

        # explode pairs that are nested inside 4 pairs
        if level >= 4 and isinstance(n, list):
            number = explode(number, i, l)
            l -= 1
            i = 0
            continue

        # split number that is 10 or greater
        if isinstance(n, int) and n >= 10:
            number[i] = (level, split(n))
        elif isinstance(n, list):
            n1, n2 = n
            if n1 >= 10:
                sp = [number[i][0] + 1, split(n1)]
                number[i][1] = n2
                number = number[:i] + [sp] + number[i:]
                l += 1
                i = 0
                continue
            elif n2 >= 10:
                import ipdb

                ipdb.set_trace()
                sp = [number[i][0] + 1, split(n2)]
                number[i][1] = n1
                number = number[: i + 1] + [sp] + number[i + 1 :]
                l += 1
                i = 0
                continue

        i += 1

        if i == l - 1:
            break

    return number


def solution():
    with open("test.txt") as fr:
        previous = fr.readline().strip()
        for line in fr.readlines():
            number = line.strip()
            number = f"[{previous},{number}]"
            previous = frmt(sreduce(parse(number)))
            print(previous)


if __name__ == "__main__":
    solution()
