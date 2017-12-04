
def read_input(filename: str) -> str:
    with open(filename, 'r') as fr:
        return fr.read().strip()


def main() -> None:
    seq = read_input('input.txt')
    total = 0
    length = len(seq)

    for i in range(0, len(seq)):
        jump = (i + int(length / 2)) % length
        if seq[i] == seq[jump]:
            total += int(seq[i])

    print(total)


if __name__ == '__main__':
    main()
