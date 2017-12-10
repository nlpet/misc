# --- Day 9: Explosives in Cyberspace ---

from typing import List


def main() -> None:
    with open('input.txt', 'r') as fr:
        decompressed_length = 0

        for line in fr.readlines():
            index = 0
            comps = line.strip()
            decomps: List[str] = []
            while index < len(comps):
                if comps[index] == '(':
                    end = comps[index + 1:].find(')') + index + 1
                    num, times = map(int, comps[index + 1: end].split('x'))
                    decomp = comps[end + 1:end + num + 1] * times
                    decomps.extend(decomp)
                    index = end + 1 + num
                else:
                    decomps.append(comps[index])
                    index += 1

            decompressed_length += sum([1 for ch in decomps if ch != ' '])
    print('Decompressed length of the file is {}'.format(decompressed_length))


if __name__ == '__main__':
    main()
