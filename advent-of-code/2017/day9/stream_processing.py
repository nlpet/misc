# --- Day 9: Stream Processing ---

from typing import Tuple


def is_cancelled(s: str, index: int) -> Tuple[bool, int]:
    end = index
    while s[index - 1] == '!':
        index -= 1
    return len(s[index: end]) % 2 == 1, index


def remove_garbage(s: str) -> Tuple[str, int]:
    start = s.find('<')
    index = start
    garbage_count = 0

    while start != -1:
        cancelled, cancelled_start = is_cancelled(s, index)
        if cancelled:
            s = s[:cancelled_start] + s[index + 1:]
            index -= index - cancelled_start

        if s[index] == '>':
            s = s[:start] + s[index + 1:]
            garbage_count += index - 1 - start
            start = s.find('<')
            index = start
        else:
            index += 1

    s = s.replace(',', '')
    return s, garbage_count


def count_groups(s: str) -> int:
    score, depth, stack = 0, 0, []

    for ch in s:
        if ch == '{':
            stack.append(ch)
            depth += 1
        else:
            stack.pop()
            score += depth
            depth -= 1

    return score


def main() -> None:
    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            clean_stream, garbage_count = remove_garbage(line.strip())
            group_count = count_groups(clean_stream)
            print('\nTotal score for all groups is {}'.format(group_count))
            print(('The number of non-cancelled characters within the'
                   ' garbage is {}'.format(garbage_count)))


if __name__ == '__main__':
    main()
