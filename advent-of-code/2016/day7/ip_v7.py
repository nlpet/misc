# --- Day 7: Internet Protocol Version 7 ---

import re


def has_abba(s: str) -> bool:
    for i in range(0, len(s) - 4 + 1):
        if s[i:i+2] == s[i + 3] + s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


def main() -> None:
    brackets_reg = re.compile(r'(\[\w+\])')
    support_tls = 0

    with open('input.txt', 'r') as fr:
        for line in fr.readlines():
            brackets = [w[1:-1] for w in brackets_reg.findall(line.strip())]
            abbas = re.sub(brackets_reg, ' ', line.strip()).split(' ')
            if any(map(has_abba, abbas)) and not any(map(has_abba, brackets)):
                support_tls += 1

    print('Number of IPs that support TLS: {}'.format(support_tls))


if __name__ == '__main__':
    main()
