# --- Day 7: Internet Protocol Version 7 ---

import re
from functools import partial
from typing import Tuple, List


def is_aba(s: str) -> bool:
    return s[0] == s[2] and s[0] != s[1]


def get_abas(s: str) -> List[str]:
    abas = []
    for i in range(0, len(s) - 3 + 1):
        if is_aba(s[i: i+3]):
            abas.append(s[i:i+3])
    return abas


def is_bab(s: str, pat: str) -> bool:
    return is_aba(s[0:3]) and pat[0] == s[1] and pat[1] == s[0]


def get_babs(patterns: List[str], s: str) -> bool:
    for i in range(0, len(s) - 3 + 1):
        if any(map(partial(is_bab, s[i: i + 3]), patterns)):
            return True
    return False


def main() -> None:
    brackets_reg = re.compile(r'(\[\w+\])')
    support_ssl = 0

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            brackets = [w[1:-1] for w in brackets_reg.findall(line.strip())]
            outside = re.sub(brackets_reg, ' ', line.strip()).split(' ')
            abas = [s for item in map(get_abas, outside) for s in item]
            if abas and any(map(partial(get_babs, abas), brackets)):
                support_ssl += 1

    print('Number of IPs that support TLS: {}'.format(support_ssl))


if __name__ == '__main__':
    main()
